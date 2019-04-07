# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2019/4/4.
"""
from app.libs.enums import OrderStatusEnum
from app.libs.error_code import OrderException, TokenException
from app.service.order import Order as OrderService
from app.models.order import Order as OrderModel
from app.service.token import Token

__author__ = 'Alimazing'

class Pay():
	order_id = None
	order_no = None

	def __init__(self, order_id):
		if not order_id:
			raise Exception() # '订单号不允许为NULL'
		self.order_id = order_id

	def pay(self):
		self.__check_order_valid()
		# 支付前，再次进行库存量检测
		order_service = OrderService()
		status = order_service.check_order_stock(self.order_id)
		if not status['pass']:
			return status

	def __make_wx_pre_order(self):
		pass

	def __check_order_valid(self):
		'''
		订单号可能根本就不存在
		订单号确实是存在的，但是订单号与当前用户是不匹配的
		订单有可能已经被支付过
		:return:
		'''
		order = OrderModel.query.filter_by(id=self.order_id).first_or_404(e=OrderException)
		if not Token.is_valid_operate(order.user_id):
			raise TokenException(msg='订单与用户不匹配', error_code=1003)
		if order.order_status != OrderStatusEnum.UNPAID:
			raise OrderException(
				msg='订单已支付',
				error_code=8003,
				code=404
			)
		self.order_no = order.order_no
		return True
