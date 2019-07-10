# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/4/4.
  「pay接口」只能用户访问，CMS管理员不能反问
"""
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.service.pay import Pay as PayService
from app.validators.params import IDMustBePositiveInt
from app.api_docs.v1 import pay as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='pay', description='支付', api_doc=api_doc)

@api.route('/pre_order', methods=['POST'])
@api.doc()
@auth.login_required
def get_pre_order():
	'''获取预订单'''
	order_id = IDMustBePositiveInt().validate_for_api().id.data
	pay = PayService(order_id)
	pay.pay()
	pass
