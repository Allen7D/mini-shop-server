# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/13.
"""
from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
	as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed, ForbiddenException
from app.libs.scope import is_in_scope

__author__ = 'Allen7D'

auth = HTTPBasicAuth()
UserTuple = namedtuple('User', ['uid', 'ac_type', 'scope'])

@auth.verify_password
def verify_password(token, password):
	user_info = verify_auth_token(token)
	if not user_info:
		return False
	else:
		g.user = user_info # 用「g.user」来记录登录的状态；g只能用于一次请求
		return True

def verify_auth_token(token):
	s = Serializer(current_app.config['SECRET_KEY'])
	try:
		data = s.loads(token) # token在请求头
	except BadSignature:
		raise AuthFailed(msg='token 无效', error_code=1002)
	except SignatureExpired:
		raise AuthFailed(msg='token 过期', error_code=1003)
	uid = data['uid']
	ac_type = data['type']
	scope = data['scope']
	# 可以获取要访问的视图函数
	allow = is_in_scope(scope, request.endpoint)
	if not allow:
		raise ForbiddenException()
	return UserTuple(uid, ac_type, scope)
