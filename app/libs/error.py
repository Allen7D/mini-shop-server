# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/12.
"""
from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = 'Allen7D'


class APIException(HTTPException):
	code = 500  # http 状态码
	msg = '服务器未知错误'  # 异常信息
	error_code = 999  # 约定的异常码

	def __init__(self, code=None, error_code=None, msg=None, headers=None):
		if code:
			self.code = code
		if error_code:
			self.error_code = error_code
		if msg:
			self.msg = msg
		super(APIException, self).__init__()

	def get_body(self, environ=None):
		body = dict(
			msg=self.msg,
			error_code=self.error_code,
			request_url=request.method + ' ' + self.get_url_no_param()
		)
		text = json.dumps(body)  # 返回文本
		return text

	def get_headers(self, environ=None):
		return [('Content-type', 'application/json; charset=utf-8')]

	@staticmethod
	def get_url_no_param():
		full_path = str(request.full_path)
		main_path = full_path.split('?')[0]
		return main_path
