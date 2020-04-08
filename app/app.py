# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/13.
"""
from datetime import date, datetime
from flask import Flask as _Flask, _request_ctx_stack
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError

__author__ = 'Allen7D'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        # 如果o是数据库查询获得的实例对象
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        # 如果o是时间戳
        # datetime.now() ==> datetime.datetime(2020, 4, 8, 9, 4, 57, 26881)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%SZ')
        # date.today() ==> datetime.date(2020, 4, 8)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
