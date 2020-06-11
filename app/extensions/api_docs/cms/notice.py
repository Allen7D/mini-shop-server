# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from app.core.swagger_filed import BodyField

__author__ = 'Allen7D'

type_in_body = BodyField(name='type', type='integer', description='通知(公告)类型', enum=[1, 2])
title_in_body = BodyField(name='title', type='string', description='通知(公告)标题', enum=['温馨提醒: 2018-08-01, 维护通知: 2018-07-15'])
content_in_body = BodyField(name='content', type='string', description='通知(公告)内容', enum=['新版本内容', '维护内容'])
status_in_body = BodyField(name='status', type='boolean', description='通知(公告)状态', enum=[True, False])
remark_in_body = BodyField(name='remark', type='string', description='通知(公告)备注', enum=['备注'])