# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/31.
"""
__author__ = 'Alimazing'

from enum import Enum


class ClientTypeEnum(Enum):
	USER_EMAIL = 100
	USER_MOBILE = 101

	# 微信小程序
	USER_MINA = 200
	# 微信公众号
	USER_WX = 201


class ScopeEnum(Enum):
	'''
	「可读性」
	逻辑：数字越大，权限越大
	用法：ScopeEnum.User == ScopeEnum(1) # True
	'''
	User = 1 # 普通用户
	Admin = 2 # 管理员
	Super = 3 # 超级管理员

