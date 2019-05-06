# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/25.
"""
from flask import current_app

from app.libs.error_code import WeChatException
from app.libs.httper import HTTP

__author__ = 'Alimazing'


class OpenToken():
	'''微信·开放平台的Token获取(网页端扫码登录)'''
	def __init__(self, code):
		self.app_id = current_app.config['OPEN_APP_ID']
		self.app_secret = current_app.config['OPEN_APP_SECRET']
		self.code = code
		self.access_token = ''
		self.openid = ''

	@property
	def access_token_url(self):
		return current_app.config['OPEN_ACCESS_TOKEN_URL'].format(self.app_id, self.app_secret, self.code)

	@property
	def user_info_url(self):
		return current_app.config['OPEN_USER_INFO_URL'].format(self.access_token, self.openid)

	def get(self):
		self.__get_access_token()
		user_info = self.__get_user_info()
		return user_info

	def __get_access_token(self):
		result = HTTP.get(self.access_token_url)
		if 'errcode' in result.keys():
			self.__process_login_error(result)
		self.access_token = result['access_token']
		self.openid = result['openid']

	def __get_user_info(self):
		'''
		user_info = {openid: ***, }
		'''
		return HTTP.get(self.user_info_url)

	def __process_login_error(self, wx_result):
		raise WeChatException(
			msg=wx_result['errmsg'],
			error_code=wx_result['errcode'],
		)
