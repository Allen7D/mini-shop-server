# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from functools import wraps
from flasgger import swag_from
from app.config.setting import specs_security
from app.libs.swagger_filed import init_specs

__author__ = 'Allen7D'


class RedPrint:
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

    def doc(self, *_args, **_kwargs):
        arg_name_list = _kwargs.get('args', [])  # 所有的请求参数(path、query、body)

        def decorator(f):
            if len(arg_name_list) > 0:
                request_args = [getattr(self.api_doc, arg_name) for arg_name in arg_name_list]
                specs = init_specs(*request_args, description=_kwargs.get('body_desc', ''))
            else:
                specs = getattr(self.api_doc, f.__name__, self.initial_specs)
            # 增加Token校验
            specs['security'] = specs_security if _kwargs.get('auth', False) else {}
            specs['tags'] = [self.tag['name']]
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
    def initial_specs(self):
        return {
            "parameters": [],
            "responses": {
                "200": {
                    "description": "",
                    "examples": {}
                }
            }
        }

    @property
    def tag(self):
        return {
            'name': self.alias if self.alias else self.name,
            'description': self.description
        }
