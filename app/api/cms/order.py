# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/18.
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import order as api_doc
from app.core.token_auth import auth
from app.core.utils import get_request_args, paginate
from app.models.order import Order
from app.dao.order import OrderDao
from app.service.order import OrderService
from app.libs.error_code import Success
from app.validators.forms import TimeIntervalValidator, OrderIDValidator

__author__ = 'Allen7D'

api = Redprint(name='order', module='订单管理', api_doc=api_doc, alias='cms_order')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询订单列表', module='订单')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.start', 'g.query.end'], auth=True)
@auth.group_required
def get_order_list():
    '''查询订单列表'''
    page, size = paginate()
    time_validator = TimeIntervalValidator().nt_data
    paged_orders = OrderDao.get_summary(page=page,
                                        size=size,
                                        start=time_validator.start,
                                        end=time_validator.end)
    return Success(paged_orders)


@api.route('/search', methods=['GET'])
@api.doc(args=['g.query.order_no'], auth=True)
@auth.group_required
def get_order_by_order_no():
    '''查询订单详情(基于订单编号)'''
    order_no = get_request_args().order_no
    order = Order.get_or_404(order_no=order_no).hide('prepay_id')
    return Success(order)


@api.route('/list/by_user', methods=['GET'])
@api.route_meta(auth='查询订单列表', module='订单')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.uid'], auth=True)
@auth.group_required
def get_order_list_by_user():
    '''查询用户的订单列表'''
    page, size = paginate()
    user_id = get_request_args().uid
    order_list = OrderDao.get_summary_by_user(uid=user_id, page=page, size=size)
    return Success(order_list)


@api.route('/delivery', methods=['PUT'])
@api.route_meta(auth='订单发货', module='订单')
@api.doc(args=['g.query.order_id'], auth=True)
@auth.group_required
def delivery():
    '''订单发货'''
    order_id = OrderIDValidator().nt_data.order_id
    rv = OrderService.delivery(order_id)
    return Success(rv)
