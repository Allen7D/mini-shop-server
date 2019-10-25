# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
__author__ = 'Allen7D'

from enum import Enum


class ClientTypeEnum(Enum):
	'''客户端登录方式类型'''
	EMAIL = 100 # 邮箱登录
	MOBILE = 101 # 手机登录
	# 微信
	WX_MINA = 200 # 微信小程序
	WX_OPEN = 201 	# 微信第三方登录
	WX = 202 # 微信公众号


class ScopeEnum(Enum):
	'''
	「可读性」
	逻辑：数字越大，权限越大
	用法：ScopeEnum.USER == ScopeEnum(1) # True
	'''
	USER = 1  # 普通用户
	ADMIN = 2  # 管理员
	SUPER = 3  # 超级管理员


class OrderStatusEnum(Enum):
	UNPAID = 1  # 待支付
	PAID = 2  # 已支付
	DELIVERED = 3  # 已发货
	PAID_BUT_OUT_OF = 4  # 已支付，但库存不足
