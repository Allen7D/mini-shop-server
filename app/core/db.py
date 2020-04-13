# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/10.
"""
from contextlib import contextmanager
from datetime import datetime
from time import localtime, strftime

from flask import current_app, json
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, Pagination as _Pagination, BaseQuery
from sqlalchemy import Column, BigInteger, orm, inspect

from app.libs.error_code import NotFound, RepeatException
from app.libs.enums import UrlFromEnum

__author__ = 'Allen7D'


def on_update_time():
    now = datetime.now
    return int(round(now().timestamp()))


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
        '''查询出的每一项数据都隐藏keys中的字段'''
        for item in self.items:
            item.hide(*keys)
        return self

    def append(self, *keys):
        '''查询出的每一项数据都添加keys中的字段'''
        for item in self.items:
            item.append(*keys)
        return self


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if hasattr(self.statement.columns, 'delete_time') and 'delete_time' not in kwargs.keys():
            kwargs['delete_time'] = None
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident, e=None, error_code=None, msg=None):
        rv = self.get(ident)  # 查询主键
        if not rv:
            raise e if e else NotFound(error_code=error_code, msg=msg)
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
            raise e if e else NotFound(error_code=error_code, msg=msg)
        return rv

    # def all(self):
    #     rv = list(self)
    #     return rv if len(rv) != 0 else []

    def all_by_wrap(self, wrap='items'):
        rv = self.all()
        return {wrap: rv} if wrap else rv

    def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None):
        '''
        :param page:页码，从1开始
        :param per_page: 每页显示的记录数
        :param error_out: 错误标记(如果是True，如果接收到超出记录范围的页面请求则报错；False则返回空列表)
        :param max_per_page:
        :return:
        '''
        # 使用paginator记的加上filter_by，用于默认添加status=1
        paginator = super(Query, self).paginate(page=page, per_page=per_page, error_out=error_out,
                                                max_per_page=max_per_page)
        return Pagination(self,
                          paginator.page,
                          paginator.per_page,
                          paginator.total,
                          paginator.items
                          )


db = SQLAlchemy(query_class=Query)


class AbortMixin(object):
    '''Mixin 添加终止校验'''

    @classmethod
    def abort_repeat(cls, e: Exception = None, error_code: int = None, msg: str = None, **kwargs):
        instance = cls.query.filter_by(**kwargs).first()
        if instance:
            raise e if e else RepeatException(error_code=error_code, msg=msg)


class CRUDMixin(object):
    '''Mixin 添加CRUD操作: create, get(read), update, delete'''

    @classmethod
    def get(cls, **kwargs):
        '''查询'''
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_or_404(cls, e: Exception = None, error_code: int = None, msg: str = None, **kwargs):
        '''查询，不存在则返回异常'''
        error_kwargs = dict(e=e, error_code=error_code, msg=msg)
        return cls.query.filter_by(**kwargs).first_or_404(**error_kwargs)

    @classmethod
    def get_all(cls, **kwargs):
        '''查询所有'''
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def create(cls, commit: bool = True, **kwargs):
        '''新增'''
        instance = cls()
        for attr, value in kwargs.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)
        return instance.save(commit)

    def update(self, commit: bool = True, **kwargs):
        '''更新'''
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        return self.save(commit)

    def save(self, commit: bool = True):
        '''保存'''
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self):
        '''软删除'''
        with db.auto_commit():
            self.delete_time = int(round(datetime.now().timestamp()))
            self.save()

    def hard_delete(self, commit: bool = True):
        '''硬删除'''
        db.session.delete(self)
        return commit and db.session.commit()


class JSONSerializerMixin(object):
    @orm.reconstructor
    def init_on_load(self):
        # 被隐藏的属性则无法用append方法添加
        self.exclude = []
        self._set_fields() # 由子类重置exclude属性
        all_columns = inspect(self.__class__).columns.keys()  # 该model的所有属性
        self.fields = list(set(all_columns) - set(self.exclude))

    def _set_fields(self):
        pass

    def keys(self):
        '''
        __getitem__和keys 与dict有关;
        item是由key中来的, 因此序列化可控
        app/app.py中JSONEncoder, 会对查询结果dict化;
        '''
        return self.fields

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

    def hide(self, *keys):
        for key in keys:
            if hasattr(self, key) and key in self.fields:
                self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            if hasattr(self, key) and key not in self.fields:
                self.fields.append(key)
        return self

    def set_attrs(self, **kwargs):
        # 快速赋值，用法: set_attrs(form.data)
        for key, value in kwargs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)


class BaseModel(CRUDMixin, AbortMixin, JSONSerializerMixin, db.Model):
    '''基础类，基础的crud model
    '''
    __abstract__ = True

    def delete(self):
        '''删除'''
        db.session.delete(self)
        db.session.commit()

    def _set_fields(self):
        self.exclude = []


class EntityModel(CRUDMixin, AbortMixin, JSONSerializerMixin, db.Model):
    '''实体业务类，提供软删除，及创建、更新、删除时间信息的crud model
    '''
    __abstract__ = True
    create_time = Column('create_time', BigInteger, comment='创建时间')
    update_time = Column('update_time', BigInteger, onupdate=on_update_time, comment='更新时间')
    delete_time = Column('delete_time', BigInteger, comment='删除时间')

    def __init__(self):
        # 时间戳
        self.create_time = int(round(datetime.now().timestamp()))

    def _set_fields(self):
        self.exclude = ['create_time', 'update_time', 'delete_time']

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def get_url(self, url):
        '''图片来源'''
        if (UrlFromEnum(self._from) == UrlFromEnum.LOCAL):
            return current_app.config['IMG_PREFIX'] + url
        return url
