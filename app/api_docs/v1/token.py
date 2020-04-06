# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import BodyField

__author__ = 'Allen7D'

token = BodyField(name='token', type='string', description='Token', enum=['eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4Mzk1MDE0NywiZXhwIjoxNTg2NTQyMTQ3fQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.k7QAXaa4Lm4w1CZZWCFulhJdNXhAdiSz9EA5LJWZpV1vjQ6OQUOng5vx2t2x-JHTywCVgJrP8W5frAopBNBDZg'])
account = BodyField(name='account', type='string', description='用户名(此处可以传邮箱，或者微信登录的code)', enum=["777@qq.com"])
secret = BodyField(name='secret', type='string', description='密码', enum=["123456"])
type = BodyField(name='type', type='integer', description='登录方式', enum=[100])
