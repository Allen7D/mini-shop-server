# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, Float, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.models.m2m import Product2Image
from app.core.db import EntityModel as Base, db

__author__ = 'Allen7D'


class Product(Base):
    '''商品'''
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, comment='所属类别组id')
    name = Column(String(50), comment='商品名称')
    price = Column(Float, comment='价格(单位:分)')
    stock = Column(Integer, comment='库存量')
    _main_img_url = Column('main_img_url', String(255), comment='主图id，这是一个反范式设计，有一定的冗余')
    _from = Column('from', SmallInteger, default=1, comment='主图来源:1 本地, 2公网')
    _images = relationship('Image', secondary='product_image', order_by=Product2Image.order.asc(), backref=backref('product', lazy='dynamic'))
    summary = Column(String(50), comment='摘要')


    def keys(self):
        self.hide('_main_img_url', '_from').append('main_image', 'images')
        return self.fields

    @property
    def main_image(self):
        return self.get_url(self._main_img_url)

    @property
    def images(self):
        _images = self._images
        return [item.url for item in _images]
