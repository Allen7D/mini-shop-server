# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base
__author__ = 'Allen7D'

class Image(Base):
	'''图片'''
	__tablename__ = 'image'
	id = Column(Integer, primary_key=True, autoincrement=True)
	_url = Column('url', String(255), comment='图片路径')
	_from = Column('from', SmallInteger, default=1, comment='图片来源: 1 本地，2 公网')

	def __repr__(self):
		return '<Image(id={0}, url={1})>'.format(self.id, self.url)

	def keys(self):
		self.hide('id', '_url','_from').append('url')
		return self.fields

	@property
	def url(self):
		return self.get_url(self._url)

	@staticmethod
	def get_img_by_id(id):
		return Image.query.filter_by(id=id).first_or_404()
