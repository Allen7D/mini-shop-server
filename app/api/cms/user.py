# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/6/27.
  ↓↓↓ 管理员接口 ↓↓↓
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.api_docs.cms import user as api_doc
from app.validators.base import BaseValidator
from app.validators.forms import PaginateValidator, ResetPasswordValidator

__author__ = 'Allen7D'

api = RedPrint(name='user', description='用户管理', api_doc=api_doc, alias='cms_user')


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_list():
    '''获取用户列表(分页)'''
    validator = PaginateValidator().validate_for_api()
    page = validator.page.data
    size = validator.size.data

    paginator = User.query.filter_by().paginate(page=page, per_page=size, error_out=False)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:uid>', methods=['GET'])
@api.doc(args=['g.path.uid+'], auth=True)
@auth.login_required
def get_one(uid):
    '''获取用户信息'''
    user = User.query.filter_by(id=uid).first_or_404()
    return Success(user)


@api.route('/<int:uid>', methods=['PUT'])
@api.doc(args=['g.path.uid+', '*str.body.name', '*int.body.age'], auth=True)
@auth.login_required
def update_one(uid):
    '''更新用户信息'''
    validator = BaseValidator().get_all_json()  # 快速获取所有的非校验的参数
    return Success(validator, error_code=1)


@api.route('/<int:uid>', methods=['DELETE'])
@api.doc(args=['g.path.uid+'], auth=True)
@auth.login_required
def delete_one(uid):
    '''删除用户'''
    user = User.query.filter_by(id=uid).first_or_404()
    user.delete()
    return Success(error_code=2)


@api.route('/<int:uid>/password', methods=['PUT'])
@api.doc(args=['g.path.uid+', 'g.body.new_password', 'g.body.confirm_password'], auth=True)
@auth.login_required
def reset_password(uid):
    '''更改用户密码'''
    new_password = ResetPasswordValidator().validate_for_api().new_password.data

    user = User.query.filter_by(id=uid).first_or_404()
    user.update(password=new_password)
    return Success(error_code=1)
