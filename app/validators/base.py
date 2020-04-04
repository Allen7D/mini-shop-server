# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/13.
"""
from collections import namedtuple

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

    def validate_for_api(self, as_dict=False):
        '''
        :param as_dict: 是否将data属性转为dict类型，结合data属性使用
        :return: self
        '''
        self.as_dict = as_dict
        valid = super(BaseValidator, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

    @property
    def data(self):
        key_list, value_list = [], []
        for key, value in self._fields.items():
            if value.data is not None:
                key_list.append(key)
                value_list.append(value.data)
        NamedTuple = namedtuple('NamedTuple', [key for key in key_list])
        nt = NamedTuple(*value_list)
        return nt._asdict() if self.as_dict else nt

    @staticmethod
    def get(key, default=None):
        data = BaseValidator.get_all_json()
        try:
            rv = data[key]
        except KeyError:
            return default
        return rv

    @staticmethod
    def get_all_json():
        data, args = request.get_json(silent=True), request.args.to_dict()
        args_json = dict(data, **args) if data is not None else args
        return {
            key: value for key, value in args_json.items() if value is not None
        }

    @staticmethod
    def get_query_json():
        args_json = request.args.to_dict()
        return {
            key: value for key, value in args_json.items() if value is not None
        }

    @staticmethod
    def get_body_json():
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
