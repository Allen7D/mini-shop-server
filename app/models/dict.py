# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from sqlalchemy import Column, Integer, String, Boolean, Text

from app.core.db import BaseModel as Model

__author__ = 'Allen7D'


class Dict(Model):
    '''字典数据'''
    __tablename__ = 'dict'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order = Column(Integer, nullable=False, comment='字典排序')
    label  = Column(String(64), comment='字典标签')
    value = Column(String(64), comment='字典键值')
    type = Column(String(64), comment='字典类型')
    css_class = Column(String(64), comment='样式属性（其他样式扩展）')
    list_class = Column(String(64), comment='表格回显样式(默认default, 主要primary, 成功success, 信息info, 警告warning, 危险danger)')
    is_default = Column(Boolean, default=False, comment='是否默认(True是, False否)')
    status = Column(Boolean, default=False, comment='状态(True正常, False停用)')
    remark = Column(Text, comment='备注')

