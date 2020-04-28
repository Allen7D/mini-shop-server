# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import BaseModel as Base
from app.models.route import Route
from app.models.group import Group

__author__ = 'Mohan'


class Menu(Base):
    __tablename__ = 'menu'
    group_id = Column(Integer, ForeignKey('group.id'), primary_key=True, comment='外键 权限组ID')
    route_id = Column(Integer, ForeignKey('route.id'), primary_key=True, comment='外键 路由节点ID')

    # def __repr__(self):
    #     return "<Menus(group_id=%s, route_id=%s, title=%s, name=%s)>" %\
    #            (self.group_id, self.route_id, self.title, self.name)

    def keys(self):
        self.hide('_route', '_group')
        self.append('create_time', 'update_time')
        return self.fields
