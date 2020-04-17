# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from enum import Enum

__author__ = 'Allen7D'


class ClientTypeEnum(Enum):
    '''客户端登录方式类型
    站内: 手机号mobile 邮箱email 用户名username
    第三方应用: 微信weixin 腾讯qq 微博weibo
    '''
    USERNAME = 100 # 用户名
    EMAIL = 101  # 邮箱登录
    MOBILE = 102  # 手机登录
    # 微信
    WX_MINA = 200  # 微信小程序(该小程序的openid)
    WX_OPEN = 201  # 微信第三方登录(Web端)
    WX_ACCOUNT = 203  # 微信第三方登录(公众号H5端)

    # 腾讯QQ
    QQ = 300 # QQ登录



class ScopeEnum(Enum):
    '''
    用法：ScopeEnum(1) == ScopeEnum.COMMON # True
    '''
    COMMON = 1  # 普通用户
    ADMIN = 2  # 管理员


class OrderStatusEnum(Enum):
    '''订单的状态'''
    UNPAID = 1  # 待支付
    PAID = 2  # 已支付
    DELIVERED = 3  # 已发货
    PAID_BUT_OUT_OF = 4  # 已支付，但库存不足
    HANDLED_OUT_OF = 5 # 已处理 PAID_BUT_OUT_OF


class UrlFromEnum(Enum):
    '''图片来源'''
    LOCAL = 1  # 1 本地
    NETWORK = 2 # 2 公网

class AtLeastEnum(Enum):
    '''至少的数目'''
    ONE = 1
    TEN = 10