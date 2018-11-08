# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/25.
"""
from flask import g

from app.libs.error_code import UserException
from app.libs.success_code import RenewSuccess, Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.models.user_address import UserAddress
from app.validators.forms import AddressNew
from app import doc

__author__ = 'Alimazing'

api = RedPrint('address')


@api.route('', methods=['GET'])
@auth.login_required
@api.doc(doc.get_address)
def get_address():
	'''获取「用户自身的地址」'''
	uid = g.user.uid
	with db.auto_check_empty(UserException(error_code=6001, msg='用户地址不存在')):
		user_address = UserAddress.query.filter_by(user_id=uid).first_or_404()
	return Success(user_address)


@api.route('', methods=['POST'])
@auth.login_required
@api.doc(doc.renew_address)
def renew_address():
	'''更新「用户自身的地址」'''
	address_info = AddressNew().validate_for_api().data
	uid = g.user.uid
	with db.auto_check_empty(UserException):
		user = User.query.filter_by(id=uid).first_or_404()
	user.save_address(address_info)
	return RenewSuccess()
