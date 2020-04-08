# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/12.
"""
from flask import json

from app.libs.utils import jsonify
from app.core.error import APIException

__author__ = 'Allen7D'


class Success(APIException):
    code = 200
    error_code = 0
    data = None
    msg = '成功'

    def __init__(self, data=None, code=None, error_code=None, msg=None):
        if data:
            self.data = jsonify(data)
        if error_code == 1:
            code = code if code else 201
            msg = msg if msg else '创建 | 更新成功'
        if error_code == 2:
            code = code if code else 202
            msg = msg if msg else '删除成功'
        super(Success, self).__init__(code, error_code, msg)

    def get_body(self, environ=None):
        body = dict(
            error_code=self.error_code,
            msg=self.msg,
            data=self.data
        )
        text = json.dumps(body)  # 返回文本
        return text


class ClientTypeError(APIException):
    code = 400
    error_code = 1006
    msg = 'client is invalid'


class ServerError(APIException):
    code = 500
    error_code = 999
    msg = '服务器端异常'


class WeChatException(ServerError):
    code = 500
    error_code = 999
    msg = '微信服务器接口调用失败'


class ParameterException(APIException):
    code = 400
    error_code = 1000
    msg = '参数无效'


class TokenException(APIException):
    code = 401
    error_code = 1001
    msg = 'Token已过期或无效Token'


class ForbiddenException(APIException):
    code = 403
    error_code = 1004
    msg = '权限不足，禁止访问'


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = '授权失败'


class RepeatException(APIException):
    code = 400
    error_code = 2001
    msg = '重复数据'


class NotFound(APIException):
    code = 404  # http 状态码
    error_code = 1001  # 约定的异常码
    msg = '未查询到数据'  # 异常信息


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
    code = 404
    error_code = 6000
    msg = '用户不存在'


class OrderException(NotFound):
    code = 404
    error_code = 8000
    msg = '订单不存在，请检查ID'
