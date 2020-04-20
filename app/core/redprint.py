# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/9.
  Redprint 红图
  RedprintAssigner 红图分派者(生成蓝图)
"""
from functools import namedtuple
from importlib import import_module
from flask import Blueprint

__author__ = 'Allen7D'

# 路由函数的权限和模块信息(meta信息)
# name 权限名；module 权限所属模块
Meta = namedtuple('meta', ['name', 'module'])
route_meta_infos = {}


class Redprint(object):
    def __init__(self, name):
        self.name = name
        self.mound = []

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


class RedprintAssigner():
    '''红图分派者，将红图分配给各自所属于的蓝图'''

    def __init__(self, app, rp_api_list):
        self.app = app
        self.api_path = self.app.config['API_PATH']  # 默认是app.api
        self.rp_api_list = rp_api_list
        self.handle_callback_list = []  # 处理红图的回调函数列表

    def create_bp_list(self):
        return self.__create_blueprint_list()

    # 装饰器的用法
    # 用于处理红图的回调函数，便于其外部扩展
    def handle_rp(self, f):
        self.handle_callback_list.append(f)
        return f

    # 依次执行红图的回调函数
    def __run_callback_list(self, api):
        for handle_callback in self.handle_callback_list:
            handle_callback(api)

    def __create_blueprint_list(self):
        '''
        :return: (url_prefix, bp) ('/v1', v1)
        '''
        api_modules = {}
        for rp_api in self.rp_api_list:
            [module_name, api_name] = rp_api.split('.')
            api = self.__import_redprint(module_name, api_name)
            # 将「红图列表」注册到蓝图中
            if module_name not in api_modules.keys():
                bp = Blueprint(module_name, '{}.{}'.format(self.api_path, module_name))
                api_modules.setdefault(module_name, bp)
            else:
                bp = api_modules.get(module_name)
            api.register(bp)
        return [('/{}'.format(module_name), bp) for module_name, bp in api_modules.items()]

    def __import_redprint(self, module_name, api_name):
        """
        :param module_name: string: 红图的版本:'cms', 'v1'
        :param api_name: string: 红图的名称: 'token', 'user', ...
        :return: 红图列表
        """
        module = import_module('{}.{}.{}'.format(self.api_path, module_name, api_name))
        api = getattr(module, 'api')
        # 依次执行红图的回调函数
        self.__run_callback_list(api)
        return api
