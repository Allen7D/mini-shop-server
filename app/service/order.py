# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/7/5.
"""
import json
from datetime import datetime
from random import randint
from time import time

from app.libs.enums import OrderStatusEnum
from app.libs.error_code import OrderException, UserException
from app.libs.utils import jsonify
from app.models.base import db
from app.models.product import Product
from app.models.order import Order as OrderModel
from app.models.user_address import UserAddress
from app.models.m2m import Order2Product

__author__ = 'Allen7D'


class Order():
	o_products = None  # order products (订单商品)缩写
	s_products = None  # stock products (库存商品)缩写
	uid = None

	def palce(self, uid, o_products):
		'''下单方法'''
		self.o_products = o_products
		self.s_products = self.__get_products_by_order(o_products)
		self.uid = uid
		# 校验库存
		status = self.__get_order_status()
		# 库存未通过
		if not status['pass']:
			status['order_id'] = -1  # 新增order_id属性
			return status
		# 库存量通过，开始创建订单
		order_snap = self.__snap_order(status)
		order = self.__create_order(order_snap)
		order['pass'] = True

		return order

	def __create_order(self, snap):
		'''将订单写入到数据库'''
		order_no = Order.make_order_no()
		from app.models.order import Order as OrderModel
		with db.auto_commit():
			order = OrderModel()
			order.user_id = self.uid
			order.order_no = order_no
			order.total_price = snap['order_price']
			order.total_count = snap['total_count']
			order.snap_img = snap['snap_img']
			order.snap_name = snap['snap_name']
			order.snap_address = snap['snap_address']
			order.snap_items = json.dumps(snap['p_status'], ensure_ascii=False)
			db.session.add(order)

			db.session.flush()  # 刷新数据库缓存，不操作事务
			order_id = order.id # 获取更新后的order信息
			for p in self.o_products:
				# 起初每个p的格式 {'product_id': x, 'count': y}
				p['order_id'] = order_id
			db.session.add_all(
				[Order2Product(p['order_id'], p['product_id'], p['count']) for p in self.o_products]
			)

		return {
			'order_no': order_no,
			'order_id': order_id,
			'create_time': order.create_time
		}

	def __snap_order(self, status):
		'''生成订单快照(不可更改)'''
		snap = {
			'order_price': 0,  # 订单总价
			'totalCount': 0,  # 订单中商品总数
			'p_status': [],  # 所有商品的状态
			'snap_address': '',  # 用户收获地址
			'snap_name': '',  # 订单缩略的名字(首个商品)
			'snap_img': ''  # 订单缩略的图片(首个商品)
		}
		snap['order_price'] = status['order_price']
		snap['total_count'] = status['total_count']
		snap['p_status'] = status['p_status_array']
		snap['snap_address'] = json.dumps(self.__get_user_address(), ensure_ascii=False)  # 建议:放在非关系型数据库(MongoDB)
		snap['snap_name'] = self.s_products[0]['name'] + (' 等' if len(self.s_products) > 1 else '')
		snap['snap_img'] = self.s_products[0]['main_img_url']

		return snap

	def __get_user_address(self):
		user_address = UserAddress.query \
			.filter_by(user_id=self.uid) \
			.first_or_404(e=UserException(error_code=6001, msg='用户地址不存在, 下单失败'))
		order_address = jsonify(user_address)  # 序列化，因为要存入到数据库
		return order_address

	def check_order_stock(self, order_id):
		'''确定订单库存(用于订单接口和支付接口)
		用order_id查询o_product和s_products
		:param order_id: 订单ID
		:return:
		'''
		self.o_products = Order2Product.query.filter_by(order_id=order_id).all()
		self.s_products = self.__get_products_by_order(self.o_products)
		status = self.__get_order_status()

		return status

	def __get_order_status(self):
		'''
		基于检测一组商品的库存量(__get_product_status)，确定订单的状态
		:return: 订单的状态
		'''
		status = {
			'pass': True,
			'order_price': 0,  # 订单的总价
			'total_count': 0,  # 订单中所有商品的总数
			'p_status_array': []  # 保存所有商品的详细信息
		}
		# 查询每个 o_product 对应的库存量的状态(p_status)
		# 将结果依次统计合并，写入 status 中
		for o_product in self.o_products:
			p_status = self.__get_product_status(o_pid=o_product['product_id'],
												 o_count=o_product['count'],
												 s_products=self.s_products)
			if not p_status['has_stock']:
				status['pass'] = False
			status['order_price'] += p_status['total_price']
			status['total_count'] += p_status['count']
			status['p_status_array'].append(p_status)

		return status

	def __get_product_status(self, o_pid, o_count, s_products):
		'''
		获取订单中「某一个商品」(基于o_pid查询)在对照库存量后的状态
		第1步: 判断在s_products中是否有库存；「无库存」则显示为-1(找不到)，且报错
		第2步: 如果有库存，则将「该商品的库存信息」写入p_status中
		第3步: 判断库存量是否充足(库存量 >= 订单量)
		:param o_pid: 订单中，某商品的ID
		:param o_count: 订单中，某商品的数量
		:param s_products: 订单中，所有商品对应的库存信息
		:return: 对照库存后，某商品的订单信息
		'''
		# 某商品的订单状态
		p_status = {
			'id': None,  # 商品ID
			'has_stock': False,  # 是否有库存
			'count': 0,  # 总数
			'name': '',  # 商品名
			'total_price': 0  # 某商品的总价
		}
		# 「o_pid的商品」处在提取后的库存中的第几个；
		# 第1步
		s_products_ids = [s_p.id for s_p in s_products]
		try:
			p_index = s_products_ids.index(o_pid)  # 「订单商品」在「库存」的序号
		except ValueError:
			raise OrderException(msg='id为{}的商品不存在，创建订单失败'.format(o_pid))

		# 第2步
		s_product = s_products[p_index]
		p_status['id'] = s_product.id
		p_status['name'] = s_product.name
		p_status['count'] = o_count
		p_status['total_price'] = s_product.price * o_count
		# 第3步: 库存量 >= 订单量，返回 True
		if s_product.stock - o_count >= 0:
			p_status['has_stock'] = True

		return p_status

	def __get_products_by_order(self, o_products):
		'''
		基于订单中的所有商品的ID，一次性获取库存中对应订单信息的商品
		:param o_products: 订单中的所有商品
		:return: 返回库存中对应订单信息的商品
		'''
		o_pids = list(map(lambda x: x['product_id'], o_products))
		products = Product.query.filter(Product.id.in_(o_pids)).all()
		return products

	@staticmethod
	def delivery(order_id, jump_page=''):
		''' 将订单状态从「已支付」转为「已发货」
			jump_page(跳转页面)
		'''
		order = OrderModel.query.filter_by(id=order_id).first_or_404()
		# 判断是否已付款
		if order.order_status != OrderStatusEnum.PAID:
			raise OrderException(code=403, error_code=8002, msg='订单未支付，或已经更新过订单了')
		with db.auto_commit():
			order.order_status = OrderStatusEnum.DELIVERED
		return {
			'order': order,
			'jump_page': jump_page
		}

	@staticmethod
	def make_order_no():
		'''
		生成唯一的随机且递增的订单标号
		:return: 订单标号
		'''
		now = datetime.now()
		timestamp = time()
		y_code = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		order_sn = y_code[now.year - 2018] + hex(now.month).upper() + str(now.day) \
				   + str('%.6f' % timestamp)[-6:] + str(timestamp)[2: 7] \
				   + str(randint(0, 99)).rjust(2, '0')
		return order_sn
