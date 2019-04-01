# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/12/4.
"""
from app.libs.swagger_filed import IntegerPathFiled

__author__ = 'Alimazing'

theme_id_in_path = IntegerPathFiled(
	name='id', description="theme id", enum=[1, 2, 3], default=1, required=True).data

get_simple_list = {
	"parameters": [
		{
			'name': 'ids',
			"in": "query",
			"required": True,
			"type": "array",
			"items": {
				"type": "integer",
				"enum": [1, 2, 3, 4, 5],
				"default": 1
			}

		}
	],
	"responses": {
		"200": {
			"description": "获取成功",
			"examples": {
				"data": [
					{
						"description": "美味水果世界",
						"head_img_url": "0.0.0.0:8080/static/images/1@theme-head.png",
						"id": 1,
						"name": "专题栏位一",
						"topic_img_url": "0.0.0.0:8080/static/images/1@theme.png"
					}
				],
				"error_code": 0,
				"msg": "成功"
			}
		}
	}
}

get_complex_one = {
	"parameters": [theme_id_in_path],
	"responses": {
		"200": {
			"description": "获取成功",
			"examples": {
				"data": {
					"description": "美味水果世界",
					"head_img_url": "0.0.0.0:8080/static/images/1@theme-head.png",
					"id": 1,
					"name": "专题栏位一",
					"products": [
						{
							"category_id": 2,
							"id": 2,
							"img_urls": [],
							"main_img_url": "0.0.0.0:8080/static/images/product-dryfruit@1.png",
							"name": "梨花带雨 3个",
							"price": 0.01,
							"stock": 984,
							"summary": None
						}
					],
					"topic_img_url": "0.0.0.0:8080/static/images/1@theme.png"
				},
				"error_code": 0,
				"msg": "成功"
			}
		}
	}
}
