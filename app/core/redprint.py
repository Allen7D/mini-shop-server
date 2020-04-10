# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/9.
"""
from sqlalchemy.util import namedtuple

__author__ = 'Allen7D'

# 路由函数的权限和模块信息(meta信息)
# name 权限名；module 权限所属模块
Meta = namedtuple('meta', ['name', 'module'])
route_meta_infos = {}


class RedPrint(object):
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
