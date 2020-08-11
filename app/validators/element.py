# -*- coding: utf-8 -*-
"""
  Created by Chai on 2020/7/13.
  Element相关的参数校验
"""
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, ValidationError

from app.core.validator import BaseValidator

__author__ = 'Chai'


class ElementValidator(BaseValidator):
    name = StringField(validators=[DataRequired()])
    sign = StringField(validators=[DataRequired()])
    route_id = IntegerField(validators=[DataRequired()])


class Group2ElementValidator(BaseValidator):
    group_id = IntegerField(validators=[DataRequired()])
    element_ids = IntegerField(validators=[DataRequired()])

    def validate_element_ids(self, value):
        ids = value.data.split(',')
        for id in ids:
            if not self.isPositiveInteger(id):
                raise ValidationError(message='ids 必须是用「,」分隔的正整数列')
        self.element_ids.data = list(map(lambda x: int(x), ids))


class RouteIdValidator(BaseValidator):
    route_id = IntegerField(validators=[DataRequired()])
