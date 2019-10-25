# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.libs.error_code import CategoryException
from app.models.base import Base

__author__ = 'Allen7D'

class Category(Base):
	__tablename__ = 'category'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	topic_img_id = Column(Integer, ForeignKey('image.id'))
	image = relationship('Image', foreign_keys=[topic_img_id])

	def keys(self):
		self.hide('topic_img_id').append('image')
		return self.fields

	@staticmethod
	def get_all_categories():
		return Category.query.all_or_404(e=CategoryException)
