# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/28.
"""
from collections import namedtuple

from flask import request, _request_ctx_stack
from wtforms import Form as WTForm, ValidationError

from app.libs.error_code import ParameterException

__author__ = 'Allen7D'


class PropVelifyMixin(object):
    '''属性校验的方法集'''

    # 判断正整数
    def isPositiveInteger(self, value):
        try:
            value = int(value)
        except ValueError:
            return False
        return True if (isinstance(value, int) and value > 0) else False

    # 判断自然数
    def isNaturalNumber(self, value):
        try:
            value = int(value)
        except ValueError:
            return False
        return True if (isinstance(value, int) and value >= 0) else False

    # 判断数组
    def isList(self, value):
        return True if isinstance(value, list) else False

    # 判断空数组
    def isEmptyList(self, value):
        return True if self.isList(value) and len(value) == 0 else False


class BaseValidator(PropVelifyMixin, WTForm):
    def __init__(self):
        data = request.get_json(silent=True)  # body中
        # view_args = _request_ctx_stack.top.request.view_args  # path中，获取view中(path路径里)的args
        args = request.args.to_dict()  # query中
        super(BaseValidator, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseValidator, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self

    def get_data(self, *args):
        '''按次序获取通过参数校验的参数
        :param args: 要解析的参数名数组
        :return:
        '''
        order_list = []
        for arg in args:
            order_list.append(getattr(self._data, arg, None))
        return order_list[0] if len(args) else set(order_list)

    @property
    def dt_data(self):
        '''返回结果以dict的形式，常用于数据库相关操作'''
        return self._data._asdict()

    @property
    def nt_data(self):
        '''返回结果以namedtuple的形式，优化数据解析'''
        return self._data

    @property
    def _data(self):
        ''' 默认返回namedtuple，若是要返回dict则有validate_for_api决定
        :return:
        '''
        self.validate_for_api()
        key_list, value_list = [], []
        for key, value in self._fields.items():
            if value.data is not None:
                key_list.append(key)
                value_list.append(value.data)
        NamedTuple = namedtuple('NamedTuple', [key for key in key_list])
        return NamedTuple(*value_list)

    @staticmethod
    def get(key, default=None):
        data = BaseValidator.get_args_json(as_dict=True)
        try:
            rv = data[key]
        except KeyError:
            return default
        return rv

    @staticmethod
    def get_args_json(as_dict: bool = False):
        '''获取query和body中的所有参数'''
        data, args = request.get_json(silent=True), request.args.to_dict()
        args_json = dict(data, **args) if data is not None else args
        data = {
            key: value for key, value in args_json.items() if value is not None
        }
        if as_dict:
            return data
        return BaseValidator.__as_namedtuple(data)

    @staticmethod
    def get_view_args(as_dict: bool = False):
        '''获取所有的path中的数据'''
        view_args = _request_ctx_stack.top.request.view_args
        data = {
            key: value for key, value in view_args.items() if (value is not None and value != '')
        }
        if as_dict:
            return data
        return BaseValidator.__as_namedtuple(data)

    @staticmethod
    def __as_namedtuple(dict_obj):
        key_list, value_list = [], []
        for key, value in dict_obj.items():
            if value is not None:
                key_list.append(key)
                value_list.append(value)
        NamedTuple = namedtuple('NamedTuple', [key for key in key_list])
        return NamedTuple(*value_list)
