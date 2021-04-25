# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/27.
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.db import BaseModel as Model
__author__ = 'Allen7D'

class Product2Property(Model):
    __tablename__ = 'product_property'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False, comment='外键, 商品id')
    name = Column(String(30), comment='详情属性名称')
    detail = Column(String(255), nullable=False, comment='详情属性')

    def keys(self):
        self.hide('id')
        return self.fields

