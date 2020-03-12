# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.libs.error_code import BannerMissException
# BannerItem 默认用于 relationship
from app.models.banner_item import BannerItem
from app.models.base import Base

__author__ = 'Allen7D'

class Banner(Base):
	'''横幅广告总类'''
	__tablename__ = 'banner'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50), comment='Banner名称')
	description = Column(String(255), comment='描述')
	_items = relationship('BannerItem', backref='author', lazy='dynamic')


	def __repr__(self):
		return '<Banner(id={0}, nickname={1})>'.format(self.id, self.name)


	def keys(self):
		self.append('items')
		return self.fields

	@property
	def items(self):
		return self._items.all()

	@staticmethod
	def get_banner_by_id(id):
		return Banner.query.filter_by(id=id).first_or_404(e=BannerMissException)
