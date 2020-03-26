# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/22.
  ↓↓↓ 订单管理接口 ↓↓↓
"""

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.service.order import Order as OrderService
from app.models.order import Order as OrderModel
from app.api_docs.cms import order as api_doc
from app.validators.forms import PaginateValidator, IDMustBePositiveIntValidator

__author__ = 'Allen7D'

api = RedPrint(name='order', description='订单管理', api_doc=api_doc, alias='cms_order')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='获取订单列表', module='订单')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_summary():
    '''获取全部订单简要信息(分页)'''
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
