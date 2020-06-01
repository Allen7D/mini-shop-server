# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base, db
from app.models.image import Image

__author__ = 'Allen7D'


class Theme(Base):
    '''商城活动主题'''
    __tablename__ = 'theme'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment='专题名称')
    description = Column(String(255), comment='专题描述')
    topic_img_id = Column(Integer, nullable=False, comment='外键: 主题图')  # theme后的图
    head_img_id = Column(Integer, nullable=False, comment='头图(专题列表页)')  # 点击theme后的图
    products = relationship('Product', secondary='theme_product', backref=backref('theme', lazy='dynamic'))

    def keys(self):
        self.hide('topic_img_id', 'head_img_id').append('topic_img_url', 'head_img_url')
        return self.fields

    @property
    def topic_img_url(self):
        image = Image.get(id=self.topic_img_id)
        return image.url if image else ''

    @property
    def head_img_url(self):
        image = Image.get(id=self.head_img_id)
        return image.url if image else ''
