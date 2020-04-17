# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  ↓↓↓ 权限管理接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import RedPrint
from app.extensions.api_docs.cms import auth as api_doc
from app.core.token_auth import auth
from app.dao.auth import AuthDao
from app.libs.error_code import Success
from app.validators.forms import AuthsValidator

__author__ = 'Allen7D'

api = RedPrint(name='auth', description='权限管理', api_doc=api_doc, alias='cms_auth')


@api.route('/append', methods=['POST'])
@api.route_meta(auth='新增多个权限', module='管理员', mount=False)
@api.doc(args=['g.body.group_id', 'g.body.auth_ids'], auth=True)
@auth.admin_required
def append_auth_list():
    '''添加多个权限(到某个权限组)'''
    validator = AuthsValidator().get_data()
    AuthDao.append_auth_list(group_id=validator.group_id, auth_ids=validator.auth_ids)
    return Success(error_code=1)


@api.route('/remove', methods=['POST'])
@api.route_meta(auth='删除多个权限', module='管理员', mount=False)
@api.doc(args=['g.body.group_id', 'g.body.auth_ids'], auth=True)
@auth.admin_required
def delete_auth_list():
    '''删除多个权限(从某个权限组)'''
    validator = AuthsValidator().get_data()
    AuthDao.delete_auth_list(group_id=validator.group_id, auth_ids=validator.auth_ids)
    return Success(error_code=2)
