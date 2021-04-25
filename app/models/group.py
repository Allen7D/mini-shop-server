# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.auth import get_ep_id
from app.core.db import BaseModel as Base, db
from app.models.auth import Auth

__author__ = 'Allen7D'


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True, comment='权限组名称')
    info = Column(String(255), comment='权限组描述')
    route = relationship('Route', secondary='menu', back_populates='group')
    elements = relationship('Element', secondary='group_2_element', back_populates='groups')

    @property
    def auth_list(self):
        auth_list = db.session.query(Auth.name, Auth.module) \
            .filter_by(group_id=self.id).all()
        auth_list = [{'id': get_ep_id(auth[0]), 'name': auth[0], 'module': auth[1]} for auth in auth_list]
        return auth_list