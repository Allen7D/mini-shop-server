# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from flask import g
from sqlalchemy import Column, Integer, String, SmallInteger
from app.libs.enums import ScopeEnum
from app.core.db import EntityModel as Base, db
from app.models.group import Group
from app.models.identity import Identity

__author__ = 'Allen7D'


class User(Base):
    '''用户'''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), unique=True, comment='小程序唯一ID(仅该小程序)')
    unionid = Column(String(50), unique=True, comment='微信唯一ID(全网所有)')
    nickname = Column(String(24), comment='昵称')
    username = Column(String(24), unique=True, comment='用户名(唯一)')
    email = Column(String(50), unique=True, comment='邮箱(唯一)')
    mobile = Column(String(16), unique=True, comment='手机号(唯一)')
    auth = Column(SmallInteger, default=ScopeEnum.COMMON.value, comment='权限')
    group_id = Column(Integer, comment='用户所属的权限组id')
    _address = db.relationship('Address', backref='author', lazy='dynamic')  # 配送地址
    _order = db.relationship('Order', backref='author', lazy='dynamic')  # 订单
    extend = Column(String(255), comment='额外备注')

    def __repr__(self):
        return '<User(id={0}, nickname={1})>'.format(self.id, self.nickname)

    def keys(self):
        self.hide('openid', 'unionid', '_password', 'extend')
        self.append('username', 'mobile', 'email', 'address', 'auth_scope')
        return self.fields

    # 登录的所有身份
    @property
    def identities(self):
        return Identity.get_all(user_id=self.id)

    # 用户的订单
    @property
    def order(self):
        return self._order.all()

    # 用户所有的配送信息
    @property
    def address(self):
        return self._address.all()

    @property
    def auth_scope(self):
        return db.session.query(Group.name) \
            .filter(Group.id == self.group_id).scalar()

    @property
    def is_admin(self):
        return ScopeEnum(self.auth) == ScopeEnum.ADMIN

    @classmethod
    def get_current_user(cls):
        '''获取当前用户'''
        return g.user
