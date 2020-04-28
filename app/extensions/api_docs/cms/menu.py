# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
"""
from app.core.swagger_filed import BodyField, IntegerQueryFiled

__author__ = 'Mohan'

group_id_in_body = BodyField(name='group_id', type='integer', description='权限组ID', enum=[1, 2, 3, 4])
group_id_in_query = IntegerQueryFiled(name='group_id', description='权限组ID', required=True, enum=[1, 2, 3, 4])
routes_in_body = BodyField(name='routes', type='array', description='路由节点ID列表', enum=[[1, 2, 3, 4], [1, 2, 3, 4]])
