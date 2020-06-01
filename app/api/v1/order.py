# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/7/5.
  ↓↓↓ 订单接口 ↓↓↓
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
from flask import g

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import order as api_doc
from app.core.token_auth import auth
from app.service.order import OrderService
from app.models.order import Order
from app.dao.order import OrderDao
from app.libs.error_code import Success
from app.validators.forms import PaginateValidator, OrderPlaceValidator, OrderIDValidator

__author__ = 'Allen7D'

api = Redprint(name='order', description='订单', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(auth=True)
@auth.login_required
def place_order():
    '''提交订单'''
    products = OrderPlaceValidator().validate_for_api().products.data
    status = OrderService().palce(uid=g.user.id, o_products=products)
    return Success(status)


@api.route('', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_order_list():
    '''查询订单列表'''
    validator = PaginateValidator().nt_data
    paged_orders = OrderDao.get_summary_by_user(
        uid=g.user.id,
        page=validator.page,
        size=validator.size)
    return Success(paged_orders)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.order_id'], auth=True)
@auth.login_required
def get_order(id):
    '''查询订单详情'''
    order = Order.query.get_or_404(id).hide('prepay_id')
    return Success(order)
