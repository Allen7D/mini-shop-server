# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
  ↓↓↓ 普通用户接口 ↓↓↓
"""
from flask import g

from app.libs.enums import ScopeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.user import User
from app.api_docs.v1 import user as api_doc  # api_doc可以引入
from app.validators.base import BaseValidator

__author__ = 'Allen7D'

# 直接将api文档的内容放入RedPrint中
api = RedPrint(name='user', description='用户', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(auth=True)
@auth.login_required
def get_user():
    '''用户获取自身信息'''
    # g变量是「线程隔离」的，是全局变量(方便在各处调用)；「g.user」是当前用户
    user = User.query.get_or_404(ident=g.user.uid)
    return Success(user)


@api.route('', methods=['POST'])
@api.doc(args=['body.email', 'body.nickname', '*str.body.password'])
def create_user():
    '''用户注册'''
    validator = BaseValidator().get_all_json()
    validator['auth'] = ScopeEnum.USER.value
    user = User.create(**validator)
    return Success(data=user, error_code=1)


@api.route('', methods=['PUT'])
@api.doc(auth=True)
@auth.login_required
def update_user():
    '''用户更改自身信息'''
    validator = BaseValidator().get_all_json()  # 快速获取所有的非校验的参数
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc(auth=True)
@auth.login_required
def delete_user():
    '''用户注销'''
    # 取代user = User.query.get_or_404(uid)，即使删除了还是能查到
    user = User.query.filter_by(id=g.user.uid).first_or_404()
    user.delete()
    return Success(error_code=2)
