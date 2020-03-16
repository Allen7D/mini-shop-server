# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import BodyFiled
from app.config.setting import token_value

__author__ = 'Allen7D'


token = BodyFiled('token', 'string', 'Token', [token_value])
account = BodyFiled('account', 'string', '用户名', ["777@qq.com"])
secret = BodyFiled('secret', 'string', '密码', ["123456"])
type = BodyFiled('type', 'integer', '登录方式', [100])