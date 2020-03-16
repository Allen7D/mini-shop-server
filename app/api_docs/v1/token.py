# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import BodyAttr
from app.config.setting import token_value

__author__ = 'Allen7D'


token = BodyAttr('token', 'string', 'Token', [token_value])
account = BodyAttr('account', 'string', '用户名', ["777@qq.com"])
secret = BodyAttr('secret', 'string', '密码', ["123456"])
type = BodyAttr('type', 'integer', '登录方式', [100])