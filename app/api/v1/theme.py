# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.theme import Theme
from app.validators.params import IDCollection, IDMustBePositiveInt

__author__ = 'Alimazing'

api = RedPrint('theme')

@api.route('', methods=['GET'])
def get_simple_list():
	'''
	:url /theme
	:arg /theme?ids=id1,id2,id3,...
	:return: 一组theme模型
	'''
	# args = IDCollection().validate_for_api()
	ids = IDCollection().validate_for_api().ids.data
	theme = Theme.get_themes(ids=ids)
	return Success(theme)


@api.route('/<id>', methods=['GET'])
def get_complex_one(id):
	'''
	Theme详情接口
	:url /theme/:id
	:param id: 专题theme的id
	:return: 专题theme的详情
	'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	theme_detail = Theme.get_theme_detail(id=id)
	return Success(theme_detail)
