# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/12/4.
"""
__author__ = 'Alimazing'

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
	"parameters": [],
	"responses": {
		"200": {
			"description": "获取成功",
			"examples": {}
		}
	}
}
