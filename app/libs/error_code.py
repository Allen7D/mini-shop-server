# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/12.
"""
from app.core.error import *

__author__ = 'Allen7D'


############################################
##########        第三方错误       ##########
############################################
class WeChatException(APIException):
    code = 500
    error_code = 999  # 属于服务端异常
    msg = '微信服务器接口调用失败'


############################################
##########  登录相关(11000~12000)  ##########
############################################
class ClientTypeError(APIException):
    code = 400
    error_code = 11000
    msg = '登录方式无效'


class AtLeastOneClientException(APIException):
    code = 400
    error_code = 11010
    msg = '无法解绑，至少保留一种登录方式'


############################################
########## 用户类错误(20000~30000) ##########
############################################
class UserException(APIException):
    code = 404
    error_code = 20000
    msg = '用户类通用错误'


class UserNotFound(APIException):
    code = 404
    error_code = 20010
    msg = '没有找到相关用户'


class IdentityException(APIException):
    code = 404
    error_code = 21000
    msg = '用户身份错误'


############################################
########## 商品类错误(30000~40000) ##########
############################################
class ProductException(APIException):
    code = 404
    error_code = 30000
    msg = '产品类通用错误'


class ProductNotFound(APIException):
    code = 404
    error_code = 30010
    msg = '没有找到相关产品'


class CategoryException(APIException):
    code = 404
    error_code = 31000
    msg = '类别类通用错误'


class CategoryNotFound(APIException):
    code = 404
    error_code = 31010
    msg = '没有找到相关类别'


############################################
########## 活动类错误(40000~50000) ##########
############################################

class BannerException(APIException):
    code = 404
    error_code = 40000
    msg = 'Banner类通用错误'


class BannerNotFound(APIException):
    code = 404
    error_code = 40010
    msg = '没有找到相关Banner'


class ThemeException(APIException):
    code = 404
    error_code = 41000
    msg = '主题类通用错误'


class ThemeNotFound(APIException):
    code = 404
    error_code = 41010
    msg = '没有找到相关主题'


############################################
########## 订单类错误(50000~60000) ##########
############################################
class OrderException(APIException):
    code = 404
    error_code = 50000
    msg = '订单类通用错误'


class OrderNotFound(APIException):
    code = 404
    error_code = 50010
    msg = '没有找到相关订单'
