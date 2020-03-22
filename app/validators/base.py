# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/13.
"""
from flask import request, _request_ctx_stack
from wtforms import Form as WTForm, ValidationError

from app.libs.error_code import ParameterException

__author__ = 'Allen7D'


class BaseValidator(WTForm):
    def __init__(self):
        data = request.get_json(silent=True)  # body中
        # view_args = _request_ctx_stack.top.request.view_args  # 获取view中(path路径里)的args
        args = request.args.to_dict()  # query中: request.args.to_dict()
        super(BaseValidator, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseValidator, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

    @property
    def data(self):
        return {
            key: value.data for key, value in self._fields.items() if value.data is not None
        }

    def get_all_json(self):
        data, args = request.get_json(silent=True), request.args.to_dict()
        args_json = dict(data, **args) if data is not None else args
        return {
            key: value for key, value in args_json.items() if value is not None
        }

    def get_query_json(self):
        args_json = request.args.to_dict()
        return {
            key: value for key, value in args_json.items() if value is not None
        }

    def get_body_json(self):
        args_json = request.get_json(silent=True)
        return {
            key: value for key, value in args_json.items() if value is not None
        }

    def isPositiveInteger(self, value):
        try:
            value = int(value)
        except ValueError:
            return False
        return True if (isinstance(value, int) and value > 0) else False

    def isList(self, value):
        return True if isinstance(value, list) else False

    def isEmptyList(self, value):
        return True if self.isList(value) and len(value) == 0 else False
