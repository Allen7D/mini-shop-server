# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base
from app.models.image import Image

__author__ = 'Allen7D'


class Theme2Product(Base):
	__tablename__ = 'theme_product'
	theme_id = Column(Integer, ForeignKey('theme.id'), primary_key=True, comment='主题外键')
	product_id = Column(Integer, ForeignKey('product.id'), primary_key=True, comment='商品外键')


class Product2Image(Base):
	__tablename__ = 'product_image'
	id = Column(Integer, primary_key=True, autoincrement=True)
	img_id = Column(Integer, ForeignKey('image.id'), nullable=False, comment='外键，关联图片表')
	order = Column(Integer, nullable=False, comment='图片排序序号')
	product_id = Column(Integer, ForeignKey('product.id'), nullable=False, comment='外键, 商品id')

	def keys(self):
		self.hide('id', 'img_id', 'product_id', 'order').append('img_url')
		return self.fields

	@property
	def img_url(self):
		return Image.get_img_by_id(id=self.img_id).url


class Product2Property(Base):
	__tablename__ = 'product_property'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(30), comment='详情属性名称')
	detail = Column(String(255), nullable=False, comment='详情属性')
	product_id = Column(Integer, ForeignKey('product.id'), nullable=False, comment='外键, 商品id')


class Order2Product(Base):
	__tablename__ = 'order_product'
	order_id = Column(Integer, primary_key=True, comment='联合主键，订单id')
	product_id = Column(Integer, primary_key=True, comment='联合主键，商品id')
	count = Column(Integer, nullable=False, comment='商品数量')

	def __init__(self, order_id=None, product_id=None, count=None):
		self.order_id = order_id
		self.product_id = product_id
		self.count = count
		super(Order2Product, self).__init__()
