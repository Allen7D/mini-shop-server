# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/10.
"""
from .admin import Extension

__author__ = 'Allen7D'


def apply_orm_admin(app):
    orm_admin = Extension(name='商城后台', template_mode='bootstrap3')
    orm_admin.init_app(app)
