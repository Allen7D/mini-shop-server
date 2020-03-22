# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/14.
"""
from app.libs.enums import ScopeEnum

__author__ = 'Allen7D'


class Scope:
    allow_api = []
    allow_module = []
    forbidden_api = []
    forbidden_module = []

    def __add__(self, other):
        self.allow_api = list(set(self.allow_api + other.allow_api))
        self.allow_module = list(set(self.allow_module + other.allow_module))
        self.forbidden_api = list(set(self.forbidden_api + other.forbidden_api))
        self.forbidden_module = list(set(self.forbidden_module + other.forbidden_module))

        return self

    @staticmethod
    def match_user_scope(auth, type='en'):
        auth_scope_en = {
            ScopeEnum.USER: 'UserScope',
            ScopeEnum.ADMIN: 'AdminScope',
            ScopeEnum.SUPER: 'SuperScope'
        }
        auth_scope_cn = {
            ScopeEnum.USER: '普通用户',
            ScopeEnum.ADMIN: '系统管理员',
            ScopeEnum.SUPER: '系统超级管理员'
        }
        if type == 'en':
            return auth_scope_en.get(ScopeEnum(auth), 'UserScope')
        elif type == 'cn':
            return auth_scope_cn.get(ScopeEnum(auth), '普通用户')


class UserScope(Scope):
    allow_api = [] + \
                []
    allow_module = ['v1.user', 'v1.address', 'v1.theme', 'v1.banner',
                    'v1.category', 'v1.product', 'v1.pay', 'v1.order']
    forbidden_api = [] + \
                    []
    forbidden_module = []

    def __init__(self):
        pass


class AdminScope(Scope):
    allow_api = ['v1.user+get_one', 'v1.user+change_password'] + \
                ['v1.product+get_one', 'v1.product+get_all_by_category'] + \
                ['v1.order+get_one']
    allow_module = ['v1.theme', 'v1.banner', 'v1.category'] + \
                   ['cms.user', 'cms.theme', 'cms.category',
                    'cms.product', 'cms.order', 'cms.file']

    forbidden_api = []
    forbidden_module = []

    def __init__(self):
        # 线上时为 pass
        self + UserScope()


class SuperScope(Scope):
    allow_api = []
    allow_module = []
    forbidden_api = []
    forbidden_module = []

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    """
    判断「访问的用户」是否有该接口的权限
    :param scope: number 权限值
    :param endpoint: string 'v1.user+get_user'
    :return: boolean
    """
    scope = globals()[scope]()  # 基于「string类型变量」查找到同名的类
    red_name = endpoint.split('+')[0]  # v1.*: v1.user 或者 cms.user
    blue_name = red_name.split('.')[0]  # v1或者cms
    if red_name in scope.forbidden_module:
        return False
    if endpoint in scope.forbidden_api:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
