# -*- coding: utf-8 -*-
"""
  Created on 2020/7/13.
"""
__author__ = 'Chai'

from app.core.swagger_filed import BodyField, IntegerQueryFiled, IntegerPathFiled

name_in_body = BodyField(name='name', type='string', description='元素名', enum=['删除按钮','新增按钮'])
element_sign_in_body = BodyField(name='element_sign', type='string', description='元素标记', enum=['add','delete'])
route_id_in_body = BodyField(name='route_id', type='integer', description='路由ID', enum=[1,2,3])

group_id_in_body = BodyField(name='group_id', type='integer', description='权限组ID', enum=[1,2,3])
element_id_in_body = BodyField(name='element_id', type='integer', description='元素ID',enum=[1,2,3])

group_id_in_query = IntegerQueryFiled(name='group_id', description='权限组ID')

element_id_in_path = IntegerPathFiled(name='element_id', description='元素ID')
