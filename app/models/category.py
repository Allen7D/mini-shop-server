# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import EntityModel as Base

__author__ = 'Allen7D'


class Category(Base):
    '''商品类别'''
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), comment='名称')
    description = Column(String(100), comment='描述')
    topic_img_id = Column(Integer, ForeignKey('image.id'), comment='外键，关联image表')
    _image = relationship('Image', foreign_keys=[topic_img_id])

    def keys(self):
        self.hide('topic_img_id').append('image')
        return self.fields

    @property
    def image(self):
        return self._image.url
