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
from app.validators.forms import PaginateValidator

__author__ = 'Allen7D'

api = RedPrint(name='user', description='用户管理', api_doc=api_doc, alias='cms_user')


@api.route('/list', methods=['GET'])
@api.doc(args=['page', 'size'], auth=True)
@auth.login_required
def get_user_list():
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
@api.doc(args=['uid'], auth=True)
@auth.login_required
def get_user(uid):
	'''获取用户信息'''
	user = User.query.filter_by(id=uid).first_or_404()
	return Success(user)


@api.route('/<int:uid>', methods=['PUT'])
@api.doc(args=['uid'], auth=True)
@auth.login_required
def update_user(uid):
	'''更新用户信息'''
	pass


@api.route('/<int:uid>', methods=['DELETE'])
@api.doc(args=['uid'], auth=True)
@auth.login_required
def delete_user(uid):
	'''删除用户'''
	with db.auto_commit():
		user = User.query.filter_by(id=uid).first_or_404()
		user.delete()
	return Success(error_code=2)
