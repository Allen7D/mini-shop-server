# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from sqlalchemy import Column, Integer, String, Boolean, Text

from app.core.db import BaseModel as Model

__author__ = 'Allen7D'

class Config(Model):
    '''参数配置'''
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), comment='名称')
    key = Column(String(64), comment='键名')
    value = Column(String(64), comment='键值')
    type = Column(Boolean, default=False, comment='是否系统内置(True是, False否)')
    remark = Column(Text, comment='备注')
