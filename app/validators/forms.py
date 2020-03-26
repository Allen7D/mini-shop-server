# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
  各种提交表单的验证
"""

from flask import request
from wtforms import StringField, IntegerField, PasswordField, FileField, MultipleFileField, FieldList
from wtforms.validators import DataRequired, length, Email, Regexp, EqualTo, Optional, ValidationError, NumberRange

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseValidator

__author__ = 'Allen7D'


########## 基础公用的参数校验器 ##########
class IDMustBePositiveIntValidator(BaseValidator):
    id = IntegerField(validators=[DataRequired()])

    def validate_id(self, value):
        id = value.data
        if not self.isPositiveInteger(id):
            raise ValidationError(message='ID 必须为正整数')
        self.id.data = id


class IDCollectionValidator(BaseValidator):
    ids = StringField(validators=[DataRequired()])

    def validate_ids(self, value):
        ids = value.data.split(',')
        for id in ids:
            if not self.isPositiveInteger(id):
                raise ValidationError(message='ids 必须是用「,」分隔的正整数列')
        self.ids.data = list(map(lambda x: int(x), ids))


class PaginateValidator(BaseValidator):
    page = IntegerField(default=1)  # 当前页
    size = IntegerField(NumberRange(min=1, max=100), default=10)  # 每页条目个数

    def validate_page(self, value):
        self.page.data = int(value.data)

    def validate_size(self, value):
        self.size.data = int(value.data)


########## 登录相关 ##########
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


########## 权限管理相关 ##########
# 注册管理员校验
class CreateAdminValidator(BaseValidator):
    password = PasswordField('新密码', validators=[
        DataRequired(message='新密码不可为空'),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message='密码长度必须在6~22位之间，包含字符、数字和 _ '),
        EqualTo('confirm_password', message='两次输入的密码不一致，请输入相同的密码')
    ])
    confirm_password = PasswordField('确认新密码', validators=[DataRequired(message='请确认密码')])
    nickname = StringField(validators=[DataRequired(message='用户名不可为空'),
                                       length(min=2, max=10, message='用户名长度必须在2~10之间')])

    group_id = IntegerField('分组id',
                            validators=[DataRequired(message='请输入分组id'), NumberRange(message='分组id必须大于0', min=1)])
    email = StringField('电子邮件', validators=[
        Regexp(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$', message='电子邮箱不符合规范，请输入正确的邮箱'),
        Optional()
    ])
    mobile = StringField(validators=[
        length(min=11, max=11, message='手机号为11个数字'),
        Regexp(r'^1(3|4|5|7|8)[0-9]\d{8}$'),
        Optional()
    ])


class UpdateAdminValidator(BaseValidator):
    group_id = IntegerField('权限组id',
                            validators=[DataRequired(message='请输入分组id'), NumberRange(message='分组id必须大于0', min=1)])


# 管理员更新分组
class UpdateGroupValidator(BaseValidator):
    # 分组name
    name = StringField(validators=[DataRequired(message='请输入分组名称')])
    # 非必须
    info = StringField(validators=[Optional()])


# 权限组的权限更新
class AuthsValidator(BaseValidator):
    group_id = IntegerField('权限组id',
                            validators=[DataRequired(message='请输入分组id'), NumberRange(message='分组id必须大于0', min=1)])
    auth_ids = FieldList(IntegerField(validators=[DataRequired(message='请输入auths字段')]))


########## 用户相关 ##########
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


########## 商品相关 ##########
class CountValidator(BaseValidator):
    count = IntegerField(default='15')  # 默认为15，可以省略 DataRequired()

    def validate_count(self, value):
        count = value.data
        if not self.isPositiveInteger(count) or not (1 <= int(count) <= 15):
            raise ValidationError(message='count必须是[1, 15]区间内 的正整数')
        self.count.data = int(count)


########## 订单相关 ##########
class OrderPlaceValidator(BaseValidator):
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


########## 上传相关 ##########
# 上传文件的校验(单个文件)
class UploadFileValidator(BaseValidator):
    # ref==> https://wtforms.readthedocs.io/en/latest/fields.html
    file = FileField()

    def validate_file(self, value):
        self.file.data = request.files[value.name]


# 上传文件的校验(两个文件)
class UploadPDFValidator(BaseValidator):
    origin = FileField(validators=[DataRequired()])
    comparer = FileField(validators=[DataRequired()])
