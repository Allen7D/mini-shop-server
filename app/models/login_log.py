# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/15.
  登录日志
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean

from app.core.db import BaseModel as Base

__author__ = 'Allen7D'


class LoginLog(Base):
    __tablename__ = 'login_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, comment='用户id')
    user_name = Column(String(50), comment='用户当时的昵称')
    ip_addr = Column(String(50), comment='登录IP地址')
    location = Column(String(255), comment='登录地点')
    browser = Column(String(50), comment='浏览器类型')
    os = Column(String(50), comment='操作系统')
    message = Column(String(255), comment='提示消息')
    status = Column(Boolean, default=True, comment='登录状态(True成功, False失败)')
    create_time = Column('create_time', Integer, comment='访问时间')

    def __init__(self):
        # 时间戳
        self.create_time = int(round(datetime.now().timestamp()))
