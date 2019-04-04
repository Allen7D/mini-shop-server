# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2019/4/4.
"""
from app.service.order import Order as OrderService
from app.models.order import Order as OrderModel

__author__ = 'Alimazing'

class Pay():
	order_id = None
	order_no = None

	def __init__(self, order_id):
		if not order_id:
			raise Exception() # '订单号不允许为NULL'
		self.order_id = order_id

	def pay(self):
		# 库存量检测
		order_service = OrderService()
		status = order_service.check_order_stock(self.order_id)


