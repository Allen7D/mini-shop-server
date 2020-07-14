# -*- coding: utf-8 -*-
"""
  Created by Chai on 2020/7/13.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import BaseModel as Base

__author__ = 'Chai'


class Element(Base):
    '''页面元素'''
    __tablename__ = 'element'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), comment='名称')
    element_sign = Column(String(50), comment='元素标识')
    route_id = Column(Integer, ForeignKey('route.id'), primary_key=True)
    groups = relationship('Group', secondary='group_2_element', back_populates='elements')
