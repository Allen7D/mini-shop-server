# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
  各种提交表单的验证
"""
from collections import namedtuple

from flask import request
from wtforms import StringField, IntegerField, PasswordField, FileField, MultipleFileField
from wtforms.validators import DataRequired, length, Email, Regexp, EqualTo, ValidationError, NumberRange

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseValidator

__author__ = 'Allen7D'


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


# 重置密码校验
class ResetPasswordValidator(BaseValidator):
    new_password = PasswordField('新密码', validators=[
        DataRequired(message='新密码不可为空'),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='密码长度必须在6~22位之间，包含字符、数字和 _ '),
        EqualTo('confirm_password', message='两次输入的密码不一致，请输入相同的密码')
    ])
    confirm_password = PasswordField('确认新密码', validators=[DataRequired(message='请确认密码')])


# 更改密码校验
class ChangePasswordValidator(ResetPasswordValidator):
    old_password = PasswordField('原密码', validators=[DataRequired(message='不可为空')])


# 上传文件的校验(单个文件)
class UploadFileValidator(BaseValidator):
    # ref==> https://wtforms.readthedocs.io/en/latest/fields.html
    file = FileField()

    def validate_file(self, value):
        self.file.data = request.files[value.name]


class UploadPDFValidator(BaseValidator):
    origin = FileField(validators=[DataRequired()])
    comparer = FileField(validators=[DataRequired()])


# 配送地址的校验
class UpdateAddressValidator(BaseValidator):
    name = StringField(validators=[DataRequired()])
    mobile = StringField(validators=[
        DataRequired(),
        length(min=11, max=11, message='手机号为11个数字'),
        Regexp(r'^1(3|4|5|7|8)[0-9]\d{8}$')
    ])
    province = StringField(validators=[DataRequired()])
    city = StringField(validators=[DataRequired()])
    country = StringField(validators=[DataRequired()])
    detail = StringField(validators=[DataRequired()])


class PaginateValidator(BaseValidator):
    page = IntegerField(default=1)  # 当前页
    size = IntegerField(NumberRange(min=1, max=100), default=10)  # 每页条目个数

    def validate_page(self, value):
        self.page.data = int(value.data)

    def validate_size(self, value):
        self.size.data = int(value.data)
