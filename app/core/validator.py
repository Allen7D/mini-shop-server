# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/28.
"""
from collections import namedtuple

from flask import request
from wtforms import Form as WTForm

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
        :return: 单个数据 或 有序的元祖
        '''
        order_list = []
        for arg in args:
            order_list.append(getattr(self._data, arg, None))
        return order_list[0] if len(order_list) == 1 else tuple(order_list)

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
