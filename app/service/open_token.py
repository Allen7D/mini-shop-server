# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/25.
"""
from flask import current_app

from app.libs.httper import HTTP

__author__ = 'Alimazing'


class OpenToken:
	def __init__(self, code):
		self.app_id = current_app.config['OPEN_APP_ID']
		self.app_secret = current_app.config['OPEN_APP_SECRET']
		self.scope = current_app.config['OPEN_SCOPE']
		self.state = current_app.config['OPEN_STATE']
		self.redirect_uri = current_app.config['REDIRECT_URI']
		self.code = code
		self.access_token = ''
		self.openid = ''

	@property
	def authorize_url(self):
		return current_app.config['OPEN_AUTHORIZE_URL'].format(self.app_id, self.redirect_uri, self.scope, self.state)

	@property
	def access_token_url(self):
		return current_app.config['OPEN_ACCESS_TOKEN_URL'].format(self.app_id, self.app_secret, self.code)

	@property
	def user_info_url(self):
		return current_app.config['OPEN_USER_INFO_URL'].format(self.access_token, self.openid)

	def get(self):
		self.get_access_token()
		user_info = self.get_user_info()
		return user_info

	def get_access_token(self):
		result = HTTP.get(self.access_token_url)
		self.access_token = result.access_token
		self.openid = result.openid

	def get_user_info(self):
		'''
		user_info = {openid: ***, }
		'''
		return HTTP.get(self.user_info_url)

	def __process_login_error(self):
		pass
