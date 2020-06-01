# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from flask import g, request, current_app
from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.orm import relationship, backref

from app.libs.enums import ScopeEnum, ClientTypeEnum
from app.core.db import EntityModel as Base, db
from app.models.group import Group
from app.models.address import Address
from app.models.order import Order
from app.models.article import Article
from app.models.identity import Identity

__author__ = 'Allen7D'


class User(Base):
    '''用户'''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), comment='昵称')
    auth = Column(SmallInteger, default=ScopeEnum.COMMON.value, comment='权限')
    group_id = Column(Integer, comment='用户所属的权限组id')
    _avatar = Column('avatar', String(255), comment='头像url')
    identities = relationship('Identity', backref=backref('user', uselist=False))  # 身份
    address = relationship('Address', backref=backref('user', uselist=False))  # 配送地址
    order = relationship('Order', backref=backref('user', uselist=False))  # 订单
    article = relationship('Article', backref=backref('user', uselist=False))  # 文章
    extend = Column(String(255), comment='额外备注')

    def __repr__(self):
        return '<User(id={0}, nickname={1})>'.format(self.id, self.nickname)

    def keys(self):
        self.hide('_password', '_avatar', 'extend')
        self.append('username', 'mobile', 'email', 'openid', 'unionid', 'avatar', 'address', 'auth_scope')
        return self.fields

    @property
    def username(self):
        identity = Identity.get(user_id=self.id, type=ClientTypeEnum.USERNAME.value)
        return identity.identifier if identity else None

    @property
    def mobile(self):
        identity = Identity.get(user_id=self.id, type=ClientTypeEnum.MOBILE.value)
        return identity.identifier if identity else None

    @property
    def email(self):
        identity = Identity.get(user_id=self.id, type=ClientTypeEnum.EMAIL.value)
        return identity.identifier if identity else None

    @property
    def avatar(self):
        if self._avatar is not None:
            host_url = request.host_url
            host_url = host_url.split(',')[-1] if ',' in host_url else host_url
            host_url = host_url[:-1]  # 当前host的路径 http://192.168.10.80:8010
            static_url_path = current_app.static_url_path[1:] + '/avatars'  # static/avatars
            return '{0}/{1}/{2}'.format(host_url, static_url_path, self._avatar)
        return self._avatar

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
