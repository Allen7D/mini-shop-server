# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/7/5.
  业务逻辑：
  	用户在选择商品后，向 API 提交包含祂所选择的商品的相关信息
  	API 在接收到信息后，需要检查订单相关商品的库存量
	有库存，把订单数据存入数据库中
	下单成功了，返回客户端消息，告诉客户端可以支付了
	调用 API 的支付接口，进行支付
	还需要再次进行库存量检测
	服务器这边就可以调用微信的支付接口进行支付
	微信会分别给小程序和 API 返回支付结果
	成功后，进行库存量的检查
	成功，进行库存量的扣除；失败，返回一个支付失败的结果
"""
from app.libs.redprint import RedPrint
from app.libs.error_code import Success
from app.libs.token_auth import auth
from app.service.order import Order as OrderService
from app.validators.params import OrderPlace
from flask import g

__author__ = 'Alimazing'

api = RedPrint(name='order', description='订单')


@api.route('', methods=['POST'])
@api.doc()
@auth.login_required
def place_order():
	'''提交订单(管理员不能调用)'''
	products = OrderPlace().validate_for_api().products.data
	order = OrderService()
	status = order.palce(uid=g.user.uid, o_products=products)
	return Success(status)


@api.route('/<int:id>', methods=['GET'])
@api.doc()
def get_detail():
	pass


@api.route('/by_user', methods=['GET'])
@api.doc()
def get_summary_by_user():
	'''按用户查询'''
	page = 1
	size = 15
	pass


@api.route('/paginate', methods=['GET'])
@api.doc()
def get_summary():
	'''分页查询'''
	page = 1
	size = 20
	pass


@api.route('/delivery', methods=['PUT'])
@api.doc()
def delivery():
	pass
