# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/8.
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String

from app.core.db import BaseModel as Base, db

__author__ = 'Allen7D'


class Log(Base):
    id = Column(Integer, primary_key=True)
    message = Column(String(450), comment='日志信息')
    user_id = Column(Integer, nullable=False, comment='用户id')
    user_name = Column(String(20), comment='用户当时的昵称')
    status_code = Column(Integer, comment='请求的http返回码')
    method = Column(String(20), comment='请求方法')
    path = Column(String(50), comment='请求路径')
    auth = Column(String(100), comment='访问哪个权限')
    create_time = Column('create_time', Integer, comment='创建时间')

    def __init__(self):
        # 时间戳
        self.create_time = int(round(datetime.now().timestamp()))

    @staticmethod
    def create_log(**kwargs):
        log = Log()
        for key in kwargs.keys():
            if hasattr(log, key):
                setattr(log, key, kwargs[key])
        db.session.add(log)
        if kwargs.get('commit') is True:
            db.session.commit()
        return log
