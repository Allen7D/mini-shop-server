# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/19.
"""
from sqlalchemy import Column, Integer, String

from app.core.db import BaseModel as Model

__author__ = 'Allen7D'

class Element(Model):
    __tablename__ = 'element'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='页面元素ID')
    code = Column(String(50), nullable=False, comment='页面元素编码')