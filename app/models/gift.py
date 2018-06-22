# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/14.
"""

from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base

__author__ = 'Alimazing'


class Gift(Base):
	id = Column(Integer, primary_key=True)
	user = relationship('User')
	uid = Column(Integer, ForeignKey('user.id'))
	isbn = Column(String(15), nullable=False)
	launched = Column(Boolean, default=False) # 是否被赠送
