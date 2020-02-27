# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import StringQueryFiled, StringPathFiled

__author__ = 'Allen7D'

category_id_in_query = StringQueryFiled(
	name='id', description="category ID", enum=['1', '2', '3', '100'], default='1', required=True).data

product_id_in_path = StringPathFiled(
	name='id', description="product ID", enum=['1', '2', '3', '100'], default='1', required=True).data

get_recent = {
	"parameters": [],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {
				"data": {
					"items": [
						{
							"category_id": 3,
							"id": 33,
							"img_urls": [],
							"main_img_url": "0.0.0.0:8010/static/images/product-vg@5.png",
							"name": "青椒 半斤",
							"price": 0.01,
							"stock": 999,
							"summary": None
						}
					]
				},
				"error_code": 0,
				"msg": "成功"
			}
		}
	}
}

get_all_by_category = {
	"parameters": [category_id_in_query],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {}
		}
	}
}

get_product = {
	"parameters": [product_id_in_path],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {
				"data":{
					"id": 1,
					"img_urls": [],
					"main_img_url": "0.0.0.0:8010/static/images/product-vg@1.png",
					"name": "芹菜 半斤",
					"price": 0.01,
					"stock": 998,
					"summary": None
				},
				"error_code": 0,
				"msg": "成功"
			}
		}
	}
}

delete_product = {
	"parameters": [product_id_in_path],
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
