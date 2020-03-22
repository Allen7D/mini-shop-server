# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/10.
"""

from contextlib import contextmanager
from datetime import datetime
from flask import current_app, json
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, Pagination as _Pagination, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer, orm, inspect

from app.libs.error_code import NotFound
from time import localtime, strftime

__author__ = 'Allen7D'


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()  # 事务
        except Exception as e:
            self.session.rollback()  # 回滚
            raise e


class Pagination(_Pagination):
    def hide(self, *keys):
        for item in self.items:
            item.hide(*keys)
        return self

    def append(self, *keys):
        for item in self.items:
            item.append(*keys)
        return self


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, e=None, error_code=None, msg=None):
        rv = self.get(ident)  # 查询主键
        if not rv:
            self.__abort_by_error(e)
            raise NotFound(error_code=error_code, msg=msg)
        return rv

    def first_or_404(self, e=None, error_code=None, msg=None):
        '''
        :param e: 异常(exception)
        :param error_code: 错误码
        :param msg: 错误信息
        :return:
        '''
        rv = self.first()
        if not rv:
            self.__abort_by_error(e)
            raise NotFound(error_code=error_code, msg=msg)
        return rv

    def all_or_404(self, e=None, error_code=None, msg=None, wrap=''):
        rv = list(self)
        if not rv:
            self.__abort_by_error(e)
            raise NotFound(error_code=error_code, msg=msg)
        return {wrap: rv} if wrap else rv

    def all(self):
        rv = list(self)
        return rv if len(rv) != 0 else []

    def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None):
        # 使用paginator记的加上filter_by，用于默认添加status=1
        paginator = BaseQuery.paginate(self, page=page, per_page=per_page, error_out=error_out,
                                       max_per_page=max_per_page)
        return Pagination(self,
                          paginator.page,
                          paginator.per_page,
                          paginator.total,
                          paginator.items
                          )

    def __abort_by_error(self, e=None):
        if e:
            raise e


db = SQLAlchemy(query_class=Query)


class CRUDMixin(object):
    """Mixin 添加CRUD操作(create, read, update, delete)."""

    @classmethod
    def get(cls, **kwargs):
        """查"""
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_or_404(cls, e=None, error_code=None, msg=None, **kwargs):
        """查，不存在则返回异常"""
        error_kwargs = dict(e=e, error_code=error_code, msg=msg)
        return cls.query.filter_by(**kwargs).first_or_404(**error_kwargs)

    @classmethod
    def create(cls, commit=True, **kwargs):
        """增"""
        instance = cls()
        for attr, value in kwargs.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)
        return instance.save(commit)

    def update(self, commit=True, **kwargs):
        """更新"""
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        return self.save(commit)

    def save(self, commit=True):
        """保存"""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self):
        """软删除"""
        with db.auto_commit():
            self.status = 0
            self.save()

    def hard_delete(self, commit=True):
        """硬删除"""
        db.session.delete(self)
        return commit and db.session.commit()


class Base(CRUDMixin, db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer, comment='创建时间')
    delete_time = Column(Integer, comment='删除时间')
    update_time = Column(Integer, comment='更新时间')
    status = Column(SmallInteger, default=1, comment='状态，是否软删除')  # 软删除

    @orm.reconstructor
    def init_on_load(self):
        # 被隐藏的属性则无法用append方法添加
        self.exclude = ['create_time', 'update_time', 'delete_time', 'status']
        all_columns = inspect(self.__class__).columns.keys()
        self.fields = list(set(all_columns) - set(self.exclude))

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        attr = getattr(self, item)
        # 将字符串转为JSON
        if isinstance(attr, str):
            try:
                attr = json.loads(attr)
            except ValueError:
                pass
        # 处理时间(时间戳转化)
        if item in ['create_time', 'update_time', 'delete_time']:
            attr = strftime('%Y-%m-%d %H:%M:%S', localtime(attr))
        return attr

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def get_url(self, url):
        if (self._from == 1):
            return current_app.config['IMG_PREFIX'] + url
        else:
            return url

    def set_attrs(self, **kwargs):
        # 快速赋值，用法: set_attrs(form.data)
        for key, value in kwargs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def keys(self):
        # 在 app/app.py中的 JSONEncoder中的 dict(o)使用
        # 在此处，整合要输出的属性：self.fields
        return self.fields

    def hide(self, *keys):
        for key in keys:
            # 使用exclude，在 Model层和 Service层等任意的操作中，已经隐藏的属性无法再添加
            # self.exclude.append(key)
            if key in self.fields:
                self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            if key not in self.fields:
                self.fields.append(key)
        return self
