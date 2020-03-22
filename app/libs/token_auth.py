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

'''
    「auth实例」被其他api蓝图调用时，已经用verify_password实现了自定义「verify_password_callback」方法
    HTTPBasicAuth自定义的方法包括：
      1. hash_password_callback
      2. verify_password_callback
      3. auth_error_callback
    其中，由于装饰器注入自定义的方法，所以会使用if判断后才执行
    如下
        if self.verify_password_callback:
            return self.verify_password_callback(username, client_password)
      
    因此，@auth.login_required作为授权解析，就能自动用上verify_password方法
'''
auth = HTTPBasicAuth()
UserTuple = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info  # 用「g.user」来记录登录的状态；g只能用于一次请求
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)  # token在请求头
    except BadSignature:
        raise AuthFailed(msg='token 无效', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token 过期', error_code=1003)
    uid = data['uid']  # 用户ID
    ac_type = data['type']  # 登录方式
    scope = data['scope']  # 权限
    # 可以获取要访问的视图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise ForbiddenException(msg='权限不足(等级:{})，禁止访问'.format(scope))
    return UserTuple(uid, ac_type, scope)


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    '''生成令牌'''
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    token = s.dumps({
        'uid': uid,
        'type': ac_type,
        'scope': scope
    })
    return {'token': token.decode('ascii')}
