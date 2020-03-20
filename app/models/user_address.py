# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/25.
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base

__author__ = 'Allen7D'


class UserAddress(Base):
	'''配送信息'''
	__tablename__ = 'user_address'
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False, comment='外键: 下单的用户id')
	name = Column(String(30), nullable=False, comment='收货人姓名')
	mobile = Column(String(20), nullable=False, comment='手机')
	province = Column(String(20), comment='省份')
	city = Column(String(20), comment='城市')
	country = Column(String(20), comment='县区')
	detail = Column(String(100), comment='详细地址')

	def keys(self):
		self.hide('id', 'user_id')
		return self.fields
