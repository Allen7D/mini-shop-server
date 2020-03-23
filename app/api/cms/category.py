# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/2/27.
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.category import Category
from app.api_docs.cms import category as api_doc
from app.validators.forms import PaginateValidator

__author__ = 'Allen7D'

api = RedPrint(name='category', description='类别管理', api_doc=api_doc, alias='cms_category')


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_list():
	'''获取类别列表(分页)'''
	page_validator = PaginateValidator().validate_for_api()
	page = page_validator.page.data
	size = page_validator.size.data

	paginator = Category.query.filter_by().paginate(page=page, per_page=size, error_out=False)
	return Success({
		'total': paginator.total,
		'current_page': paginator.page,
		'items': paginator.items
	})


@api.route('/<int:id>', methods=['PUT'])
@api.doc(auth=True)
@auth.login_required
def update_one(id):
	'''更新类别信息'''
	pass


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(auth=True)
@auth.login_required
def delete_one(id):
	'''删除某类别'''
	pass
