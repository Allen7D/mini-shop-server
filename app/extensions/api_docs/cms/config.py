# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from app.core.swagger_filed import IntegerPathFiled, IntegerQueryFiled, \
    StringPathFiled, StringQueryFiled, BodyField

__author__ = 'Allen7D'

key_in_path = StringPathFiled(
    name='key', description='参数key', enum=['sys.user.init_password', 'sys.layout.layout_theme'])
key_in_query = StringQueryFiled(
    name='key', description='参数key', enum=['sys.user.init_password', 'sys.layout.layout_theme'])

config_id_in_path = IntegerPathFiled(
    name='id', description="参数配置ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1)
config_id_in_query = IntegerQueryFiled(
    name='config_id', description="参数配置ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1)

name_in_body = BodyField(name='name', type='string', description='参数名称', enum=['用户管理-账号初始密码'])
key_in_body = BodyField(name='key', type='string', description='参数键名', enum=['sys.user.init_password'])
value_in_body = BodyField(name='value', type='string', description='参数键值', enum=['123456'])
type_in_body = BodyField(name='type', type='boolean', description='是否系统内置(True是, False否)', enum=[True, False])
remark_in_body = BodyField(name='remark', type='string', description='参数备注', enum=['备注'])