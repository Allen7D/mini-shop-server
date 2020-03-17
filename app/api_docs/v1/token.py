# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import BodyField
from app.config.setting import token_value

__author__ = 'Allen7D'

get_token = {
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "description": '''登录的基本信息: 账号、密码、登录类型:
                                                           - 邮箱账号登录(type:100)
                                                           - 手机账号登录(type:101)
                                                           - 小程序登录(type:200)
                                                           - 微信扫码登录(type:201)''',
            "schema": {
                "properties": {
                    "account": {
                        "type": "string",
                        "description": "用户名(此处可以传邮箱，或者微信登录的code)",
                        "enum": ["999@qq.com", "888@qq.com", "777@qq.com"],
                        "default": "999@qq.com"
                    },
                    "secret": {
                        "type": "string",
                        "description": "密码",
                        "enum": ["123456"],
                        "default": "123456"
                    },
                    "type": {
                        "type": "integer",
                        "description": "登录方式(100: 邮箱登录; 200: 微信登录)",
                        "enum": [100, 200],
                        "default": 100
                    }
                }
            }
        }
    ]
}

token = BodyField('token', 'string', 'Token', [token_value])
account = BodyField('account', 'string', '用户名(此处可以传邮箱，或者微信登录的code)', ["777@qq.com"])
secret = BodyField('secret', 'string', '密码', ["123456"])
type = BodyField('type', 'integer', '登录方式', [100])
