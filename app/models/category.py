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
	'''商品类别'''
	__tablename__ = 'category'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50), comment='名称')
	description = Column(String(100), comment='描述')
	topic_img_id = Column(Integer, ForeignKey('image.id'), comment='外键，关联image表')
	image = relationship('Image', foreign_keys=[topic_img_id])

	def keys(self):
		self.hide('topic_img_id').append('image')
		return self.fields

	@staticmethod
	def get_all_categories():
		return Category.query.all_or_404(e=CategoryException, wrap='items')
