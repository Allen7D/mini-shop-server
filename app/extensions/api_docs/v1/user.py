# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/25.
"""
from app.core.swagger_filed import BodyField

__author__ = 'Allen7D'

email = BodyField(name='email', type='string', description='邮箱', enum=['462870781@qq.com'])
nickname = BodyField(name='nickname', type='string', description='昵称', enum=['Allen7D'])
password = BodyField(name='password', type='string', description='密码', enum=['123456'])