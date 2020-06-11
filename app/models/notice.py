# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, Text

from app.core.db import EntityModel as Model
from app.libs.enums import NoticeTypeEnum

__author__ = 'Allen7D'

class Notice(Model):
    '''通知(公告)'''
    __tablename__ = 'notice'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(SmallInteger, default=NoticeTypeEnum.NOTICE.value, comment='类型(1通知, 2公告)')
    title = Column(String(64), comment='标题')
    content = Column(Text, comment='内容')
    status = Column(Boolean, default=False, comment='状态(0正常, 1关闭)')
    remark = Column(Text, comment='备注')
    create_by = Column(String(32), default='', comment='创建者')
    update_by = Column(String(32), default='', comment='更新者')


