# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/25.
  ↓↓↓ 用户地址接口 ↓↓↓
"""
from flask import g

from app.extensions.api_docs.redprint import RedPrint
from app.extensions.api_docs.v1 import address as api_doc
from app.core.token_auth import auth
from app.models.user_address import UserAddress
from app.dao.address import UserAddressDao
from app.libs.error_code import Success
from app.validators.forms import CreateOrUpdateAddressValidator

__author__ = 'Allen7D'

api = RedPrint(name='address', description='配送信息', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_all_address():
    '''查询所有「配送信息」'''
    address_list = UserAddress.query.filter_by(user_id=g.user.id).all_by_wrap()
    return Success(address_list)


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
    address_info = CreateOrUpdateAddressValidator().get_data(as_dict=True)
    UserAddress.create(user_id=g.user.id, **address_info)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['g.path.address_id', 'name', 'mobile', 'province', 'city', 'country', 'detail'], auth=True)
@auth.login_required
def update_address(id):
    '''更新「配送信息」'''
    address_info = CreateOrUpdateAddressValidator().get_data(as_dict=True)
    UserAddressDao.update_address(id=id, user_id=g.user.id, **address_info)
    return Success(error_code=1)


@api.route('<int:id>', methods=['DELETE'])
@api.doc(args=['*int.path.address_id'], auth=True)
@auth.login_required
def delete_address(id):
    '''删除「配送信息」'''
    UserAddressDao.delete_address(id=id, user_id=g.user.id)
    return Success(error_code=2)
