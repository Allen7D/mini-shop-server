# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.libs.error_code import CategoryException
from app.models.base import Base, db

__author__ = 'Alimazing'

class Category(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	topic_img_id = Column(Integer, ForeignKey('image.id'))
	image = relationship('Image', foreign_keys=[topic_img_id])

	def keys(self):
		self.hide('topic_img_id').append('image')
		return self.fields

	@staticmethod
	def get_all_categories():
		with db.auto_check_empty(CategoryException):
			return Category.query.all()
