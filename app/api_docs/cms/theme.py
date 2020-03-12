# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/12.
"""
from app.libs.swagger_filed import IntegerQueryFiled

__author__ = 'Allen7D'

page = IntegerQueryFiled(
    name='page', description="第几页", enum=[1, 2, 3, 4, 5], default=1)
size = IntegerQueryFiled(
    name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10)

