# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import inject, StringQueryFiled, StringPathFiled

__author__ = 'Allen7D'

category_id = StringQueryFiled(
    name='id', description="category ID", enum=['1', '2', '3', '100'], default='1', required=True)
product_id = StringPathFiled(
    name='id', description="product ID", enum=['1', '2', '3', '100'], default='1', required=True)