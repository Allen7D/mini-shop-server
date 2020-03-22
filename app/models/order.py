# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/7/6.
"""
from sqlalchemy import Column, Integer, SmallInteger, String, Float, Text

from app.models.base import Base

__author__ = 'Allen7D'


class Order(Base):
	'''用户订单'''
	__tablename__ = 'order'
	id = Column(Integer, primary_key=True, autoincrement=True)
	order_no = Column(String(20), unique=True, comment='订单号')
	user_id = Column(Integer, comment='外键，用户id，注意并不是openid') # 下单用户ID
	order_status = Column(SmallInteger, default=1, comment='订单状态 1:未支付 2:已支付 3:已发货 4:已支付，但库存不足 ')
	snap_img = Column(String(255), comment='订单快照·封面')
	snap_name = Column(String(80), comment='订单快照·别名')
	snap_items = Column(Text, comment='订单快照·详情')
	snap_address = Column(String(500), comment='订单快照·地址')
	total_count = Column(Integer, comment='订单总量')
	total_price = Column(Float, comment='订单总价')
	prepay_id = Column(String(100), unique=True, comment='预支付id')

	def keys(self):
		self.hide('user_id').append('create_time')
		return self.fields

	@classmethod
	def get_summary_by_user(cls, uid, page=1, size=10):
		paginator = cls.query.filter_by(user_id=uid) \
			.order_by(cls.create_time.desc()) \
			.paginate(page=page, per_page=size, error_out=True)
		paginator.hide('snap_items', 'snap_address', 'prepay_id')
		return {
			'total': paginator.total,
			'current_page': paginator.page,
			'items': paginator.items
		}

	@classmethod
	def get_summary(cls, page=1, size=10):
		paginator = cls.query.filter_by().order_by(
			cls.create_time.desc()
		).paginate(
			page=page,
			per_page=size,
			error_out=True
		)
		paginator.hide('snap_items', 'snap_address', 'prepay_id').append('create_time')
		return {
			'total': paginator.total,
			'current_page': paginator.page,
			'items': paginator.items
		}
