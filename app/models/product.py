# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, Float, String, SmallInteger
from sqlalchemy import desc, asc
from sqlalchemy.orm import relationship, backref

from app.libs.error_code import ProductException
from app.libs.utils import jsonify
from app.models.m2m import Product2Image
from app.models.base import Base, db

__author__ = 'Allen7D'

class Product(Base):
	'''商品'''
	__tablename__ = 'product'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50), comment='商品名称')
	price = Column(Float, comment='价格(单位:分)')
	stock = Column(Integer, comment='库存量')
	category_id = Column(Integer, comment='所属类别组id')
	_main_img_url = Column('main_img_url', String(255), comment='主图id，这是一个反范式设计，有一定的冗余')
	_from = Column('from', SmallInteger, default=1, comment='图片来源:1 本地, 2公网')
	summary = Column(String(50), comment='摘要')
	img_id = Column(Integer, comment='外键，关联image表')
	theme = relationship('Theme', secondary='theme_product', backref=backref('product', lazy='dynamic'))

	def keys(self):
		self.hide('_main_img_url', '_from', 'img_id').append('main_img_url', 'img_urls')
		return self.fields

	@property
	def main_img_url(self):
		return self.get_url(self._main_img_url)

	@property
	def img_urls(self):
		try:
			img_urls = Product2Image.query.filter_by(product_id=self.id).order_by(asc(Product2Image.order)).all()
		except Exception:
			return []
		return list(map(lambda x: x['img_url'], jsonify(img_urls)))

	@staticmethod
	def get_most_recent(count):
		return Product.query.order_by(desc(Product.create_time)).limit(count).all_or_404(e=ProductException, wrap='items')

	@staticmethod
	def get_product_by_category(id):
		return Product.query.filter_by(category_id=id).all_or_404(e=ProductException, wrap='items')

	@staticmethod
	def get_product_detail(id):
		return Product.query.filter_by(id=id)\
			.first_or_404(e=ProductException).hide('category_id')

	@staticmethod
	def delete_by_id(id):
		product = Product.query.filter_by(id=id).first_or_404()
		product.delete()
