# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/6/27.
  ↓↓↓ 管理员接口 ↓↓↓
"""
from app.libs.core import get_ep_id
from app.libs.enums import ScopeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User as UserModel
from app.models.auth import Auth as AuthModel
from app.api_docs.cms import user as api_doc
from app.validators.base import BaseValidator
from app.validators.forms import PaginateValidator, ResetPasswordValidator, UpdateAdminValidator

__author__ = 'Allen7D'

api = RedPrint(name='user', description='用户管理', api_doc=api_doc, alias='cms_user')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='获取用户列表', module='用户')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_user_list():
    '''获取用户列表(分页)'''
    validator = PaginateValidator().validate_for_api()
    page = validator.page.data
    size = validator.size.data

    paginator = UserModel.query.filter_by(auth=ScopeEnum.USER.value).paginate(page=page, per_page=size, error_out=False)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:uid>', methods=['GET'])
@api.route_meta(auth='获取用户详情', module='用户')
@api.doc(args=['g.path.uid+'], auth=True)
@auth.group_required
def get_user(uid):
    '''获取用户信息'''
    user = UserModel.query.filter_by(id=uid).first_or_404()
    return Success(user)


@api.route('/<int:uid>', methods=['PUT'])
@api.route_meta(auth='更新用户', module='用户')
@api.doc(args=['g.path.uid+', 'g.body.group_id'], auth=True)
@auth.group_required
def update_user(uid):
    '''更新用户信息(仅能重新分组)'''
    group_id = UpdateAdminValidator().validate_for_api().group_id.data
    user = UserModel.get_or_404(id=uid)
    user.update(group_id=group_id)
    return Success(error_code=1)


@api.route('/<int:uid>', methods=['DELETE'])
@api.route_meta(auth='删除用户', module='用户')
@api.doc(args=['g.path.uid+'], auth=True)
@auth.group_required
def delete_user(uid):
    '''删除用户'''
    user = UserModel.query.filter_by(id=uid).first_or_404()
    user.delete()
    return Success(error_code=2)


@api.route('/<int:uid>/password', methods=['PUT'])
@api.route_meta(auth='更改用户密码', module='用户')
@api.doc(args=['g.path.uid+', 'g.body.new_password', 'g.body.confirm_password'], auth=True)
@auth.group_required
def reset_password(uid):
    '''更改用户密码'''
    new_password = ResetPasswordValidator().validate_for_api().new_password.data

    user = UserModel.query.filter_by(id=uid).first_or_404()
    user.update(password=new_password)
    return Success(error_code=1)


@api.route('/auths', methods=['GET'])
@api.route_meta(auth='查询自己拥有的权限', module='用户', mount=False)
@api.doc(auth=True)
@auth.login_required
def get_auth_list():
    '''查询自己拥有的权限'''
    user = UserModel.get_current_user()
    auth_list = db.session.query(AuthModel.auth, AuthModel.module)\
        .filter_by(group_id=user.group_id).all()
    auth_list = [{'id': get_ep_id(auth[0]), 'auth': auth[0], 'module': auth[1]} for auth in auth_list]
    return Success({
        'items': auth_list
    })
