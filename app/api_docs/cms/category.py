# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/02/27.
"""
from app.libs.swagger_filed import IntegerQueryFiled

__author__ = 'Allen7D'

get_category_list = {
	"parameters": [
		IntegerQueryFiled(name='index', description="第几页", enum=[1, 2, 3, 4, 5], default=1).data,
		IntegerQueryFiled(name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10).data,
	],
	"responses": {
		"200": {
			"description": "产品分类(分页)",
			"examples": {}
		}
	}
}

update_category = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "用户类别信息",
			"examples": {
			}
		}
	}
}

delete_category = {
	"parameters": [],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "用户类别信息",
			"examples": {
			}
		}
	}
}