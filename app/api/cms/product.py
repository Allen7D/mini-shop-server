# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/2/27.
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.api_docs.cms import product as api_doc
from app.models.product import Product
from app.validators.forms import PaginateValidator
from app.validators.params import IDMustBePositiveInt

__author__ = 'Allen7D'

api = RedPrint(name='product', description='产品管理', api_doc=api_doc, alias='cms_product')


@api.route('/list/by_category', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.category_id'], auth=True)
@auth.login_required
def get_list_by_category():
	'''获取商品列表(分页&基于categoryID)'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	page_validator = PaginateValidator().validate_for_api()
	page = page_validator.page.data
	size = page_validator.size.data

	paginator = Product.query.filter_by(category_id=id).paginate(page=page, per_page=size, error_out=False)
	return Success({
		'total': paginator.total,
		'current_page': paginator.page,
		'items': paginator.items
	})

@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['g.path.product_id'], auth=True)
@auth.login_required
def update_one(id):
	'''更新商品信息'''
	return Success(error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(args=['g.path.product_id'], auth=True)
@auth.login_required
def delete_one(id):
	'''删除某商品'''
	Product.delete_by_id(id)
	return Success(error_code=2)
