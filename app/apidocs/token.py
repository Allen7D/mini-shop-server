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
			"require": "true",
			"schema": {
				"id": "Token",
				"required": ["account", "secret", "type"],
				"properties": {
					"account": {
						"type": "string",
						"description": "用户名",
						"enum": ["999@qq.com", "888@qq.com"],
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
			"examples": {}
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
