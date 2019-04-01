# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/13.
"""
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, \
	SignatureExpired, BadSignature

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success, AuthFailed
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientValidator, TokenValidator

__author__ = 'Alimazing'

api = RedPrint(name='token', description='登录令牌')


@api.route('/user', methods=['POST'])
@api.doc()
def get_token():
	'''生成「令牌」'''
	form = ClientValidator().validate_for_api()
	promise = {
		ClientTypeEnum.USER_EMAIL: User.verify_by_email,
		ClientTypeEnum.USER_WX: User.verify_by_wx,
	}
	# 微信登录则account为code(需要微信小程序调用wx.login接口获取), secret为空
	identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)

	# Token生成
	expiration = current_app.config['TOKEN_EXPIRATION']
	token = generate_auth_token(identity['uid'],
								form.type.data,
								identity['scope'],
								expiration)
	return Success(data=token)


@api.route('/app', methods=['POST'])
def get_app_token():
	pass


@api.route('/secret', methods=['POST'])
@api.doc()
def get_token_info():
	"""解析「令牌」"""
	form = TokenValidator().validate_for_api()
	s = Serializer(current_app.config['SECRET_KEY'])
	try:
		data = s.loads(form.token.data, return_header=True)
	except SignatureExpired:
		raise AuthFailed(msg='token is expired', error_code=1003)
	except BadSignature:
		raise AuthFailed(msg='token is invalid', error_code=1002)

	r = {
		'scope': data[0]['scope'],
		'uid': data[0]['uid'],
		'create_at': data[1]['iat'],  # 创建时间
		'expire_in': data[1]['exp']  # 有效期
	}
	return Success(data=r)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
	'''生成令牌'''
	s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
	token = s.dumps({
		'uid': uid,
		'type': ac_type.value,
		'scope': scope
	})
	return {'token': token.decode('ascii')}
