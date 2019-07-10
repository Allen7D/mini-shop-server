# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/25.
"""
from app.libs.swagger_filed import IntegerQueryFiled, StringQueryFiled, IntegerPathFiled, StringPathFiled

__author__ = 'Allen7D'

uid_in_path = StringPathFiled(name='uid',
							  description="用户ID",
							  enum=['0000aef0774f11e8ba9500163e0ce7e6',
									'00171b62791711e889ad00163e0ce7e6',
									'0017be56959511e8b34700163e0ce7e6',
									'001aa40c61c111e8a8a600163e0ce7e6',
									'001ea0984fa111e8a3d400163e0ce7e6'],
							  default='0000aef0774f11e8ba9500163e0ce7e6',
							  required=True).data

get_user = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "用户获取自身信息",
			"examples": {
			}
		}
	}
}

update_user = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "用户修改信息",
			"examples": {
			}
		}
	}
}

delete_user = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "用户注销",
			"examples": {
			}
		}
	}
}
