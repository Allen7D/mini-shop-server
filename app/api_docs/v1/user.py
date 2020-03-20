# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/25.
"""
from app.libs.swagger_filed import BodyField

__author__ = 'Allen7D'

email = BodyField('email', 'string', '邮箱', ['462870781@qq.com'])
nickname = BodyField('nickname', 'string', '昵称', ['Allen7D'])
password = BodyField('password', 'string', '密码', ['123456'])