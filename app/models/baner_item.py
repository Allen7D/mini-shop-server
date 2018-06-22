# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/16.
"""
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.image import Image

__author__ = 'Alimazing'

class BannerItem(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	banner = relationship('Banner')
	banner_id = Column(Integer, ForeignKey('banner.id'))
	image = relationship('Image')
	img_id = Column(Integer, ForeignKey('image.id'))
	key_word = Column(String(100))
	type = Column(SmallInteger, default=1)

	def keys(self):
		self.hide('banner_id', 'img_id').append('img')
		return self.fields

	@property
	def img(self):
		return Image.get_img_by_id(id=self.img_id)
