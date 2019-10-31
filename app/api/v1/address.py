# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/25.
  ↓↓↓ 用户地址接口 ↓↓↓
"""
from flask import g

from app.libs.error_code import Success, UserException
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.user import User
from app.models.user_address import UserAddress
from app.validators.forms import AddressNew
from app.api_docs.v1 import address as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='address', description='用户地址', api_doc=api_doc)

@api.route('', methods=['GET'])
@api.doc()
@auth.login_required
def get_address():
	'''获取「用户自身的地址」'''
	uid = g.user.uid
	user_address = UserAddress.query.filter_by(user_id=uid).first_or_404(
		error_code=6001, msg='用户地址不存在')
	return Success(user_address)


@api.route('', methods=['POST'])
@api.doc()
@auth.login_required
def update_address():
	'''更新「用户自身的地址」'''
	address_info = AddressNew().validate_for_api().data
	uid = g.user.uid
	user = User.query.filter_by(id=uid).first_or_404(e=UserException)
	user.save_address(address_info)
	return Success(error_code=1)
