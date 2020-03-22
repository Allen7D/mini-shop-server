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
from app.validators.base import BaseValidator
from app.validators.forms import UpdateAddressValidator
from app.api_docs.v1 import address as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='address', description='配送信息', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_all():
    '''获取所有「配送信息」'''
    uid = g.user.uid
    user_address_list = UserAddress.query.filter_by(user_id=uid).all_or_404(
        error_code=6001, msg='配送地址不存在')
    return Success(user_address_list)


@api.route('', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_one():
    '''获取「配送信息」'''
    uid = g.user.uid
    user_address = UserAddress.get_or_404(user_id=uid, error_code=6001, msg='配送地址不存在')
    return Success(user_address)


@api.route('', methods=['POST'])
@api.doc(args=['name', 'mobile', 'province', 'city', 'country', 'detail'], auth=True)
@auth.login_required
def create_one():
    '''新增「配送信息」'''
    address_info = UpdateAddressValidator().validate_for_api().data
    user = User.get_or_404(id=g.user.uid, e=UserException)
    user.save_address(address_info)
    return Success(error_code=1)


@api.route('', methods=['PUT'])
@api.doc(args=['name', 'mobile', 'province', 'city', 'country', 'detail'], auth=True)
@auth.login_required
def update_one():
    '''更新「配送信息」'''
    address_info = UpdateAddressValidator().validate_for_api().data
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404(e=UserException)
    user.save_address(address_info)
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(args=['*int.path.address_id'], auth=True)
@auth.login_required
def delete_one():
    '''删除「配送信息」'''
    uid = g.user.uid
    validator = BaseValidator().get_all_json()
    user_address = UserAddress.get_or_404(user_id=uid, id=validator.address_id)
    user_address.delete()
    return Success(error_code=2)
