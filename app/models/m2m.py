# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

__author__ = 'Alimazing'

class Theme2Product(Base):
	__tablename__ = 'theme_product'
	theme_id = Column(Integer, ForeignKey('theme.id'), primary_key = True)
	product_id = Column(Integer, ForeignKey('product.id'), primary_key = True)
