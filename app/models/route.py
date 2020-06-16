# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
"""
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.core.db import BaseModel as Base

__author__ = 'Mohan'


class Route(Base):
    __tablename__ = 'route'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='路由节点ID')
    parent_id = Column(Integer, nullable=False, comment='路由节点父级ID')
    order = Column(Integer, default=0, comment='节点排序')
    title = Column(String(20), nullable=False, comment='路由节点标签')
    name = Column(String(20), unique=True, comment='路由节点名')
    icon = Column(String(100), default='', comment='图标')
    path = Column(String(100), nullable=False, comment='路由节点相对路径')
    component = Column(String(100), comment='组件路径')
    hidden = Column(Boolean, default=False, nullable=False, comment='路由节点是否隐藏')
    group = relationship('Group', secondary='menu', back_populates='route')

    def __repr__(self):
        return "<Route(id=%s, parent_id=%s, title=%s, name=%s, group=%s)>" %\
               (self.id, self.parent_id, self.title, self.name, self.group)
