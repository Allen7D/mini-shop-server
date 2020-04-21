# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  ↓↓↓ 管理员(能登录CMS的系统工作人员)管理接口 ↓↓↓
"""
from flask import request

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import admin as api_doc
from app.core.token_auth import auth
from app.dao.admin import AdminDao
from app.dao.user import UserDao
from app.libs.error_code import Success
from app.validators.forms import PaginateValidator, ResetPasswordValidator, CreateAdminValidator

__author__ = 'Allen7D'

api = Redprint(name='admin', description='管理员管理', api_doc=api_doc, alias='cms_admin')

@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询管理员列表', module='管理员', mount=False)
@api.doc(args=['g.query.page', 'g.query.size', 'query.group_id'], auth=True)
@auth.admin_required
def get_admin_list():
    '''查询管理员列表'''
    paginate = PaginateValidator().get_data()
    group_id = int(request.args.get('group_id'))  # 可选
    user_list = AdminDao.get_admin_list(group_id=group_id, page=paginate.page, size=paginate.size)
    return Success(user_list)


@api.route('', methods=['POST'])
@api.route_meta(auth='新增管理员', module='管理员', mount=False)
@api.doc(args=['g.body.nickname', 'g.body.password', 'g.body.confirm_password',
               'g.body.group_id', 'g.body.email', 'g.body.mobile'], auth=True)
@auth.admin_required
def create_admin():
    '''新增管理员'''
    form = CreateAdminValidator().get_data(as_dict=True)
    AdminDao.create_admin(form)
    return Success()


@api.route('/<int:uid>', methods=['PUT'])
@api.route_meta(auth='更新管理员', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def update_admin(uid):
    '''更新管理员'''
    AdminDao.update_admin(uid)
    return Success(error_code=1)


@api.route('/<int:uid>', methods=['GET'])
@api.route_meta(auth='删除管理员', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def delete_admin(uid):
    '''删除管理员'''
    AdminDao.delete_admin(uid)
    return Success(error_code=2)


@api.route('/password/<int:uid>', methods=['PUT'])
@api.route_meta(auth='修改管理员密码', module='管理员', mount=False)
@api.doc(auth=True)
@auth.admin_required
def change_user_password(uid):
    '''修改管理员密码'''
    new_password = ResetPasswordValidator().get_data().new_password
    UserDao.reset_password(uid=uid, password=new_password)
    return Success(error_code=1, msg='密码修改成功')


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
