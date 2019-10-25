# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/22.
"""
from flask import current_app

from app.libs.error_code import WeChatException
from app.libs.httper import HTTP

__author__ = 'Allen7D'


class WxToken():
	'''微信·小程序的Token获取(小程序登录)'''

	def __init__(self, code):
		self.code = code
		self.wx_app_id = current_app.config['APP_ID']
		self.wx_app_secret = current_app.config['APP_SECRET']

	@property
	def wx_login_url(self):
		return current_app.config['LOGIN_URL'].format(
			self.wx_app_id,
			self.wx_app_secret,
			self.code
		)

	def get(self):
		wx_result = HTTP.get(self.wx_login_url)
		self.__process_login_error(wx_result)  # 微信异常处理
		return wx_result

	def __process_login_error(self, wx_result):
		if not wx_result:
			raise WeChatException()
		if 'errcode' in wx_result.keys():
			raise WeChatException(
				msg=wx_result['errmsg'],
				error_code=wx_result['errcode'],
			)
