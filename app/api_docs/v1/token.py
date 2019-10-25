# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
__author__ = 'Allen7D'

get_token = {
	"parameters": [
		{
			"name": "body",
			"in": "body",
			"description": '''登录的基本信息: 账号、密码、登录类型\n邮箱账号登录(type:100)\n手机账号登录(type:101)\n小程序登录(type:200)\n微信扫码登录(type:201)''',
			"require": "true",
			"schema": {
				"id": "Token",
				"required": ["account", "secret", "type"],
				"properties": {
					"account": {
						"type": "string",
						"description": "用户名",
						"enum": ["777@qq.com"],
						"default": "777@qq.com"
					},
					"secret": {
						"type": "string",
						"description": "密码",
						"enum": ["123456"],
						"default": "123456"
					},
					"type": {
						"type": "integer",
						"description": "登录方式",
						"enum": [100],
						"default": 100
					}
				}
			}
		}
	],
	"responses": {
		"200": {
			"description": "登录成功",
			"examples": {
				"data": {
					"token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTgxOTk2MywiZXhwIjoxNTc0NDExOTYzfQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.VO3qP77Dlnqt_joixPG2Z_AWXn-DHj2WdBY8xTLxi1Y2cLRA-pkG69dL47q2diAv0f5yO3z2EpMqwfpbnDW3ZQ"
				},
				"error_code": 0
			}
		}
	}
}

get_token_info = {
	"parameters": [
		{
			"name": "body",
			"in": "body",
			"require": "true",
			"schema": {
				"required": ["token"],
				"properties": {
					"token": {
						"type": "string",
						"description": "token",
						"enum": [
							"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTgxOTk2MywiZXhwIjoxNTc0NDExOTYzfQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.VO3qP77Dlnqt_joixPG2Z_AWXn-DHj2WdBY8xTLxi1Y2cLRA-pkG69dL47q2diAv0f5yO3z2EpMqwfpbnDW3ZQ"
						],
						"default": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTgxOTk2MywiZXhwIjoxNTc0NDExOTYzfQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.VO3qP77Dlnqt_joixPG2Z_AWXn-DHj2WdBY8xTLxi1Y2cLRA-pkG69dL47q2diAv0f5yO3z2EpMqwfpbnDW3ZQ"
					}
				}
			}
		}
	],
	"responses": {
		"200": {
			"description": "获取成功",
			"examples": {
				"data": {
					"create_at": 1545142403,
					"expire_in": 1547734403,
					"scope": "UserScope",
					"uid": "0017be56959511e8b34700163e0ce7e6"
				},
				"error_code": 0
			}
		}
	}
}

get_open_redirect_url = {
	"parameters": [],
	"responses": {
		"200": {
			"description": "获取成功",
			"examples": {
				"data": {
					"auth_url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx87186e0123456789&redirect_uri=https%3a%2f%2fapi.izjgk.com%2ftoken%2fuser&response_type=code&scope=snsapi_login&state=3d6be0a4035d839573b04816624a415e#wechat_redirect"
				},
				"error_code": 0
			}
		}
	}
}
