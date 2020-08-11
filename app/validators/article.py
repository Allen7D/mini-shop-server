# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/8/11.
  Article相关的参数校验
"""

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

from app.core.validator import BaseValidator

__author__ = 'Allen7D'


class ArticleTypeValidator(BaseValidator):
    type = IntegerField('文章类型', validators=[
        NumberRange(min=0, max=2, message='文章类型必须0, 1, 2'),
    ], default=0)


class ArticleValidator(BaseValidator):
    author_id = IntegerField()
    type = IntegerField('文章类型', validators=[
        NumberRange(min=0, max=2, message='文章类型必须0, 1, 2')
    ], default=0)
    title = StringField(validators=[DataRequired()])
    summary = StringField()
    content = StringField()
    img = StringField()
    theme = IntegerField()
    views = IntegerField()
