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
@api.doc(args=['count'])
def get_recent():
	'''最新的商品'''
	count = Count().validate_for_api().count.data
	product_list = Product.get_most_recent(count=count)
	return Success(product_list)


@api.route('/all/by_category', methods=['GET'])
@api.doc(args=['g.query.category_id'])
def get_all_by_category():
	'''所有 category_id 类的商品'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	product_list = Product.get_product_by_category(id=id)
	return Success(product_list)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.product_id'])
def get_one(id):
	'''获取某商品信息'''
	product = Product.get_product_detail(id=id)
	return Success(product)
