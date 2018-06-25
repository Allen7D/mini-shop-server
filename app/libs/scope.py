# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/14.
"""
__author__ = 'Alimazing'


class Scope:
	allow_api = []
	allow_module = []
	forbidden = []

	def __add__(self, other):
		self.allow_api = list(set(self.allow_api + other.allow_api))
		self.allow_module = list(set(self.allow_module + other.allow_module))
		self.forbidden = list(set(self.forbidden + other.forbidden))

		return self


class UserScope(Scope):
	forbidden = ['v1.user+super_fetch_user', 'v1.user+super_delete_user',
				 'v1.user+super_update_user']

	def __init__(self):
		self + AdminScope()


class AdminScope(Scope):
	# allow_api = ['v1.user+super_fetch_user', 'v1.user+super_delete_user']
	allow_module = ['v1.user', 'v1.address']  # 所有视图函数

	def __init__(self):
		# self + (UserScope())
		pass


class SuperScope(Scope):
	allow_api = []
	allow_module = []

	def __init__(self):
		self + UserScope() + AdminScope()


def is_in_scope(scope, endpoint):
	scope = globals()[scope]()
	splits = endpoint.split('+')
	red_name = splits[0]  # v1.*
	if endpoint in scope.forbidden:
		return False
	if endpoint in scope.allow_api:
		return True
	if red_name in scope.allow_module:
		return True
	else:
		return False
