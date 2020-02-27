# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 产品接口 ↓↓↓
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.product import Product
from app.validators.params import Count, IDMustBePositiveInt
from app.api_docs.v1 import product as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='product', description='产品', api_doc=api_doc)


@api.route('/recent', methods=['GET'])
@api.doc()
def get_recent():
	'''最新的商品'''
	count = Count().validate_for_api().count.data
	products = Product.get_most_recent(count=count)
	return Success(products)


@api.route('/by_category', methods=['GET'])
@api.doc()
def get_all_by_category():
	'''所有 category_id 类的商品'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	products = Product.get_product_by_category(id=id)
	return Success(products)


@api.route('/<int:id>', methods=['GET'])
@api.doc()
def get_product(id):
	'''获取某商品信息'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	product = Product.get_product_detail(id=id)
	return Success(product)
