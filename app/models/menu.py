# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
"""
from sqlalchemy import Column, Integer, ForeignKey

from app.core.db import BaseModel as Model

__author__ = 'Mohan'


class Menu(Model):
    __tablename__ = 'menu'
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True, comment='外键 权限组ID')
    route_id = Column(Integer, ForeignKey('route.id'), primary_key=True, comment='外键 路由节点ID')
