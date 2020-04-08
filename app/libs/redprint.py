# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from functools import wraps
from collections import namedtuple

from flasgger import swag_from

from app.libs.swagger_filed import SwaggerSpecs

__author__ = 'Allen7D'
# 路由函数的权限和模块信息(meta信息)
# name 权限名；module 权限所属模块
Meta = namedtuple('meta', ['name', 'module'])
route_meta_infos = {}


class RedPrint(object):
    name_list = ()  # 存放所有rp的name, 避免重复

    def __init__(self, name, description, api_doc=None, alias=''):
        self.name = name
        self.alias = alias  # 接口的别名
        self.description = description
        self.mound = []
        self.api_doc = api_doc

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

    def route_meta(self, auth: str, module: str = 'common', mount: bool = True):
        def wrapper(f):
            if mount:
                name = f.__name__ + str(f.__hash__())
                existed = route_meta_infos.get(name, None) and route_meta_infos.get(name).module == module
                if existed:
                    raise Exception("视图函数(f)名不能重复出现在同一个模块(module)中")
                else:
                    route_meta_infos.setdefault(name, Meta(auth, module))
            return f

        return wrapper

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
            if f.__doc__ and '\n\t' in f.__doc__:
                f.__doc__ = f.__doc__.split('\n\t')[0]

            # swag_from将specs注入到swagger实例(单例)中
            @swag_from(specs=specs)
            @wraps(f)
            def wrapper(*args, **kwargs):
                return f(*args, **kwargs)

            return wrapper

        return decorator

    @property
    def tag(self):
        return {
            'name': self.alias if self.alias else self.name,
            'description': self.description
        }
