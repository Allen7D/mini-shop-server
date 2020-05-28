# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
  ↓↓↓ 普通用户接口 ↓↓↓
"""
from flask import g

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import user as api_doc
from app.core.token_auth import auth
from app.models.user import User
from app.dao.user import UserDao
from app.dao.auth import AuthDao
from app.dao.identity import IdentityDao
from app.libs.error_code import Success
from app.validators.forms import BaseValidator, ChangePasswordValidator, \
    CreateUserValidator, UpdateUserValidator, UpdateAvatarValidator

__author__ = 'Allen7D'

api = Redprint(name='user', description='用户', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_user():
    '''查询自身'''
    user = User.get(id=g.user.id)
    return Success(user)


@api.route('', methods=['POST'])
@api.doc(args=['g.body.username', 'g.body.email', 'g.body.mobile', 'g.body.nickname',
               'g.body.password', 'g.body.confirm_password'])
def create_user():
    '''用户注册'''
    form = CreateUserValidator().nt_data
    UserDao.create_user(form)
    return Success(error_code=1)


@api.route('', methods=['PUT'])
@api.doc(args=['g.body.nickname', 'g.body.username', 'g.body.email', 'g.body.mobile'], auth=True)
@auth.login_required
def update_user():
    '''更新自身'''
    form = UpdateUserValidator().nt_data
    UserDao.update_user(uid=g.user.id, form=form)
    return Success(error_code=1)


@api.route('/bind', methods=['PUT'])
@api.doc(args=['g.body.account', 'type'], auth=True)
@auth.login_required
def bind_identity():
    '''绑定账号'''
    validator = BaseValidator.get_args_json()
    IdentityDao.bind(user_id=g.user.id, identifier=validator.account, type=validator.type)
    pass


@api.route('/unbind', methods=['PUT'])
@api.doc(args=['type'], auth=True)
@auth.login_required
def unbind_identity():
    '''解绑账号'''
    type = BaseValidator.get_args_json().type
    IdentityDao.unbind(user_id=g.user.id, type=type)
    return Success()


@api.route('', methods=['DELETE'])
@api.doc(auth=True)
@auth.login_required
def delete_user():
    '''注销自身'''
    UserDao.delete_user(uid=g.user.id)
    return Success(error_code=2)


@api.route('/password', methods=['PUT'])
@api.doc(args=['g.body.new_password', 'g.body.old_password', 'g.body.confirm_password'], auth=True)
@auth.login_required
def change_password():
    '''更改密码'''
    validator = ChangePasswordValidator().nt_data
    UserDao.change_password(
        uid=g.user.id,
        old_password=validator.old_password,
        new_password=validator.new_password
    )
    return Success(error_code=1)


@api.route('/avatar', methods=['PUT'])
@api.doc(args=['g.body.avatar'], auth=True)
@auth.login_required
def set_avatar():
    '''更新用户头像'''
    validator = UpdateAvatarValidator().nt_data
    UserDao.set_avatar(id=g.user.id, avatar=validator.avatar)
    return Success(error_code=1, msg='更新头像成功')


@api.route('/auths', methods=['GET'])
@api.route_meta(auth='查询自己拥有的权限', module='用户', mount=False)
@api.doc(auth=True)
@auth.login_required
def get_auths():
    '''查询自己拥有的权限'''
    auth_list = AuthDao.get_auth_list(group_id=g.user.group_id)
    return Success({
        'items': auth_list
    })
