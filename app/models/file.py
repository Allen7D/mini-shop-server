# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/10.
"""
from sqlalchemy import Column, Integer, SmallInteger, String

from app.core.db import EntityModel as Base, db

__author__ = 'Allen7D'


class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    path = Column(String(500), nullable=False, comment='路径')
    _type = Column('type', SmallInteger, default=1, comment='1 local，其他表示其他地方')
    name = Column(String(100), nullable=False, comment='名称')
    extension = Column(String(50), nullable=False, comment='后缀')
    size = Column(Integer, comment='大小')
    md5 = Column(String(40), unique=True, comment='图片md5值，防止上传重复图片')

    @staticmethod
    def create_file(**kwargs):
        file = File()
        for key in kwargs.keys():
            if hasattr(file, key):
                setattr(file, key, kwargs[key])
        db.session.add(file)
        if kwargs.get('commit') is True:
            db.session.commit()
        return file
