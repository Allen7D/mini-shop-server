# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/02/27.
"""
from app.libs.swagger_filed import StringPathFiled, IntegerQueryFiled, StringQueryFiled

__author__ = 'Allen7D'

product_id_in_path = StringPathFiled(
	name='id', description="product ID", enum=['1', '2', '3', '100'], default='1', required=True).data

category_id_in_query = StringQueryFiled(
	name='id', description="category ID", enum=['1', '2', '3', '100'], default='1', required=True).data

get_list_by_category = {
	"parameters": [
		category_id_in_query,
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
			"description": "产品信息列表",
			"examples": {
			}
		}
	}
}

update_product = {
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
