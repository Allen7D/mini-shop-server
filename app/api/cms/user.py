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

__author__ = 'Allen7D'

api = RedPrint(name='user', description='管理用户', api_doc=api_doc, alias='cms_user')


@api.route('/<int:uid>', methods=['GET'])
@api.doc()
@auth.login_required
def super_get_user(uid):
	# user = User.query.get_or_404(uid) # 会查询到已经被删除的数据
	user = User.query.filter_by(id=uid).first_or_404()
	return Success(user)


@api.route('/<int:uid>', methods=['POST'])
@api.doc()
@auth.login_required
def super_update_user(uid):
	pass


@api.route('/<int:uid>', methods=['DELETE'])
@api.doc()
@auth.login_required
def super_delete_user(uid):
	with db.auto_commit():
		# 取代user = User.query.get_or_404(uid)，即使删除了还是能查到
		user = User.query.filter_by(id=uid).first_or_404()
		user.delete()
	return Success(error_code=2)


@api.route('/test', methods=['GET'])
@api.doc()
def super_test():
	return Success()
