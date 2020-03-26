# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
"""
from sqlalchemy import Column, Integer, String

from app.libs.core import get_ep_id
from app.models.base import Base, db
from app.models.auth import Auth as AuthModel

__author__ = 'Allen7D'


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), comment='权限组名称')
    info = Column(String(255), comment='权限组描述')

    @property
    def auth_list(self):
        auth_list = db.session.query(AuthModel.name, AuthModel.module) \
            .filter_by(group_id=self.id).all()
        auth_list = [{'id': get_ep_id(auth[0]),'name': auth[0], 'module': auth[1]} for auth in auth_list]
        return auth_list
