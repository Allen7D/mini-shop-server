# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/6.
"""
from ..base import ModelView

__author__ = 'Allen7D'


class OrderView(ModelView):
    column_searchable_list = ['user_id']
