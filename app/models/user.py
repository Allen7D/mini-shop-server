# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from flask import g
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.enums import ScopeEnum
from app.libs.error_code import AuthFailed, UserException
from app.core.db import EntityModel as Base, db
from app.models.group import Group as GroupModel
from app.models.user_address import UserAddress
from app.service.open_token import OpenToken
from app.service.wx_token import WxToken
from app.service.account_token import AccountToken

__author__ = 'Allen7D'


class User(Base):
    '''用户'''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    openid = Column(String(50), unique=True, comment='小程序唯一ID(仅该小程序)')
    unionid = Column(String(50), unique=True, comment='微信唯一ID(全网所有)')
    email = Column(String(24), unique=True, comment='邮箱')
    # mobile = Column(String(16), unique=True)
    nickname = Column(String(24), comment='昵称')
    auth = Column(SmallInteger, default=ScopeEnum.COMMON.value, comment='权限')
    group_id = Column(Integer, comment='用户所属的权限组id')
    _user_address = db.relationship('UserAddress', backref='author', lazy='dynamic')
    _password = Column('password', String(100), comment='密码')
    extend = Column(String(255), comment='额外备注')

    def __repr__(self):
        return '<User(id={0}, nickname={1})>'.format(self.id, self.nickname)

    def keys(self):
        self.hide('openid', 'unionid', '_password', 'extend').append('user_address', 'auth_scope')
        return self.fields

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 用户所有的配送信息
    @property
    def user_address(self):
        return self._user_address.all()

    @property
    def auth_scope(self):
        return db.session.query(GroupModel.name) \
            .filter(GroupModel.id == self.group_id).scalar()

    @property
    def is_admin(self):
        return ScopeEnum(self.auth) == ScopeEnum.ADMIN

    @staticmethod
    def register_by_email(nickname=None, account=None, secret=None):
        """邮箱注册"""
        form = {'nickname': nickname, 'email': account, 'password': secret}
        return User.create(**form)

    @staticmethod
    def register_by_mobile(nickname=None, account=None, secret=None):
        """手机号注册"""
        form = {'nickname': nickname, 'mobile': account, 'password': secret}
        return User.create(**form)

    @staticmethod
    def register_by_wx_mina(account=None):
        """小程序注册"""
        form = {'openid': account}
        return User.create(**form)

    @staticmethod
    def register_by_wx_open(form):
        """
        微信第三方注册
        :param form: 属性包含(openid、unionid、nickname、headimgurl)
        :return:
        """
        return User.create(**form)

    @staticmethod
    def verify_by_email(email, password):
        user = User.query.filter_by(email=email) \
            .first_or_404(e=UserException(msg='该账号未注册'))
        if not user.check_password(password):
            raise AuthFailed(msg='密码错误')
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_mobile(mobile, password):
        user = User.query.filter_by(mobile=mobile) \
            .first_or_404(e=UserException(msg='该账号未注册'))
        if not user.check_password(password):
            raise AuthFailed(msg='密码错误')
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_wx_mina(code, *args):
        ut = WxToken(code)
        wx_result = ut.get()  # wx_result = {session_key, expires_in, openid}
        openid = wx_result['openid']
        user = User.query.filter_by(openid=openid).first()
        # 如果不在数据库，则新建用户
        if not user:
            user = User.register_by_wx_mina(openid)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_wx_open(code, *args):
        # 微信开放平台(第三方)登录
        ot = OpenToken(code)
        user_info = ot.get()
        openid = user_info['openid']  # 用户唯一标识
        user = User.query.filter_by(openid=openid).first()
        if not user:
            user = User.register_by_wx_open(form=user_info)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_wx_account(code, *args):
        ot = AccountToken(code)
        user_info = ot.get()
        unionid = user_info['unionid']
        user = User.query.filter_by(unionid=unionid).first()
        if not user:
            user = User.register_by_wx_open(user_info)
        return {'uid': user.id, 'scope': user.auth_scope}

    @classmethod
    def get_current_user(cls):
        '''获取当前用户的用户信息'''
        return cls.get(id=g.user.uid)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
