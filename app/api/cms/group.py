# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  ↓↓↓ 权限组管理接口 ↓↓↓
"""

from app.core.auth import find_auth_module, get_ep_name
from app.libs.error_code import Success, NotFound, Forbidden
from app.libs.redprint import RedPrint
from app.core.token_auth import auth
from app.core.db import db
from app.models.user import User as UserModel
from app.models.group import Group as GroupModel
from app.models.auth import Auth as AuthModel
from app.api_docs.cms import group as api_doc
from app.validators.base import BaseValidator
from app.validators.forms import PaginateValidator, UpdateGroupValidator

__author__ = 'Allen7D'

api = RedPrint(name='group', description='权限组管理', api_doc=api_doc, alias='cms_group')


@api.route('/all', methods=['GET'])
@api.route_meta(auth='查询所有权限组', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def get_group_all():
    '''查询所有权限组'''
    group_list = GroupModel.get_all()
    if not group_list:
        raise NotFound(msg='不存在任何权限组')
    return Success(group_list)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.group_id'], auth=True)
@auth.admin_required
def get_group(id):
    '''查询一个权限组及其权限'''
    group = GroupModel.get_or_404(id=id, msg='分组不存在')
    group.append('auth_list')
    return Success(group)


@api.route('', methods=['POST'])
@api.doc(args=['body.group_name', 'body.auth_ids', 'body.info'], auth=True)
@auth.admin_required
def create_group():
    '''新建权限组'''
    validator = BaseValidator.get_args_json()
    name = validator['name']  # 权限组名
    auth_ids = validator['auth_ids']  # 权限IDs
    auth_list = [get_ep_name(auth_id) for auth_id in auth_ids]  # 权限名列表
    info = validator['info']  # 权限组名描述

    with db.auto_commit():
        group = GroupModel.create(name=name, info=info, commit=False)
        db.session.flush()
        for auth in auth_list:
            meta = find_auth_module(auth)
            if meta:
                AuthModel.create(auth=meta.name, module=meta.module, group_id=group.id, commit=False)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['g.path.group_id', 'body.group_name', 'body.info'], auth=True)
@auth.admin_required
def update_group(id):
    '''更新权限组'''
    form = UpdateGroupValidator().validate_for_api()
    group = GroupModel.get_or_404(id=id, msg='分组不存在，更新失败')
    group.update(name=form.name.data, info=form.info.data)
    return Success()


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(args=['g.path.group_id'], auth=True)
@auth.admin_required
def delete_group(id):
    '''删除权限组'''
    group = GroupModel.get_or_404(id=id, msg='分组不存在，删除失败')
    if UserModel.get(group_id=id):
        raise Forbidden(msg='分组下存在用户，不可删除')

    # 删除group拥有的权限
    AuthModel.query.filter_by(group_id=id).delete()
    group.delete()
    return Success()
