# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, ValidationError

from app.validators.base import BaseValidator

__author__ = 'Allen7D'


class IDMustBePositiveInt(BaseValidator):
	id = IntegerField(validators=[DataRequired()])

	def validate_id(self, value):
		id = value.data
		if not self.isPositiveInteger(id):
			raise ValidationError(message='ID 必须为正整数')
		self.id.data = id


class IDCollection(BaseValidator):
	ids = StringField(validators=[DataRequired()])

	def validate_ids(self, value):
		ids = value.data.split(',')
		for id in ids:
			if not self.isPositiveInteger(id):
				raise ValidationError(message='ids 必须是用「,」分隔的正整数列')
		self.ids.data = list(map(lambda x: int(x), ids))


class Count(BaseValidator):
	count = IntegerField(default='15')  # 默认为15，可以省略 DataRequired()

	def validate_count(self, value):
		count = value.data
		if not self.isPositiveInteger(count) or not (1 <= int(count) <= 15):
			raise ValidationError(message='count必须是[1, 15]区间内 的正整数')
		self.count.data = int(count)


class OrderPlace(BaseValidator):
	products = StringField()

	def validate_products(self, value):
		'''
		数据格式: [{'product_id': 1, 'count': 10}, ...]
		'''
		products = value.data
		if not self.isList(products):
			raise ValidationError(message='商品参数不正确')
		if len(products) == 0:
			raise ValidationError(message='商品列表不能为空')
		for product in products:
			if not self.isPositiveInteger(product['product_id']) \
					or not self.isPositiveInteger(product['count']):
				raise ValidationError(message='商品列表参数错误')

		self.products.data = products
