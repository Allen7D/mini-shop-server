# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/22.
"""
from flask import current_app

from app.libs.error_code import WeChatException
from app.libs.httper import HTTP

__author__ = 'Allen7D'


class WxToken:
	'''微信·小程序的Token获取'''
	def __init__(self, code):
		self.code = code
		self.wx_app_id = current_app.config['APP_ID']
		self.wx_app_secret = current_app.config['APP_SECRET']
		self.wx_login_url = current_app.config['LOGIN_URL'].format(self.wx_app_id, self.wx_app_secret, self.code)

	def get(self):
		wx_result = HTTP.get(self.wx_login_url)
		if not wx_result:
			# 获取session_key及openID时异常，微信内部错误
			raise Exception() # 待完成
		else:
			if 'errcode' in wx_result.keys():
				# loginFail
				self.__process_login_error(wx_result)
			else:
				return wx_result

	def __process_login_error(self, wx_result):
		raise WeChatException(
			msg=wx_result['errmsg'],
			error_code=wx_result['errcode'],
		)

