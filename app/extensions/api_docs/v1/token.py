# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.core.swagger_filed import BodyField

__author__ = 'Allen7D'

token = BodyField(name='token', type='string', description='Token', enum=['eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NjM2ODEzMCwiZXhwIjoxNTg4OTYwMTMwfQ.eyJ1aWQiOjEsInR5cGUiOjEwMCwic2NvcGUiOiLns7vnu5_nrqHnkIblkZgifQ.ovFuc5Ti5zGm5B7JS7AGOBBmrYHGCRsVk9OFAWb88LhY7v9Ubw4c_3xGik7K8Emd6_fz4Ho6Hk3GI1_fjcSIww'])
account = BodyField(name='account', type='string', description='用户名(此处可以传邮箱，或者微信登录的code)', enum=["777@qq.com"])
secret = BodyField(name='secret', type='string', description='密码', enum=["123456"])
type = BodyField(name='type', type='integer', description='登录方式', enum=[100])
