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
			"description": "登录的基本信息: 账号、密码、登录类型",
			"require": "true",
			"schema": {
				"id": "Token",
				"required": ["account", "secret", "type"],
				"properties": {
					"account": {
						"type": "string",
						"description": "用户名",
						"enum": ["999@qq.com"],
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
					"token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1MzE1OTE0MCwiZXhwIjoxNTU1NzUxMTQwfQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJVc2VyU2NvcGUifQ.5OHN-WF3ujKGcP3kT8lUbVZ-BIKFUgZLZL989X_ae-qjoxI1Sf7O7FRE10s9jk2I1ZRHdYfWdKY-TmSRmn0p-A"
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
							"eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1MzI0NTY3NywiZXhwIjoxNTU1ODM3Njc3fQ.eyJ1aWQiOiIwMDAwYWVmMDc3NGYxMWU4YmE5NTAwMTYzZTBjZTdlNiIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.js9yvuAQ5ia0I2Aw2qWVBiq7C7oMbQGYw5G5uGAn5JS70h_CShD_4SxF1Kpwf--S0ml5lZiWBsRcBgiJe0k4nQ"
						],
						"default": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU1MzI0NTY3NywiZXhwIjoxNTU1ODM3Njc3fQ.eyJ1aWQiOiIwMDAwYWVmMDc3NGYxMWU4YmE5NTAwMTYzZTBjZTdlNiIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.js9yvuAQ5ia0I2Aw2qWVBiq7C7oMbQGYw5G5uGAn5JS70h_CShD_4SxF1Kpwf--S0ml5lZiWBsRcBgiJe0k4nQ"
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
