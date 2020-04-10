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

from app.libs.redprint import RedPrint
from app.libs.error_code import Success
from app.core.token_auth import auth
from app.service.order import Order as OrderService
from app.models.order import Order as OrderModel
from app.validators.forms import PaginateValidator, OrderPlaceValidator, IDMustBePositiveIntValidator
from app.api_docs.v1 import order as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='order', description='订单', api_doc=api_doc)


@api.route('', methods=['POST'])
@api.doc(auth=True)
@auth.login_required
def place_order():
    '''提交订单(管理员X)'''
    products = OrderPlaceValidator().validate_for_api().products.data
    status = OrderService().palce(uid=g.user.uid, o_products=products)
    return Success(status)


@api.route('/by_user', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_summary_by_user():
    '''用户查询「自身订单列表」'''
    validator = PaginateValidator().validate_for_api()
    paged_orders = OrderModel.get_summary_by_user(uid=g.user.uid,
                                                  page=validator.page.data,
                                                  size=validator.size.data)
    return Success(paged_orders)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.order_id'], auth=True)
@auth.login_required
def get_order(id):
    '''订单详情'''
    order = OrderModel.query.get_or_404(id).hide('prepay_id')
    return Success(order)


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询订单列表', module='订单')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_list_by_summary():
    '''查询订单列表'''
    validator = PaginateValidator().validate_for_api()
    paged_orders = OrderModel.get_summary(page=validator.page.data,
                                          size=validator.size.data)
    return Success(paged_orders)


@api.route('/delivery', methods=['PUT'])
@api.route_meta(auth='订单发货', module='订单')
@api.doc(args=['g.query.order_id'], auth=True)
@auth.group_required
def delivery():
    '''订单发货'''
    order_id = IDMustBePositiveIntValidator().validate_for_api().id.data
    result = OrderService.delivery(order_id)
    Success(result)
