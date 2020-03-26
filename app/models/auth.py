# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
"""
from sqlalchemy import Column, Integer, String

from app.models.base import Base

__author__ = 'Allen7D'


class Auth(Base):
    __tablename__ = 'auth'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, nullable=False, comment='所属权限组id')
    name = Column(String(60), comment='权限字段')
    module = Column(String(50), comment='权限的模块')
