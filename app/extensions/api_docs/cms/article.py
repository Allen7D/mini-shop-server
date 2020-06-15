# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/26.
"""
from app.core.swagger_filed import IntegerQueryFiled, IntegerPathFiled, \
    StringPathFiled, StringQueryFiled, ArrayQueryField, \
    BodyField

__author__ = 'Allen7D'

type_in_query = IntegerQueryFiled(
    name='type', description="文章类型", enum=[0, 1, 2], default=1)