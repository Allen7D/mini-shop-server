# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/13.
  ↓↓↓ Token接口 ↓↓↓
"""
from flask import current_app

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.user import User
from app.service.token import Token
from app.libs.token_auth import generate_auth_token
from app.validators.forms import ClientValidator, TokenValidator
from app.api_docs.v1 import token as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='token', description='登录令牌', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['account', 'secret', 'type'], body_desc='''登录的基本信息: 账号、密码、登录类型:
                                                           - 邮箱账号登录(type:100)
                                                           - 手机账号登录(type:101)
                                                           - 小程序登录(type:200)
                                                           - 微信扫码登录(type:201)''')
def get_token():
	'''生成「令牌」(4种登录方式)'''
	form = ClientValidator().validate_for_api()
	promise = {
		ClientTypeEnum.EMAIL: User.verify_by_email,  # 邮箱&密码登录
		ClientTypeEnum.MOBILE: User.verify_by_mobile,  # 手机号&密码登录
		ClientTypeEnum.WX_MINA: User.verify_by_wx_mina,  # 微信·小程序登录
		ClientTypeEnum.WX_OPEN: User.verify_by_wx_open,  # 微信·开发平台登录(web端扫码登录)
		ClientTypeEnum.WX_ACCOUNT: User.verify_by_wx_account # 微信第三方登录(公众号H5端)
	}
	# 微信登录, 则account为code(需要微信小程序调用wx.login接口获取), secret为空
	identity = promise[ClientTypeEnum(form.type.data)](form.account.data, form.secret.data)
	# token生成
	expiration = current_app.config['TOKEN_EXPIRATION']  # token有效期
	token = generate_auth_token(identity['uid'],
								form.type.data.value,
								identity['scope'],
								expiration)
	return Success(data=token)


@api.route('/verify', methods=['POST'])
@api.doc(args=['token'], body_desc='令牌')
def get_token_info():
	"""解析「令牌」"""
	token = TokenValidator().validate_for_api().token.data
	result = Token.decrypt(token)
	return Success(data=result)


@api.route('/open_redirect_url', methods=['GET'])
@api.doc()
def get_open_redirect_url():
	'''微信授权跳转链接
	用于前端弹出微信扫描页面，获取code
	:return: 跳转的链接，用于弹出「微信扫描页面」
	'''
	return Success(data={'redirect_url': current_app.config['OPEN_AUTHORIZE_URL']})
