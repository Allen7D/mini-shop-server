# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/25.
"""
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

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
