# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/15.
"""
from app.core.swagger_filed import StringPathFiled, StringQueryFiled, BodyField

__author__ = 'Allen7D'

type_id_in_path = StringPathFiled(
    name='id', description='字典类型ID', enum=[0, 1, 2, 3, 4, 5, 10, 100], default=1)
type_id_in_query = StringQueryFiled(
    name='type_id', description='字典类型ID', enum=[0, 1, 2, 3, 4, 5, 10, 100], default=1)

name = BodyField(name='value', type='string', description='字典名称', enum=['用户性别', '菜单状态'])
type = BodyField(name='type', type='string', description='字典类型', enum=['sys_user_sex', 'sys_show_hide'])
status = BodyField(name='status', type='boolean', description='状态(True正常, False停用)', enum=[True, False], default=True)
remark = BodyField(name='remark', type='string', description='备注', enum=[''])
