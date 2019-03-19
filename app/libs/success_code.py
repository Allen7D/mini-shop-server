# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/25.
"""
from flask import json
from app.libs.utils import jsonify
from app.libs.error import APIException

__author__ = 'Alimazing'


class Success(APIException):
	code = 200
	error_code = 0
	data = None  # 结果可以是{} 或 []
	msg = '成功'

	def __init__(self, data=None, code=None, error_code=None, msg=None):
		if data:
			self.data = jsonify(data)
		if error_code == 1:
			code = code if code else 201
			msg = msg if msg else '创建 | 更新成功'
		if error_code == 2:
			code = code if code else 201
			msg = msg if msg else '删除成功'
		super(Success, self).__init__(code, error_code, msg)

	def get_body(self, environ=None):
		body = dict(
			error_code=self.error_code,
			data=self.data
		)
		text = json.dumps(body)  # 返回文本
		return text


class RenewSuccess(Success):
	code = 201
	error_code = 1
	msg = 'renew success'


class DeleteSuccess(Success):
	code = 202
	error_code = 2
	msg = 'delete success'
