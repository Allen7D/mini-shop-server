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
