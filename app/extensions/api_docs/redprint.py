# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from functools import wraps

from flasgger import swag_from

from app.core.redprint import Redprint as _Redprint
from app.core.swagger_filed import SwaggerSpecs
from app.core.logger import Logger
from app.libs.enums import OperTyepEnum

__author__ = 'Allen7D'


class Redprint(_Redprint):
    def __init__(self, name, module, description='', api_doc=None, alias=''):
        '''
        :param name: 接口名称(英文)
        :param module: 接口模块名(接口中文名称)
        :param description: 接口描述
        :param api_doc: 接口的文档模块
        :param alias: 接口的别名
        '''
        self.alias = alias  # 接口的别名
        self.description = description if description else module
        self.api_doc = api_doc
        super(Redprint, self).__init__(name, module)

    @property
    def tag(self):
        return {
            'name': self.alias if self.alias else self.name,
            'description': self.description
        }

    def doc(self, args: list = [], auth: bool = False, body_desc: str = None):
        '''应该对args分批处理, path, query, body'''

        def decorator(f):
            if hasattr(self.api_doc, f.__name__):
                # 若swagger备注用函数名
                specs = getattr(self.api_doc, f.__name__)
                if not isinstance(specs, dict):
                    raise TypeError('{} must be dict'.format(f.__name__))
                specs['tags'] = [self.tag['name']]
            else:
                specs = SwaggerSpecs(args=args, api_doc=self.api_doc, body_desc=body_desc, auth=auth,
                                     tags=[self.tag['name']]).specs
            # 对f.__doc__处理
            if f.__doc__ and '\n' in f.__doc__:
                f.__doc__ = f.__doc__.split('\n')[0]

            # swag_from将specs注入到swagger实例(单例)中
            @swag_from(specs=specs)
            @wraps(f)
            def wrapper(*args, **kwargs):
                return f(*args, **kwargs)

            return wrapper

        return decorator

    def log(self, template=None, type=OperTyepEnum.OTHER):
        return Logger(module=self.module, template=template, type=type)
