# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/13.
"""
from app.libs.swagger_filed import IntegerQueryFiled, IntegerPathFiled

__author__ = 'Allen7D'

uid_in_path = IntegerPathFiled(
    name='uid', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)
uid_in_query = IntegerQueryFiled(
    name='uid', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)

product_id_in_path = IntegerPathFiled(
    name='id', description="商品 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)
product_id_in_query = IntegerQueryFiled(
    name='id', description="商品 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)

category_id_in_path = IntegerPathFiled(
    name='id', description="类别 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)
category_id_in_query = IntegerQueryFiled(
    name='id', description="类别 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)

theme_id_in_path = IntegerPathFiled(
    name='id', description="主题ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)
theme_id_in_query = IntegerQueryFiled(
    name='id', description="主题ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)

banner_id_in_path = IntegerPathFiled(
	name='id', description="轮播图ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)
banner_id_in_query = IntegerQueryFiled(
	name='id', description="轮播图ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)

order_id_in_path = IntegerPathFiled(
    name='id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)
order_id_in_query = IntegerQueryFiled(
    name='id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20], required=True)

page = IntegerQueryFiled(name='page', description="第几页", enum=[1, 2, 3, 4, 5], default=1)
size = IntegerQueryFiled(name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10)