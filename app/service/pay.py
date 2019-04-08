# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2019/4/4.
  https://blog.csdn.net/qq_34493908/article/details/81190057
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
			# 待完成
			raise Exception('订单号不允许为NULL')
		self.order_id = order_id

	def pay(self):
		# 检测订单情况
		self.__check_order_valid()
		# 支付前，再次进行库存量检测
		order_service = OrderService()
		status = order_service.check_order_stock(self.order_id)
		if not status['pass']:
			return status

	def __make_wx_pre_order(self):
		pass

	def __check_order_valid(self):
		'''对订单作三种情况的检测'''
		# 1. 验证订单号是否存在
		order = OrderModel.query.filter_by(id=self.order_id)\
			.first_or_404(e=OrderException)
		# 2. 如果订单号存在的，验证订单号与当前用户是否匹配
		if not Token.is_valid_operate(order.user_id):
			raise TokenException(msg='订单与用户不匹配', error_code=1003)
		# 3. 验证订单是否已经被支付过
		if order.order_status != OrderStatusEnum.UNPAID:
			raise OrderException(
				msg='订单已支付',
				error_code=8003,
				code=404
			)

		self.order_no = order.order_no
		return True
