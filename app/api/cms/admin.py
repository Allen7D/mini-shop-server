# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  ↓↓↓ 管理员(能登录CMS的系统工作人员)管理接口 ↓↓↓
"""
from flask import current_app, request

from app.extensions.api_docs.redprint import RedPrint
from app.extensions.api_docs.cms import admin as api_doc
from app.core.token_auth import auth
from app.libs.enums import ScopeEnum
from app.models.user import User as UserModel
from app.models.group import Group as GroupModel
from app.libs.error_code import Success
from app.validators.forms import PaginateValidator, ResetPasswordValidator, CreateAdminValidator

__author__ = 'Allen7D'

api = RedPrint(name='admin', description='管理员管理', api_doc=api_doc, alias='cms_admin')


@api.route('/auths', methods=['GET'])
@api.route_meta(auth='查询所有可分配的权限', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def get_auths():
    '''查询所有可分配的权限'''
    endpoint_info_list = current_app.config['EP_INFOS']
    return Success(endpoint_info_list)


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询管理员列表', module='管理员', mount=False)
@api.doc(args=['g.query.page', 'g.query.size', 'query.group_id'], auth=True)
@auth.admin_required
def get_admin_list():
    '''查询管理员列表'''
    paginate = PaginateValidator().validate_for_api().nt_data
    group_id = int(request.args.get('group_id'))  # 可选
    query_condition = {
        'auth': ScopeEnum.COMMON.value,
        'group_id': group_id  # 管理员(至少拥有权限组)
    } if group_id else {
        'auth': ScopeEnum.COMMON.value
    }
    user_list = UserModel.query \
        .filter_by(**query_condition) \
        .paginate(page=paginate.page, per_page=paginate.size, error_out=False)
    return Success(user_list)


@api.route('', methods=['POST'])
@api.route_meta(auth='新增管理员', module='管理员', mount=False)
@api.doc(args=['g.body.nickname', 'g.body.password', 'g.body.confirm_password',
               'g.body.group_id', 'g.body.email', 'g.body.mobile'], auth=True)
@auth.admin_required
def create_admin():
    '''新增管理员'''
    form = CreateAdminValidator().validate_for_api()
    UserModel.abort_repeat(nickname=form.nickname.data, msg='用户名重复，请重新输入')
    UserModel.create(auth=ScopeEnum.COMMON.value, **form.data)
    return Success()


@api.route('/<int:uid>', methods=['PUT'])
@api.route_meta(auth='更新管理员', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def update_admin(uid):
    '''更新管理员'''
    user = UserModel.get_or_404(id=uid, msg='用户不存在')
    return Success()


@api.route('/<int:uid>', methods=['GET'])
@api.route_meta(auth='删除管理员', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def delete_admin(uid):
    '''删除管理员'''
    user = UserModel.get_or_404(id=uid, msg='用户不存在')
    user.hard_delete()
    return Success()


@api.route('/password/<int:uid>', methods=['PUT'])
@api.route_meta(auth='修改管理员密码', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def change_user_password(uid):
    '''修改管理员密码'''
    form = ResetPasswordValidator().validate_for_api()
    user = UserModel.get_or_404(id=uid, msg='用户不存在')
    user.update(password=form.new_password.data)
    return Success(msg='密码修改成功')


@api.route('/active/<int:uid>', methods=['PUT'])
@api.doc(args=['g.path.uid'], auth=True)
@auth.admin_required
def trans2active(uid):
    '''激活管理员'''
    return Success(msg='操作成功')


@api.route('/disable/<int:uid>', methods=['PUT'])
@api.doc(args=['g.path.uid'], auth=True)
@auth.admin_required
def trans2disable(uid):
    '''禁用管理员'''
    return Success(msg='操作成功')
