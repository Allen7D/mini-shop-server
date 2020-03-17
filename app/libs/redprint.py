# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from functools import wraps
from flasgger import swag_from
from app.config.setting import specs_security
from app.libs.swagger_filed import init_specs
from app.api_docs import global_args as global_args_module

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
        arg_path_name_list = _kwargs.get('args', [])  # 所有的请求参数(path、query、body)

        def decorator(f):
            if len(arg_path_name_list) > 0:
                request_args = self.__load_arg(arg_path_name_list)
                specs = init_specs(*request_args, body_desc=_kwargs.get('body_desc', ''))
            else:
                args_module = self.api_doc
                specs = getattr(args_module, f.__name__, init_specs())
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
    def tag(self):
        return {
            'name': self.alias if self.alias else self.name,
            'description': self.description
        }

    def __load_arg(self, arg_path_name_list):
        request_arg_list = []
        for arg_path_name in arg_path_name_list:
            # arg_path_name是参数的路径'g.query.id'
            arg_path = arg_path_name.split('.')
            arg_name = _get_request_arg_name(last_arg_path=arg_path[-1])  # 请求参数名
            arg_site, args_module = self.__get_args_module(arg_path_name)

            request_arg = _get_request_arg(arg_name, arg_site, args_module)
            request_arg = _set_request_arg_required(request_arg, arg_path[-1])
            request_arg_list.append(request_arg)
        return request_arg_list

    def __get_args_module(self, arg_path_name):
        '''
        :param arg_path_name: 路径名(g.query.id 或者 query.id 或者 id)
        :return: arg_site: 请求参数的位置: path、query、body
                 args_module: 参数的模块(global_args or self.api_doc)
        '''
        arg_path_list = arg_path_name.split('.')
        if arg_path_name.startswith('g.'):
            arg_site = arg_path_list[1]
            args_module = global_args_module
        elif len(arg_path_list) == 2:
            arg_site = arg_path_list[0]
            args_module = self.api_doc
        else:
            arg_site = None
            args_module = self.api_doc
        return arg_site, args_module


def _set_request_arg_required(request_arg, last_arg_path):
    ''' 判断last_arg_path是否带有「+」或「-」，设置request_arg.required状态
    「+」加required
    「-」去required
        否则保持required不变
    :param request_arg: 请求的参数
    :param last_arg_path: 请求路径的最后字段(可能是id 或 id+ 或 id-)
    :return: request_arg
    '''
    if last_arg_path.endswith('+'):
        request_arg.required = True
    if last_arg_path.endswith('-'):
        request_arg.required = False
    return request_arg


def _get_request_arg(arg_name, arg_site, args_module):
    '''
    :param arg_name: 请求参数名
    :param arg_site: 请求参数的位置: path、query、body
    :param args_module: 参数的模块(global_args or self.api_doc)
    :return:
    '''
    if not arg_site:
        return getattr(args_module, arg_name)
    # 判断是有_in_的参数
    try:
        # 从args_module中导入「x_in_y」变量
        return getattr(args_module, '{}_in_{}'.format(arg_name, arg_site))
    except AttributeError as e:
        # 从args_module中导入「x」变量
        return getattr(args_module, arg_name)

def _get_request_arg_name(last_arg_path):
    '''
    :param last_arg_path: 参数名
    :return:
    '''
    if last_arg_path.endswith('+'):
        arg_name = last_arg_path.split('+')[0]
    elif last_arg_path.endswith('-'):
        arg_name = last_arg_path.split('-')[0]
    else:
        arg_name = last_arg_path
    return arg_name
