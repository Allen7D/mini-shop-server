# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/31.
"""
from flask import g

from app.libs.success_message import Success, RenewSuccess, DeleteSuccess
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

__author__ = 'Alimazing'

api = RedPrint('user')


# 管理员
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_fetch_user(uid):
	# user = User.query.get_or_404(uid) # 会查询到已经被删除的数据
	user = User.query.filter_by(id=uid).first_or_404()
	return Success(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
	with db.auto_commit():
		# 取代user = User.query.get_or_404(uid)，即使删除了还是能查到
		user = User.query.filter_by(id=uid).first_or_404()
		user.delete()
	return DeleteSuccess()


@api.route('', methods=['GET'])
@auth.login_required
def fetch_user():
	uid = g.user.uid  # g变量是「线程隔离」的
	user = User.query.filter_by(id=uid).first_or_404()
	return Success(user)


@api.route('/<int:uid>', methods=['PUT'])
def update_user():
	return RenewSuccess()


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
	uid = g.user.uid  # g变量是「线程隔离」的
	with db.auto_commit():
		# 取代user = User.query.get_or_404(uid)，即使删除了还是能查到
		user = User.query.filter_by(id=uid).first_or_404()
		user.delete()
	return DeleteSuccess()

# 创建用户在clinet.py中
