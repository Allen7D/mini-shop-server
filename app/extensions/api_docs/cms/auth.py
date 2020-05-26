# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
"""
from app.core.swagger_filed import IntegerQueryFiled, IntegerPathFiled
__author__ = 'Allen7D'

# 权限
group_id_in_path = IntegerPathFiled(
    name='group_id', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20])
group_id_in_query = IntegerQueryFiled(
    name='group_id', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20])
