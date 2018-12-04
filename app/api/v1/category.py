# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from app.libs.success_code import Success
from app.libs.redprint import RedPrint
from app.models.category import Category

__author__ = 'Alimazing'

api = RedPrint(name='category', description='产品分类')


@api.route('/all', methods=['GET'])
@api.doc()
def get_all_categories():
	'''获取所有产品的分类'''
	categories = Category.get_all_categories()
	return Success(categories)
