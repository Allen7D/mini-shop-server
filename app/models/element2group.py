# -*- coding: utf-8 -*-

from app.core.db import BaseModel as Base
from sqlalchemy import Column, Integer, ForeignKey


class Element2Group(Base):
    __tablename__ = 'element_group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    element_id = Column(Integer, ForeignKey('element.id'), primary_key=True)
    group_id = Column(Integer,  ForeignKey('group.id'), primary_key=True)