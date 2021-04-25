# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/21.
"""
from datetime import date, datetime
from flask.json import JSONEncoder as _JSONEncoder

from app.core.error import ServerError

__author__ = 'Allen7D'


class JSONEncoder(_JSONEncoder):
    def default(self, obj):
        # 如果obj是数据库查询获得的实例对象
        if hasattr(obj, 'keys') and hasattr(obj, '__getitem__'):
            obj.lock_fileds()  # 锁定ctrl层的hide过和append过的字段
            return dict(obj)
        # 如果o是时间戳
        # datetime.now() ==> datetime.datetime(2020, 4, 8, 9, 4, 57, 26881)
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        # date.today() ==> datetime.date(2020, 4, 8)
        if isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        raise ServerError()
