# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from app.core.swagger_filed import StringPathFiled, StringQueryFiled


__author__ = 'Allen7D'

type_in_path = StringPathFiled(
    name='type', description='字典类型', enum=['sys_user_sex', 'sys_show_hide'])
type_in_query = StringQueryFiled(
    name='type', description='字典类型', enum=['sys_user_sex', 'sys_show_hide'])
