# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.enums import ScopeEnum
from app.libs.error_code import AuthFailed, UserException
from app.models.base import Base, db
from app.models.user_address import UserAddress
from app.service.open_token import OpenToken
from app.service.wx_token import WxToken

__author__ = 'Allen7D'


class User(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	openid = Column(String(50), unique=True)
	unionid = Column(String(50), unique=True)
	email = Column(String(24), unique=True)
	nickname = Column(String(24), unique=True)
	extend = Column(String(255))
	auth = Column(SmallInteger, default=1)
	_user_address = db.relationship('UserAddress', backref='author', lazy='dynamic')
	_password = Column('password', String(100))

	def keys(self):
		self.hide('openid', 'unionid', '_password', 'extend').append('user_address')
		return self.fields

	@property
	def password(self):
		return self._password

	@property
	def user_address(self):
		return self._user_address.first()

	@password.setter
	def password(self, raw):
		self._password = generate_password_hash(raw)

	def save_address(self, address_info):
		with db.auto_commit():
			# address = UserAddress.query.filter_by(user_id=self.id).first()
			address = self.user_address
			if not address:
				address = UserAddress(author=self)
			address.name = address_info.name
			address.mobile = address_info.mobile
			address.province = address_info.province
			address.city = address_info.city
			address.country = address_info.country
			address.detail = address_info.detail
			db.session.add(address)

	@staticmethod
	def register_by_email(nickname, account, secret):
		"""邮箱注册"""
		with db.auto_commit():
			user = User()
			user.nickname = nickname
			user.email = account
			user.password = secret
			db.session.add(user)
		return user

	@staticmethod
	def register_by_wx(account):
		"""小程序注册"""
		with db.auto_commit():
			user = User()
			user.openid = account
			db.session.add(user)
		return user

	@staticmethod
	def register_by_wx_open(user_info):
		"""微信第三方注册"""
		with db.auto_commit():
			user = User()
			user.openid = user_info['openid']
			user.unionid = user_info['unionid']
			user.nickname = user_info['nickname']
			user.avatar = user_info['headimgurl']
			db.session.add(user)
		return user

	@staticmethod
	def verify_by_email(email, password):
		user = User.query.filter_by(email=email)\
			.first_or_404(e=UserException(msg='该账号未注册'))
		if not user.check_password(password):
			raise AuthFailed(msg='密码错误')
		scope = 'AdminScope' if user.auth == ScopeEnum.Admin else 'UserScope'
		return {'uid': user.id, 'scope': scope}

	@staticmethod
	def verify_by_wx(code, *args):
		ut = WxToken(code)
		wx_result = ut.get()  # wx_result = {session_key, expires_in, openid}
		openid = wx_result['openid']
		user = User.query.filter_by(openid=openid).first()
		# 如果不在数据库，则新建用户
		if not user:
			user = User.register_by_wx(openid)
		scope = 'AdminScope' if user.auth == ScopeEnum.Admin else 'UserScope'
		return {'uid': user.id, 'scope': scope}

	@staticmethod
	def verify_by_wx_open(code, *args):
		# 微信开放平台(第三方)登录
		ot = OpenToken(code)
		user_info = ot.get()
		openid = user_info['openid']  # 用户唯一标识
		user = User.query.filter_by(openid=openid).first()
		if not user:
			user = User.register_by_wx_open(user_info)
		scope = 'AdminScope' if ScopeEnum(user.auth) == ScopeEnum.Admin else 'UserScope'
		return {'uid': user.id, 'scope': scope}

	def check_password(self, raw):
		if not self._password:
			return False
		return check_password_hash(self._password, raw)
