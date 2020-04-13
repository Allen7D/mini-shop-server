# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/25.
  ↓↓↓ 用户地址接口 ↓↓↓
"""
from flask import g

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.core.token_auth import auth
from app.models.user_address import UserAddress
from app.validators.base import BaseValidator
from app.validators.forms import UpdateAddressValidator
from app.extensions.api_docs.v1 import address as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='address', description='配送信息', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_all_address():
    '''查询所有「配送信息」'''
    uid = g.user.uid
    user_address_list = UserAddress.query.filter_by(user_id=uid).all_by_wrap(
        error_code=6001, msg='配送地址不存在')
    return Success(user_address_list)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.address_id'], auth=True)
@auth.login_required
def get_address(id):
    '''查询「配送信息」'''
    user_address = UserAddress.get_or_404(id=id, error_code=6001, msg='配送地址不存在')
    return Success(user_address)


@api.route('', methods=['POST'])
@api.doc(args=['name', 'mobile', 'province', 'city', 'country', 'detail'], auth=True)
@auth.login_required
def create_address():
    '''新增「配送信息」'''
    address_info = UpdateAddressValidator().validate_for_api().dt_data
    UserAddress.create(user_id=g.user.uid, **address_info)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['g.path.address_id', 'name', 'mobile', 'province', 'city', 'country', 'detail'], auth=True)
@auth.login_required
def update_address(id):
    '''更新「配送信息」'''
    address_info = UpdateAddressValidator().validate_for_api().dt_data
    user_address = UserAddress.get_or_404(id=id, user_id=g.user.uid)
    user_address.update(**address_info)
    return Success(error_code=1)


@api.route('<int:id>', methods=['DELETE'])
@api.doc(args=['*int.path.address_id'], auth=True)
@auth.login_required
def delete_address(id):
    '''删除「配送信息」'''
    validator = BaseValidator.get_args_json()
    user_address = UserAddress.get_or_404(id=validator['id'], user_id=g.user.uid)
    user_address.delete()
    return Success(error_code=2)
