# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.db import EntityModel as Base


class Element(Base):
    '''页面元素'''
    __tablename__ = 'element'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), comment='名称')
    element_sign = Column(String(50), comment='元素标识')
    route_id = Column(Integer, ForeignKey('route.id'), primary_key=True)