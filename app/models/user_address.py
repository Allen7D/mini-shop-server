# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/25.
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base

__author__ = 'Allen7D'


class UserAddress(Base):
	__tablename__ = 'user_address'
	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
	name = Column(String(30), nullable=False)
	mobile = Column(String(20), nullable=False)
	country = Column(String(20))
	province = Column(String(20))
	city = Column(String(20))
	detail = Column(String(100))  # 具体体制

	def keys(self):
		self.hide('id', 'user_id')
		return self.fields
