# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/14.
"""
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


class UserScope(Scope):
	forbidden_api = ['cms.user+get_user_list', 'cms.user+get_user', 'cms.user+delete_user',
					 'cms.user+update_user'] + \
					[]
	allow_api = ['v1.order+place_order', 'v1.order+get_summary_by_user'] + \
				['v1.pay+get_pre_order'] + \
				[]

	def __init__(self):
		self + AdminScope()


class AdminScope(Scope):
	# allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
	allow_api = ['v1.order+get_detail'] + \
				[]
	allow_module = ['v1.user', 'v1.address', 'v1.product'] + \
				   ['cms.user', 'cms.file']

	def __init__(self):
		pass


class SuperScope(Scope):
	allow_api = []
	allow_module = []

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
