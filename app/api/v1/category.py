# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 类别接口 ↓↓↓
"""
from app.api_docs.v1 import category as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.category import Category

__author__ = 'Allen7D'

api = RedPrint(name='category', description='产品类别', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc()
def get_all():
	'''获取所有产品的分类'''
	categories = Category.get_all_categories()
	return Success(categories)