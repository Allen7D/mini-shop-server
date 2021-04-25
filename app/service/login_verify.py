# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, \
    SignatureExpired, BadSignature

from flask import current_app

from app.core.token_auth import generate_auth_token
from app.core.logger import record_login_log
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed, IdentityException
from app.models.identity import Identity
from app.models.user import User
from app.dao.user import UserDao
from app.service.open_token import OpenToken
from app.service.wx_token import WxToken
from app.service.account_token import AccountToken

__author__ = 'Allen7D'


class LoginVerifyService():
    @staticmethod
    def get_token(account, secret, type):
        promise = {
            ClientTypeEnum.USERNAME: LoginVerifyService.verify_by_username,  # 账号&密码登录
            ClientTypeEnum.EMAIL: LoginVerifyService.verify_by_email,  # 邮箱&密码登录
            ClientTypeEnum.MOBILE: LoginVerifyService.verify_by_mobile,  # 手机号&密码登录
            ClientTypeEnum.WX_MINA: LoginVerifyService.verify_by_wx_mina,  # 微信·小程序登录
            ClientTypeEnum.WX_OPEN: LoginVerifyService.verify_by_wx_open,  # 微信·开发平台登录(web端扫码登录)
            ClientTypeEnum.WX_ACCOUNT: LoginVerifyService.verify_by_wx_account  # 微信第三方登录(公众号H5端)
        }
        # 微信登录, 则account为code(需要微信小程序调用wx.login接口查询), secret为空
        identity = promise[ClientTypeEnum(type)](account, secret)
        # token生成
        expiration = current_app.config['TOKEN_EXPIRATION']  # token有效期
        record_login_log(identity['uid'], message='登录成功')
        token = generate_auth_token(identity['uid'],
                                    type.value,
                                    identity['scope'],
                                    expiration)
        return token

    # 解析token的信息
    @staticmethod
    def decrypt_token(token):
        '''
        :param token:
        :return: 该token的权限、用户ID、创建时间、有效期
        '''
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token, return_header=True)  # token在POST中
        except BadSignature:
            raise AuthFailed(msg='token失效，请重新登录', error_code=1002)
        except SignatureExpired:
            raise AuthFailed(msg='token过期，请重新登录', error_code=1003)

        rv = {
            'scope': data[0]['scope'],  # 用户权限
            'uid': data[0]['uid'],  # 用户ID
            'create_at': data[1]['iat'],  # 创建时间
            'expire_in': data[1]['exp']  # 有效期
        }

        return rv

    @staticmethod
    def verify_by_username(username, password):
        identity = Identity.get_or_404(identifier=username, type=ClientTypeEnum.USERNAME.value,
                                       e=IdentityException(msg='该用户名未注册'))
        identity.check_password(password, e=AuthFailed(msg='密码错误'))
        user = User.get(id=identity.user_id)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_email(email, password):
        identity = Identity.get_or_404(identifier=email, type=ClientTypeEnum.EMAIL.value,
                                       e=IdentityException(msg='该邮箱未注册'))
        identity.check_password(password, e=AuthFailed(msg='密码错误'))
        user = User.get(id=identity.user_id)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_mobile(mobile, password):
        identity = Identity.get_or_404(identifier=mobile, type=ClientTypeEnum.MOBILE.value,
                                       e=IdentityException(msg='该手机号未注册'))
        identity.check_password(password, e=AuthFailed(msg='密码错误'))
        user = User.get(id=identity.user_id)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_wx_mina(code, *args):
        ut = WxToken(code)
        wx_result = ut.get()  # wx_result = {session_key, expires_in, openid}
        openid = wx_result['openid']
        identity = Identity.get(identifier=openid, type=ClientTypeEnum.WX_MINA.value)
        # 如果不在数据库，则新建用户
        if not identity:
            user = UserDao.register_by_wx_mina(openid=openid)
        else:
            user = User.get(id=identity.user_id)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_wx_open(code, *args):
        # 微信开放平台(第三方)登录
        ot = OpenToken(code)
        user_info = ot.get()
        openid = user_info['openid']  # 用户唯一标识
        user = User.query.filter_by(openid=openid).first()
        if not user:
            user = UserDao.register_by_wx_open(form=user_info)
        return {'uid': user.id, 'scope': user.auth_scope}

    @staticmethod
    def verify_by_wx_account(code, *args):
        ot = AccountToken(code)
        user_info = ot.get()
        unionid = user_info['unionid']
        user = User.query.filter_by(unionid=unionid).first()
        if not user:
            user = UserDao.register_by_wx_account(form=user_info)
        return {'uid': user.id, 'scope': user.auth_scope}
