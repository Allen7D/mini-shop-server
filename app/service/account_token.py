# _*_ coding: utf-8 _*_
"""
  Created by Allen on 2018/11/23.
"""
from flask import current_app

from app.service.open_token import OpenToken

__author__ = 'Allen7D'


class AccountToken(OpenToken):
	def __init__(self, code):
		super(AccountToken, self).__init__(code)
		self.app_id = current_app.config['ACCOUNT_APP_ID']
		self.app_secret = current_app.config['ACCOUNT_APP_SECRET']
