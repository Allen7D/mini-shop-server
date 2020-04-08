# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/13.
"""
from collections import namedtuple
from functools import wraps

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth as _HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer \
    as Serializer, BadSignature, SignatureExpired

from app.models.user import User as UserModel
from app.libs.error_code import AuthFailed
from app.core.auth import is_in_auth_scope

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


class HTTPBasicAuth(_HTTPBasicAuth):
    def __init__(self, scheme=None, realm=None):
        super(HTTPBasicAuth, self).__init__(scheme, realm)
        self.hash_password(None)
        self.verify_password(None)

    def admin_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if request.method != 'OPTIONS':
                [username, client_password] = [auth.username, auth.password] \
                    if auth else ['', '']
                if self.verify_admin_callback:
                    self.verify_admin_callback(username, client_password)
            return f(*args, **kwargs)

        return decorated

    def verify_admin(self, f):
        self.verify_admin_callback = f
        return f

    def group_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if request.method != 'OPTIONS':
                [username, client_password] = [auth.username, auth.password] \
                    if auth else ['', '']
                if self.verify_group_callback:
                    self.verify_group_callback(username, client_password)
            return f(*args, **kwargs)

        return decorated

    def verify_group(self, f):
        self.verify_group_callback = f
        return f


auth = HTTPBasicAuth()
UserTuple = namedtuple('User', ['uid', 'ac_type', 'scope'])


##### 超级管理员的API校验 #####
@auth.verify_admin
def verify_admin(token, password):
    (uid, ac_type, scope) = decrypt_token(token)
    current_user = UserModel.get_or_404(id=uid)
    if not current_user.is_admin:
        raise AuthFailed(msg='该接口为超级管理员权限操作')
    g.user = UserTuple(uid, ac_type, scope)


##### CMS授权的管理员的API校验 #####
@auth.verify_group
def verify_group(token, password):
    (uid, ac_type, scope) = decrypt_token(token)
    current_user = UserModel.get_or_404(id=uid)
    group_id = current_user.group_id
    # 非admin用户，先进行校验
    if not current_user.is_admin:
        if group_id is None:
            raise AuthFailed(msg='您还不属于任何权限组，请联系系统管理员获得权限')
        allowed = is_in_auth_scope(group_id, request.endpoint)
        if not allowed:
            raise AuthFailed(msg='权限不够，请联系系统管理员获得权限')

    g.user = UserTuple(uid, ac_type, scope)


##### 普通用户的API校验 #####
@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    g.user = user_info  # 用「g.user」来记录登录的状态；g只能用于一次请求
    return True


def verify_auth_token(token):
    # 经过token的解析(包含校验层)
    (uid, ac_type, scope) = decrypt_token(token)
    return UserTuple(uid, ac_type, scope)


def decrypt_token(token):
    '''
    解析(包含校验层)Token成 UserTuple(uid, ac_type, scope)
    :param token:
    :return:
    '''
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
