# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/10.
"""
from flask import current_app, request
from sqlalchemy import Column, Integer, SmallInteger, String

from app.core.db import EntityModel as Base, db
from app.libs.enums import UrlFromEnum

__author__ = 'Allen7D'


class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    uuid_name = Column(String(100), nullable=False, comment='唯一名称')
    name = Column(String(100), nullable=False, comment='原始名称')
    path = Column(String(500), nullable=False, comment='路径')
    extension = Column(String(50), nullable=False, comment='后缀')
    _from = Column('type', SmallInteger, default=1, comment='来源: 1 本地，2 公网')
    size = Column(Integer, comment='大小')
    md5 = Column(String(40), unique=True, comment='图片md5值，防止上传重复图片')

    def keys(self):
        self.hide('_from', 'path', 'md5').append('url')
        return self.fields

    @property
    def url(self):
        '''Nginx配置的静态资源地址'''
        if (UrlFromEnum(self._from) == UrlFromEnum.LOCAL):
            host_url = request.host_url
            host_url = host_url.split(',')[-1] if ',' in host_url else host_url
            host_url = host_url[:-1] # 当前host的路径 http://192.168.10.80:8010
            static_url_path = current_app.static_url_path[1:] + '/files' # static/files
            return '{0}/{1}/{2}'.format(host_url, static_url_path, self.path)
        return self.path
