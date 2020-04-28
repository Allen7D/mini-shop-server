# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
"""
from app.core.swagger_filed import BodyField, IntegerPathFiled

__author__ = 'Mohan'

id_in_body = BodyField(name='id', type='integer', description='路由节点ID', enum=[1, 2, 3, 4])
id_in_path = IntegerPathFiled(name='id', description='路由节点ID', enum=[1, 2, 3, 4, 23, 24, 25])
parent_id_in_body = BodyField(name='parent_id', type='integer', description='路由节点父级ID', enum=[0, 0, 0, 0])
children_in_body = BodyField(name='children', type='array', description='子路由节点', enum=[[2, 3, 4]])
title_in_body = BodyField(name='title', type='string', description='路由标题', enum=['菜小单', '菜小双', '菜小三'])
name_in_body = BodyField(name='name', type='string', description='路由名', enum=['menu_1', 'menu_2', 'menu_3'])
icon_in_body = BodyField(name='icon', type='string', description='图标url', enum=['fa-bars1', 'fa-bars2', 'fa-bars3'])
path_in_body = BodyField(name='path', type='string', description='路由节点相对路径', enum=['/admin/menu1', '/admin/menu2', '/admin/menu3'])
component_in_body = BodyField(name='component', type='string', description='路由节点对应组件', enum=['vue-component1', 'vue-component2', 'vue-component3'])
hidden_in_body = BodyField(name='hidden', type='boolean', description='路由节点渲染时是否隐藏', enum=[False, False, False])
nodes_in_body = BodyField(name='route_tree', type='array', description='修改后完整路由结构', enum=[{'id': 1, 'children': [{'id': 2, 'children': [{'id': 5}, {'id': 6}]}, {'id': 3}]}])
