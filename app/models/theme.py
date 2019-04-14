# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String

from app.libs.error_code import ThemeException
from app.models.base import Base, db
from app.models.image import Image

__author__ = 'Allen7D'


def empty_interceptor(f):
	def decorator(id):
		try:
			f(id)
		except Exception:
			raise ThemeException()

	return decorator


class Theme(Base):
	__tablename__ = 'theme'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50), nullable=False)
	description = Column(String(255))
	topic_img_id = Column(Integer, nullable=False)  # theme后的图
	head_img_id = Column(Integer, nullable=False)  # 点击theme后的图

	def keys(self):
		self.hide('topic_img_id', 'head_img_id').append('topic_img_url', 'head_img_url')
		return self.fields

	@property
	def topic_img_url(self):
		return Image.get_img_by_id(self.topic_img_id).url

	@property
	def products(self):
		return self.product.all()

	@property
	def head_img_url(self):
		return Image.get_img_by_id(self.head_img_id).url

	@staticmethod
	def get_themes(ids):
		return [Theme.get_theme_by_id(id=id) for id in ids]

	@staticmethod
	def get_theme_by_id(id):
		with db.auto_check_empty(ThemeException):
			return Theme.query.filter_by(id=id).first_or_404()

	@staticmethod
	def get_theme_detail(id):
		# get theme detail with product
		with db.auto_check_empty(ThemeException):
			theme_detail = db.session.query(Theme).filter(Theme.id == id).first_or_404()
			return theme_detail.append('products')
