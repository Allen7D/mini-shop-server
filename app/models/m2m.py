# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, ForeignKey

from app.core.db import BaseModel as Model, db

__author__ = 'Allen7D'

theme_product = db.Table(
    'theme_product',
    Column('theme_id', Integer, ForeignKey('theme.id'), primary_key=True, comment='主题外键'),
    Column('product_id', Integer, ForeignKey('product.id'), primary_key=True, comment='商品外键')
)

# class Theme2Product(Model):
#     __tablename__ = 'theme_product'
#     theme_id = Column(Integer, ForeignKey('theme.id'), primary_key=True, comment='主题外键')
#     product_id = Column(Integer, ForeignKey('product.id'), primary_key=True, comment='商品外键')


class Product2Image(Model):
    __tablename__ = 'product_image'
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True, comment='外键, 商品id')
    img_id = Column(Integer, ForeignKey('image.id'), primary_key=True, comment='外键，关联图片表')
    order = Column(Integer, nullable=False, comment='图片排序序号')


class Order2Product(Model):
    __tablename__ = 'order_product'
    order_id = Column(Integer, primary_key=True, comment='联合主键，订单id')
    product_id = Column(Integer, primary_key=True, comment='联合主键，商品id')
    count = Column(Integer, nullable=False, comment='商品数量')

    def __init__(self, order_id=None, product_id=None, count=None):
        self.order_id = order_id
        self.product_id = product_id
        self.count = count


class Group2Element(Model):
    __tablename__ = 'group_2_element'
    group_id = Column(Integer,  ForeignKey('group.id'), primary_key=True)
    element_id = Column(Integer, ForeignKey('element.id'), primary_key=True)
