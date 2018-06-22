# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/12.
"""
from flask import json
from app.libs.utils import jsonify
from app.libs.error import APIException

__author__ = 'Alimazing'


class Success(APIException):
	code = 200
	error_code = 0
	data = None  # 结果可以是{} 或 []
	msg = 'fetch success'

	def __init__(self, data=None, code=None, error_code=None, msg=None):
		if data:
			self.data = jsonify(data)
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
	msg = 'renew data success'


class DeleteSuccess(Success):
	code = 202
	error_code = 2
	msg = 'delete success'


class TokenException(APIException):
	code = 400
	error_code = 1001
	msg = 'Token已过期或无效Token'


class ClientTypeError(APIException):
	code = 400
	error_code = 1006
	msg = 'clinet is invalid'


class ServerError(APIException):
	code = 500
	error_code = 999
	msg = 'sorry, we make a mistake!'


class WeChatException(ServerError):
	code = 500
	error_code = 999
	msg = '微信服务器接口调用失败'


class ParameterException(APIException):
	code = 400
	error_code = 1000
	msg = 'invalid parameter'


class AuthFailed(APIException):
	code = 401
	error_code = 1005
	msg = 'authorization failed'


class ForbiddenException(APIException):
	code = 403
	error_code = 1004
	msg = 'forbidden, not in scope'


class DuplicateGift(APIException):
	code = 400
	error_code = 2001
	msg = 'the current book has already in gift'


class NotFound(APIException):
	code = 404
	error_code = 1001
	msg = 'the resource are not found'


class ProductException(NotFound):
	code = 404
	error_code = 2000
	msg = '指定的商品不存在，请检查参数'


class ThemeException(NotFound):
	code = 404
	error_code = 3000
	msg = '请求的主题不存在，请检查主题ID'


class BannerMissException(NotFound):
	code = 404
	error_code = 4000
	msg = '请求的Banner不存在'


class CategoryException(NotFound):
	code = 404
	error_code = 5000
	msg = '指定的类目不存在, 请检查参数'


class UserException(NotFound):
	code = 400
	error_code = 6000
	msg = '用户不存在'


class OrderException(NotFound):
	code = 404
	error_code = 8000
	msg = '订单不存在，请检查ID'
