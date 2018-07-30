# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/7/5.
"""
import json
from datetime import datetime
from random import randint
from time import time

from app.libs.error_code import OrderException, UserException
from app.libs.utils import jsonify
from app.models.base import db
from app.models.product import Product
from app.models.user_address import UserAddress
from app.models.m2m import Order2Product

__author__ = 'Alimazing'


class Order():
	o_products = None  # order products 缩写
	s_products = None  # stock products 缩写
	uid = None

	def palce(self, uid, o_products):
		self.o_products = o_products
		self.s_products = self.__get_products_by_order(o_products)
		self.uid = uid

		status = self.__get_order_status()
		if not status['pass']:
			status['order_id'] = -1
			return status

		# 开始创建订单
		order_snap = self.__snap_order()

	def __create_order(self, snap):
		order_no = Order.make_order_no()
		from app.models.order import Order as ModelOrder
		with db.auto_commit():
			order = ModelOrder()
			order.user_id = self.uid
			order.order_no = order_no
			order.total_price = snap['order_price']
			order.total_count = snap['total_count']
			order.snap_img = snap['snap_img']
			order.snap_name = snap['snap_name']
			order.snap_address = snap['snap_address']
			order.snap_items = json.dumps(snap['p_status'])
			db.session.add(order)

		order_id = order.id
		for p in self.o_products:
			p['order_id'] = order_id

		with db.auto_commit():
			order_product = Order2Product()

	# 生成订单快照
	def __snap_order(self, status):
		snap = {
			'order_price': 0,
			'totalCount': 0,
			'p_status': [],
			'snap_address': '',
			'snap_name': '',
			'snap_img': ''
		}
		snap['order_price'] = status['order_price']
		snap['total_count'] = status['total_count']
		snap['p_status'] = status['p_status_array']
		snap['snap_address'] = json.dumps(self.__get_user_address())  # 放在文档型数据库
		snap['snap_name'] = self.s_products[0]['name'] + (' 等' if len(self.s_products) > 1 else '') # 订单缩略的名字：首个
		snap['snap_img'] = self.s_products[0]['main_img_url']  # 订单缩略的图片：首个

	def __get_user_address(self):
		with db.auto_check_empty(UserException(error_code=6001, msg='用户地址不存在, 下单失败')):
			user_address = UserAddress.query.filter_by(user_id=self.uid).first_or_404()
		return jsonify(user_address)

	def __get_order_status(self):
		status = {
			'pass': True,
			'order_price': 0,
			'total_count': 0,
			'p_status_array': []
		}
		for o_product in self.o_products:
			p_status = self.__get_product_status(
				o_product['product_id'], o_product['count'], self.s_products
			)
			if p_status['has_stock']:
				status['pass'] = False
			status['order_price'] += p_status['total_price']
			status['total_count'] += p_status['count']
			status['p_status_array'].append(p_status)

		return status

	def __get_product_status(self, o_pid, o_count, s_products):
		p_index = -1
		p_status = {
			'id': None,
			'has_stock': False,
			'count': 0,
			'name': '',
			'total_price': 0
		}
		for i in range(len(s_products)):
			if o_pid == s_products[i].id:
				p_index = i  # 「o_pid的商品」处在提取后的库存空的第几个；找不到则为0

		if p_index == -1:
			raise OrderException(msg='id为' + o_pid + '的商品不存在，创建订单失败')
		else:
			s_product = s_products[p_index]
			p_status['id'] = s_product.id
			p_status['name'] = s_product.name
			p_status['count'] = o_count
			p_status['total_price'] = s_product.price * o_count
			if s_product.stock - o_count >= 0:
				p_status['has_stock'] = True

		return p_status

	# 根据订单消息查找真实的商品信息
	def __get_products_by_order(self, o_products):
		o_pids = list(map(lambda x: x['product_id'], o_products))
		products = Product.query.filter(id.in_(o_pids)).all()
		return products

	# 生成唯一的订单标号
	@staticmethod
	def make_order_no():
		now = datetime.now()
		timestamp = time()
		y_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		order_sn = y_code[now.year - 2018] + hex(now.month).upper() + now.day \
				   + str('%.6f' % timestamp)[-6:] + str(timestamp)[2: 7] \
				   + str(randint(0, 99))
		return order_sn
