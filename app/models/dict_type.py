# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from sqlalchemy import Column, Integer, String, Boolean, Text

from app.core.db import BaseModel as Model

__author__ = 'Allen7D'


class DictType(Model):
    '''字典类型'''
    __tablename__ = 'dict_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), comment='字典名称')
    type = Column(String(64), comment='字典类型')
    status = Column(Boolean, default=False, comment='状态(True正常, False停用)')
    remark = Column(Text, comment='备注')
