# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import IntegerPathFiled, IntegerQueryFiled

__author__ = 'Allen7D'

id_in_path = IntegerPathFiled(
	name='id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], default=1, required=True).data


'''
"type": "array" 时
	- 可以使用 items

"type": 'object'时
	-可以使用 properties
'''
place_order = {
	"parameters": [
		{
			"name": "body",
			"in": "body",
			"description": "订单中商品信息列表(商品ID&数量)",
			"require": "true",
			"schema": {
				"id": "Order",  # 在Swagger中，可以显示Model; 全局唯一，否则会覆盖同ID处
				"required": ["products"],
				"properties": {
					"products": {
						"type": "array",
						"description": "商品列表",
						"items": {
							"type": 'object',
							"properties": {
								'product_id': {
									'type': 'integer',  # 不写 enum，则默认为数字0
									"description": "商品ID",
									"enum": [1, 2, 3, 4, 5],  # 在Swagger中，默认显示第0个
									'default': 1  # 必须结合 enum 使用，否则无效; 可以自定义超出enum设置的范围
								},
								'count': {
									'type': 'integer',
									"description": "商品数量",
									"enum": [10, 15, 20, 25, 30],
									'default': 10
								}
							}
						}
					}
				}
			}
		}
	],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "提交成功",
			"examples": {
				"data": {
					"create_time": 1554227821,
					"order_id": 1,
					"order_no": "B0X431741575422719",
					"pass": True
				},
				"error_code": 0,
				"msg": "成功"
			}
		}
	}
}

get_detail = {
	"parameters": [
		id_in_path
	],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "订单详情",
			"examples": {}
		}
	}
}

get_summary_by_user = {
	"parameters": [
		IntegerQueryFiled(name='page', description="第几页", enum=[1, 2, 3, 4, 5], default=1).data,
		IntegerQueryFiled(name='size', description="每页数量", enum=[5, 10, 20, 30, 40, 50, 100], default=10).data
	],
	"security": [
		{
			"basicAuth": []
		}
	],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {}
		}
	}
}

get_summary = {
	"parameters": [],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {}
		}
	}
}

delivery = {
	"parameters": [],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {}
		}
	}
}
