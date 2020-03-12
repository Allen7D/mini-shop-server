# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/26.
"""
from app.libs.swagger_filed import inject, IntegerPathFiled

__author__ = 'Allen7D'

banner_id = IntegerPathFiled(
	name='id', description="banner id", enum=[1, 2, 3, 100], required=True)