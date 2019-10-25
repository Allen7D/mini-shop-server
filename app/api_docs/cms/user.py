# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/25.
"""
from app.libs.swagger_filed import IntegerQueryFiled, IntegerPathFiled

__author__ = 'Allen7D'

uid_in_path = IntegerPathFiled(name='uid',
							   description="用户ID",
							   enum=[1, 2, 3, 4, 5, 100, 1000000],
							   default=1,
							   required=True).data

get_user_list = {
	"parameters": [
		IntegerQueryFiled(name='index', description="第几页", enum=[1, 2, 3, 4, 5], default=1).data,
		IntegerQueryFiled(name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10).data,
	],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "管理员获取用户信息列表",
			"examples": {
			}
		}
	}
}

get_user = {
	"parameters": [uid_in_path],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "获取用户信息",
			"examples": {
			}
		}
	}
}

update_user = {
	"parameters": [uid_in_path],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "修改用户信息",
			"examples": {
			}
		}
	}
}

delete_user = {
	"parameters": [uid_in_path],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "注销用户",
			"examples": {
			}
		}
	}
}
