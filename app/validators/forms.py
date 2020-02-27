# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
  各种提交表单的验证
"""
from collections import namedtuple

from wtforms import StringField, IntegerField, FileField, MultipleFileField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError, NumberRange

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseValidator

__author__ = 'Allen7D'

Address = namedtuple('Address', ['name', 'mobile', 'province', 'city', 'country', 'detail'])


class ClientValidator(BaseValidator):
	account = StringField(validators=[DataRequired(message='Not Null'),
									  length(min=5, max=32)])
	secret = StringField()
	type = IntegerField(validators=[DataRequired()])

	def validate_type(self, value):
		try:
			client = ClientTypeEnum(value.data)
		except ValueError as e:
			raise e
		self.type.data = client


class TokenValidator(BaseValidator):
	token = StringField(validators=[DataRequired()])


class UserEmailValidator(ClientValidator):
	account = StringField(validators=[Email(message='无效email')])
	secret = StringField(validators=[
		DataRequired(),
		# password can only include letters, numbers and "_"
		Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
	])
	nickname = StringField(validators=[
		DataRequired(),
		length(min=2, max=22)
	])

	def validate_account(self, value):
		if User.query.filter_by(email=value.data).first():
			raise ValidationError()


class BookSearchValidator(BaseValidator):
	q = StringField(validators=[DataRequired()])


class UploadFileValidator(BaseValidator):
	# ref==> https://wtforms.readthedocs.io/en/latest/fields.html
	file = FileField(validators=[DataRequired()])


class UploadPDFValidator(BaseValidator):
	origin = FileField(validators=[DataRequired()])
	comparer = FileField(validators=[DataRequired()])


class AddressNew(BaseValidator):
	name = StringField(validators=[DataRequired()])
	mobile = StringField(validators=[
		DataRequired(),
		length(min=11, max=11, message='手机号为11个数字'),
		Regexp(r'^1(3|4|5|7|8)[0-9]\d{8}$')
	])
	province = StringField(validators=[DataRequired()])
	city = StringField(validators=[DataRequired()])
	country = StringField(validators=[DataRequired()])
	detail = StringField()

	@property
	def data(self):
		return Address(
			self.name.data, self.mobile.data, self.province.data,
			self.city.data, self.country.data, self.detail.data
		)

class PaginateValidator(BaseValidator):
	page = IntegerField(default=1) # 当前页
	size = IntegerField(NumberRange(min=1, max=100), default=10) # 每页条目个数

	def validate_page(self, value):
		self.page.data = int(value.data)

	def validate_size(self, value):
		self.size.data = int(value.data)
