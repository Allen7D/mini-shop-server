# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship, backref

from app.core.db import EntityModel as Base
from app.models.image import Image

__author__ = 'Allen7D'


class BannerItem(Base):
    '''横幅广告'''
    __tablename__ = 'banner_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    banner_id = Column(Integer, ForeignKey('banner.id'), comment='外键，所属Banner组id')
    img_id = Column(Integer, ForeignKey('image.id'), comment='外键，关联image表')
    _image = relationship('Image', backref=backref('banner_item', uselist=False))
    key_word = Column(String(100), comment='执行关键字，根据不同的type含义不同')
    type = Column(SmallInteger, default=1,
                  comment='跳转类型，可能导向商品，可能导向专题，可能导向其他。0，无导向；1：导向商品;2:导向专题')

    def keys(self):
        self.hide('banner_id', 'img_id').append('image')
        return self.fields

    @property
    def image(self):
        return self._image.url
