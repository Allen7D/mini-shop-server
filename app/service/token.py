# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/25.
"""
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, \
	SignatureExpired, BadSignature

from app.libs.error_code import AuthFailed

__author__ = 'Alimazing'

class Token():
	@staticmethod
	def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
		'''生成令牌'''
		s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
		token = s.dumps({
			'uid': uid,
			'type': ac_type.value,
			'scope': scope
		})
		return {'token': token.decode('ascii')}

	@staticmethod
	def decrypt(token):
		'''解析token的信息
		:param token:
		:return: 该token的权限、用户ID、创建时间、有效期
		'''
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token, return_header=True)
		except SignatureExpired:
			raise AuthFailed(msg='token is expired', error_code=1003)
		except BadSignature:
			raise AuthFailed(msg='token is invalid', error_code=1002)

		r = {
			'scope': data[0]['scope'], # 用户权限
			'uid': data[0]['uid'], # 用户ID
			'create_at': data[1]['iat'],  # 创建时间
			'expire_in': data[1]['exp']  # 有效期
		}

		return r