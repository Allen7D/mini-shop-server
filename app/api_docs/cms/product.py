# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/02/27.
"""
from app.libs.swagger_filed import inject, StringPathFiled, IntegerQueryFiled, StringQueryFiled

__author__ = 'Allen7D'

product_id = StringPathFiled(
	name='id', description="product ID", enum=['1', '2', '3', '100'], required=True)

category_id = StringQueryFiled(
	name='id', description="category ID", enum=['1', '2', '3', '100'], required=True)

page = IntegerQueryFiled(
	name='page', description="第几页", enum=[1, 2, 3, 4, 5], default=1)
size = IntegerQueryFiled(
	name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10)

@inject(category_id, page, size)
def get_list_by_category(): pass

@inject(product_id)
def update_product(): pass

@inject(product_id)
def delete_product(): pass