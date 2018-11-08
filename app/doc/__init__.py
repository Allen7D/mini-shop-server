# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/11/5.
"""
from app.libs.param_filed import IntegerQueryFiled, StringQueryFiled, BooleanQueryFiled, \
	IntegerPathFiled, StringPathFiled, BooleanPathFiled

__author__ = 'Alimazing'

banner_id_in_path = StringPathFiled(
	name='id', description="banner id", enum=['1'], default='1', required=True).data

get_banner = {
	"parameters": [banner_id_in_path],
	"responses": {
		"200": {
			"description": "轮播图",
			"examples": {}
		}
	}
}

# address
get_address = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "用户地址信息",
			"examples": {}
		}
	}
}

renew_address = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "更新成功: 用户地址",
			"examples": {}
		}
	}
}

# token
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
