# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
"""
from app.libs.swagger_filed import BodyField

__author__ = 'Allen7D'

group_name_in_body = BodyField(name='name', type='string', description='权限组名称', enum=['活动策划员', '运维管理员'])
auth_ids_in_body = BodyField(name='auth_ids', type='array', description='权限ID列表',
                             enum=[[6, 7, 8],[12, 13, 14]])
info_in_body = BodyField(name='info', type='string', description='权限组描述', enum=['策划线上营销活动', '管理商品的上下架'])
