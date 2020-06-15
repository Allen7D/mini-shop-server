# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from app.core.swagger_filed import StringPathFiled, StringQueryFiled, BodyField

__author__ = 'Allen7D'

type_in_path = StringPathFiled(
    name='type', description='字典类型', enum=['sys_user_sex', 'sys_show_hide'])
type_in_query = StringQueryFiled(
    name='type', description='字典类型', enum=['sys_user_sex', 'sys_show_hide'])

dict_id_in_path = StringPathFiled(
    name='id', description='字典数据ID', enum=[0, 1, 2, 3, 4, 5, 10, 100], default=1)
dict_id_in_query = StringQueryFiled(
    name='dict_id', description='字典数据ID', enum=[0, 1, 2, 3, 4, 5, 10, 100], default=1)

order = BodyField(name='order', type='integer', description='字典排序', enum=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
label = BodyField(name='label', type='string', description='字典标签', enum=['男or女)'])
value = BodyField(name='value', type='string', description='字典键值', enum=['0or1'])
type = BodyField(name='type', type='string', description='字典类型', enum=['sys_user_sex', 'sys_show_hide'])
css_class = BodyField(name='css_class', type='string', description='样式属性（其他样式扩展）', enum=[''])
list_class = BodyField(name='list_class', type='string',
                       description='表格回显样式(默认default, 主要primary, 成功success, 信息info, 警告warning, 危险danger)',
                       enum=['default', 'primary', 'success', 'info', 'warning', 'danger'])
is_default = BodyField(name='is_default', type='boolean', description='是否默认(True是, False否)', enum=[True, False], default=False)
status = BodyField(name='status', type='boolean', description='状态(True正常, False停用)', enum=[True, False], default=True)
remark = BodyField(name='remark', type='string', description='备注', enum=[''])
