# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  ↓↓↓ 权限管理接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import RedPrint
from app.extensions.api_docs.cms import auth as api_doc
from app.core.auth import get_ep_name, find_auth_module
from app.core.token_auth import auth
from app.core.db import db
from app.models.auth import Auth as AuthModel
from app.libs.error_code import Success
from app.validators.forms import AuthsValidator

__author__ = 'Allen7D'

api = RedPrint(name='auth', description='权限管理', api_doc=api_doc, alias='cms_auth')


@api.route('/append', methods=['POST'])
@api.route_meta(auth='新增多个权限', module='管理员', mount=False)
@api.doc(args=['g.body.group_id', 'g.body.auth_ids'], auth=True)
@auth.admin_required
def create_auth_list():
    '''添加多个权限(到某个权限组)'''
    validator = AuthsValidator().validate_for_api()
    auth_name_list = [get_ep_name(id) for id in validator.auth_ids.data]
    group_id = validator.group_id.data

    with db.auto_commit():
        for name in auth_name_list:
            one = AuthModel.get(group_id=group_id, name=name)
            if not one:
                meta = find_auth_module(name)
                AuthModel.create(group_id=group_id, name=meta.name,
                                 module=meta.module, commit=False)
    return Success(error_code=1)


@api.route('/remove', methods=['POST'])
@api.route_meta(auth='删除多个权限', module='管理员', mount=False)
@api.doc(args=['g.body.group_id', 'g.body.auth_ids'], auth=True)
@auth.admin_required
def delete_auth_list():
    '''删除多个权限(从某个权限组)'''
    validator = AuthsValidator().validate_for_api()
    auth_name_list = [get_ep_name(id) for id in validator.auth_ids.data]
    group_id = validator.group_id.data

    with db.auto_commit():
        db.session.query(AuthModel).filter(
            AuthModel.name.in_(auth_name_list),
            AuthModel.group_id == group_id
        ).delete(synchronize_session=False)
    return Success(error_code=2)
