# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/16.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.libs.error_code import BannerMissException
from app.models.baner_item import BannerItem
from app.models.base import Base, db

__author__ = 'Alimazing'

class Banner(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	description = Column(String(255))
	_items = relationship('BannerItem', backref='author', lazy='dynamic')

	def keys(self):
		self.append('items')
		return self.fields

	@property
	def items(self):
		return self._items.all()

	@staticmethod
	def get_banner_by_id(id):
		with db.auto_check_empty(BannerMissException):
			# banner = Banner.query.filter_by(id=id).first_or_404()
			# items = banner.items.all()
			return Banner.query.filter_by(id=id).first_or_404()
