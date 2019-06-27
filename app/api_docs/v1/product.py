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
			"examples": {}
		}
	}
}

get_all_in_category = {
	"parameters": [category_id_in_query],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {}
		}
	}
}

get_one = {
	"parameters": [],
	"responses": {
		"200": {
			"description": "产品分类",
			"examples": {}
		}
	}
}

delete_one = {
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
