# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/11/26.
"""
__author__ = 'Alimazing'

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
