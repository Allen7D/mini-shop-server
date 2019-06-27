# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from flask import g

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.api_docs.v1 import user as api_doc

__author__ = 'Allen7D'

# 直接将api文档的内容放入RedPrint中
api = RedPrint(name='user', description='用户', api_doc=api_doc)

'''
	↓↓↓ 普通用户接口 ↓↓↓
'''


@api.route('', methods=['GET'])
@api.doc()
@auth.login_required
def get_user():
	'''用户获取自身信息'''
	uid = g.user.uid  # g变量是「线程隔离」的，是全局变量(方便在各处调用)；「g.user」是当前用户
	user = User.query.filter_by(id=uid).first_or_404()
	return Success(user)


@api.route('', methods=['PUT'])
@api.doc()
def update_user():
	'''用户更改自身信息'''
	return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.doc()
@auth.login_required
def delete_user():
	'''用户注销'''
	uid = g.user.uid  # g变量是「线程隔离」的
	with db.auto_commit():
		# 取代user = User.query.get_or_404(uid)，即使删除了还是能查到
		user = User.query.filter_by(id=uid).first_or_404()
		user.delete()
	return Success(error_code=2)

# 创建用户在clinet.py中
