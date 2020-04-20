# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/13.
  ↓↓↓ Token接口 ↓↓↓
"""
from flask import current_app

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import token as api_doc
from app.service.login_verify import LoginVerifyService
from app.libs.error_code import Success
from app.validators.forms import ClientValidator, TokenValidator

__author__ = 'Allen7D'

api = Redprint(name='token', description='登录令牌', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(args=['g.body.account', 'g.body.secret', 'g.body.type'], body_desc='''登录的基本信息: 账号、密码、登录类型:
                                                           - 用户名登录(type:100)
                                                           - 邮箱账号登录(type:101)
                                                           - 手机账号登录(type:102)
                                                           - 小程序登录(type:200)
                                                           - 微信扫码登录(type:201)''')
def get_token():
    '''生成「令牌」(5种登录方式)'''
    form = ClientValidator().get_data()
    token = LoginVerifyService.get_token(account=form.account, secret=form.secret, type=form.type)
    return Success(data=token)


@api.route('/verify', methods=['POST'])
@api.doc(args=['g.body.token'], body_desc='令牌')
def decrypt_token():
    '''解析「令牌」'''
    token = TokenValidator().get_data().token
    token_info = LoginVerifyService.decrypt_token(token)
    return Success(data=token_info)


@api.route('/open_redirect_url', methods=['GET'])
@api.doc()
def get_open_redirect_url():
    '''微信授权跳转链接
    用于前端弹出微信扫描页面，获取code
    :return: 跳转的链接，用于弹出「微信扫描页面」
    '''
    return Success(data={'redirect_url': current_app.config['OPEN_AUTHORIZE_URL']})
