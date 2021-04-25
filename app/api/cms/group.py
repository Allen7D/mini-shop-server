# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  ↓↓↓ 权限组管理接口 ↓↓↓
"""

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import group as api_doc
from app.core.token_auth import auth
from app.core.utils import get_request_args
from app.models.group import Group
from app.dao.group import GroupDao
from app.libs.error_code import Success
from app.validators.forms import UpdateGroupValidator, MigrateUserValidator

__author__ = 'Allen7D'

api = Redprint(name='group', module='权限组管理', api_doc=api_doc, alias='cms_group')


@api.route('/all', methods=['GET'])
@api.route_meta(auth='查询所有权限组', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def get_all_group():
    '''查询所有权限组'''
    group_list = Group.get_all()
    return Success({
        'items': group_list
    })


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.group_id'], auth=True)
@auth.admin_required
def get_group(id):
    '''查询一个权限组及其权限'''
    group = Group.get_or_404(id=id, msg='分组不存在')
    group.append('auth_list')
    return Success(group)


@api.route('', methods=['POST'])
@api.doc(args=['body.group_name', 'body.auth_ids', 'body.info'], auth=True)
@auth.admin_required
def create_group():
    '''新建权限组'''
    form = get_request_args()
    GroupDao.create_group(name=form.name, auth_ids=form.auth_ids, info=form.info)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['g.path.group_id', 'body.group_name', 'body.info'], auth=True)
@auth.admin_required
def update_group(id):
    '''更新权限组'''
    form = UpdateGroupValidator().nt_data
    GroupDao.update_group(id=id, name=form.name, info=form.info)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(args=['g.path.group_id'], auth=True)
@auth.admin_required
def delete_group(id):
    '''删除权限组'''
    GroupDao.delete_group(id=id)
    return Success(error_code=2)


@api.route('/migrate', methods=['PUT'])
@api.doc(args=['g.body.src_id', 'g.body.dest_id'], auth=True)
@auth.admin_required
def migrate_users():
    '''迁移权限组下的用户'''
    validator = MigrateUserValidator().nt_data
    GroupDao.migrate_users(src_id=validator.src_id, dest_id=validator.dest_id)
    return Success(error_code=1)
