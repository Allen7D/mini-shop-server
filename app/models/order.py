# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/7/6.
"""
from sqlalchemy import Column, Integer, SmallInteger, String, Float, Text

from app.models.base import Base

__author__ = 'Allen7D'

class Order(Base):
	id = Column(Integer, primary_key=True, autoincrement=True)
	order_no = Column(String(20), unique=True)
	user_id = Column(Integer)
	total_price = Column(Float)
	order_status = Column(SmallInteger, default=1)
	snap_img = Column(String(255))
	snap_name = Column(String(80))
	total_count = Column(Integer)
	snap_items = Column(Text)
	snap_address = Column(String(500))
	prepay_id = Column(String(100), unique=True)

	def keys(self):
		self.hide('user_id').append('create_time')
		return self.fields

	@classmethod
	def get_summary_by_user(cls, uid, page=1, size=10):
		paginator = cls.query.filter_by(
			user_id=uid
		).order_by(cls.create_time.desc()).paginate(
			page=page,
			per_page=size,
			error_out=True
		)
		paginator.hide('snap_items', 'snap_address', 'prepay_id')
		return {
			'total': paginator.total,
			'current_page': paginator.page,
			'data': paginator.items
		}
