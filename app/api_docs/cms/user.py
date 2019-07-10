# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/25.
"""
from app.libs.swagger_filed import StringPathFiled

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

super_get_user = {
	"parameters": [uid_in_path],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "管理员获取用户信息",
			"examples": {
			}
		}
	}
}

super_update_user = {
	"parameters": [uid_in_path],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "管理员修改用户信息",
			"examples": {
			}
		}
	}
}

super_delete_user = {
	"parameters": [uid_in_path],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "管理员注销用户",
			"examples": {
			}
		}
	}
}

