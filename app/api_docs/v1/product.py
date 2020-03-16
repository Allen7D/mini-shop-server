# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/4.
"""
from app.libs.swagger_filed import IntegerQueryFiled

__author__ = 'Allen7D'

count = IntegerQueryFiled(
    name='count', description='商品数', enum=[1, 2, 3, 4, 5, 10, 15], default=1
)
