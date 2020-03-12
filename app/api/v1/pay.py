# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/4/4.
  ↓↓↓ 支付接口 ↓↓↓
  「pay接口」只能用户访问，CMS管理员不能访问
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.service.pay import Pay as PayService
from app.validators.params import IDMustBePositiveInt
from app.api_docs.v1 import pay as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='pay', description='支付', api_doc=api_doc)


@api.route('/pre_order', methods=['POST'])
@api.doc(auth=True)
@auth.login_required
def get_pre_order():
	'''获取预订单'''
	order_id = IDMustBePositiveInt().validate_for_api().id.data
	pay_service = PayService(order_id)
	pay_service.pay()
	Success()


@api.route('/notify', methods=['POST'])
@api.doc(auth=True)
@auth.login_required
def receive_notify():
	'''接收微信平台支付结果
	文档: https://pay.weixin.qq.com/wiki/doc/api/native.php?chapter=9_7&index=8
	微信总共会发起10次通知，通知频率为15s/15s/30s/3m/10m/20m/30m/30m/30m/60m/3h/3h/3h/6h/6h - 总计 24h4m）
	'''

	Success()


@api.route('/re_notify', methods=['POST'])
@api.doc(auth=True)
@auth.login_required
def redirect_notify():
	''''''
	Success()


@api.route('/concurrency', methods=['POST'])
@api.doc(auth=True)
@auth.login_required
def notify_concurrency():
	''''''
	Success()
