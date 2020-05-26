# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/10/25.
"""

__author__ = 'Allen7D'


class ParamFiled:
    def __init__(self, name, site, type, description, enum, required=None, default=None):
        self.name = name
        self.site = site
        self.type = type
        self.description = description
        self.enum = enum
        self.required = required
        self.default = default if default else (enum[0] if enum else None)

    @property
    def data(self):
        return {
            "name": self.name,
            "in": self.site,
            "type": self.type,
            "description": self.description,
            "enum": self.enum,
            "required": self.required,
            "default": self.default
        }


class IntegerQueryFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        super().__init__(name, 'query', 'integer', description, enum, required, default)


class IntegerPathFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        super().__init__(name, 'path', 'integer', description, enum, required, default)


class StringQueryFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        super().__init__(name, 'query', 'string', description, enum, required, default)


class StringPathFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        super().__init__(name, 'path', 'string', description, enum, required, default)


class BooleanQueryFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        super().__init__(name, 'query', 'boolean', description, enum, required, default)


class BooleanPathFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        super().__init__(name, 'path', 'boolean', description, enum, required, default)


class ArrayQueryField():

    def __init__(self, name, description, item_type, enum=None, required=None, default=None):
        self.name = name
        self.site = 'query'
        self.item_type = item_type
        self.description = description
        self.enum = enum
        self.required = required
        self.default = default

    @property
    def items(self):
        return {
            'type': self.item_type,
            'enum': self.enum,
            'default': self.default
        }

    @property
    def data(self):
        return {
            'name': self.name,
            "in": "query",
            "description": self.description,
            "required": self.required,
            "type": "array",
            "items": self.items
        }


class RequestBody():
    '''请求体'''

    def __init__(self, *args, description=''):
        self.args = args
        self.description = description

    @property
    def data(self):
        properties = {}
        for arg in self.args:
            properties[arg['name']] = arg

        return {
            "name": 'body',
            "in": 'body',
            "description": self.description,
            "schema": {
                "properties": properties
            }
        }


class BodyField():
    '''Body中的参数'''

    def __init__(self, name, type, description, enum=None, default=None):
        self.name = name
        self.site = 'body'
        self.type = type  # type的类型: string、integer、boolean, array
        self.description = description
        self.enum = enum
        self.default = default if default else enum[0]

    @property
    def data(self):
        data_dict = {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "enum": self.enum,
            "default": self.default
        }
        if self.type in ('array'):
            data_dict['type'] = 'list'
            data_dict['items'] = self.default
        return data_dict


def inject(*args, **kwargs):
    # 使用kwargs应该也可以接受 自定义的dict
    def decorator(f):
        return SwaggerSpecs.init_specs(*args, **kwargs)

    return decorator


class SwaggerSpecs():
    '''每个路由的specs，其包含path、query、body中的多个参数'''

    def __init__(self, args=[], auth=False, tags=[], api_doc=None, body_desc=None):
        self.whole_args = []
        self.simple_args = []  # *开头的
        self.auth = auth
        self.tags = tags  # 必填
        self.api_doc = api_doc
        self.body_desc = body_desc
        for arg in args:
            if arg.startswith('*'):
                arg = arg.split('*')[1]  # 去掉*
                self.simple_args.append(arg)
            else:
                self.whole_args.append(arg)

    @property
    def security(self):
        if self.auth:
            return [{"basicAuth": []}]
        return []

    @property
    def arg_fields(self):
        '''解析出args'''
        whole_arg_fields = self.parse_whole_args(self.whole_args)
        simple_arg_fields = self.parse_simple_args(self.simple_args)
        return whole_arg_fields + simple_arg_fields

    @property
    def specs(self):
        _specs = self.init_specs(*self.arg_fields, body_desc=self.body_desc)
        _specs['tags'] = self.tags
        _specs['security'] = self.security
        _specs['responses'] = {
            "200": {
                "description": "",
                "examples": {}
            }
        }
        return _specs

    def parse_whole_args(self, arg_src_list):
        arg_fields = []
        for arg_src in arg_src_list:
            # arg_path_name是参数的路径'g.query.id'
            request_arg = WholeArg(arg_src, api_doc=self.api_doc).data
            arg_fields.append(request_arg)
        return arg_fields

    def parse_simple_args(self, arg_src_list):
        '''
        校验数据格式必须是3个
            第2个是数据类型: int、str、bool, arr
            第3个是数据位置: body、query、path
        :param arg_src_list: 'str.path.id'
        :return:
        '''
        arg_fields = []
        for arg_src in arg_src_list:
            arg_type, arg_site, arg_name = arg_src.split('.')
            arg = SimpleArg(name=arg_name, abbr_type=arg_type, site=arg_site).data
            arg_fields.append(arg)
        return arg_fields

    @staticmethod
    def init_specs(*args, **kwargs):
        path_fields, query_fields, body_fields = [], [], []
        specs_obj = {
            "parameters": [],
            "responses": {
                "200": {
                    "description": "",
                    "examples": {}
                }
            }
        }
        for field in args:
            site = field.site
            if site in ('path', 'query', 'body'):
                fields = locals()['{}_fields'.format(site)]
                fields.append(field.data)
        specs_obj['parameters'] = path_fields + query_fields
        if len(body_fields) > 0:
            specs_obj['parameters'].append(
                RequestBody(*body_fields, description=kwargs.get('body_desc', '')).data
            )
        return specs_obj


class WholeArg():
    def __init__(self, arg_src, api_doc):
        '''
        :param arg_src: 路径名(g.query.id 或者 query.id 或者 id)
        :param api_doc:
        '''
        self.arg_src = arg_src
        self.api_doc = api_doc

    @property
    def is_global(self):
        return self.arg_src.startswith('g.')

    @property
    def arg_src_list(self):
        return self.arg_src.split('.')

    @property
    def arg_name(self):
        _arg_name = self.arg_src_list[-1]  # 按.切分后的最后的元素，_arg_name末尾可能带'+'或'-'
        if _arg_name.endswith(('+', '-')):
            _arg_name = _arg_name[:-1]  # 不要'+'或'-'
        return _arg_name

    @property
    def arg_required(self):
        if self.arg_src.endswith('+'):
            return True
        elif self.arg_src.endswith('-'):
            return False
        return False

    @property
    def arg_site(self):
        '''
        :return: arg_site: 请求参数的位置: path、query、body
        '''
        if self.is_global:
            _arg_site = self.arg_src_list[1]  # g.path.id
        elif len(self.arg_src_list) == 2:
            _arg_site = self.arg_src_list[0]  # path.id
        else:
            _arg_site = None  # id
        return _arg_site

    @property
    def args_module(self):
        '''
        :return: args_module: 参数的模块(global_args or self.api_doc)
        '''
        from app.extensions.api_docs import global_args as global_args_module
        return global_args_module if self.is_global else self.api_doc

    @property
    def data(self):
        if not self.arg_site:
            _arg_field = getattr(self.args_module, self.arg_name)
        # 判断是有_in_的参数
        try:
            # 从args_module中导入「x_in_y」变量
            _arg_field = getattr(self.args_module, '{}_in_{}'.format(self.arg_name, self.arg_site))
        except AttributeError as e:
            # 从args_module中导入「x」变量
            _arg_field = getattr(self.args_module, self.arg_name)
        _arg_field = self.set_required(_arg_field)
        return _arg_field

    def set_required(self, arg_field):
        ''' 判断arg_src是否带有「+」或「-」，arg_field.required状态
            「+」加required;「-」去required; 否则保持required不变
        '''
        if self.arg_src.endswith(('+', '-')):
            arg_field.required = self.arg_required
        return arg_field


class SimpleArg():
    def __init__(self, name, abbr_type, site):
        '''
        :param name: 参数名
        :param abbr_type: 参数类型缩写('int', 'str', 'bool', 'arr')
        :param site: 参数位置: ('path', 'query', 'body')
        '''
        self.name = name
        self.abbr_type = abbr_type
        if site not in ('path', 'query', 'body'):
            raise ValueError('请求位置:{} 错误，应该为path, query, body位置选项'.format(site))
        self.site = site

    @property
    def type(self):
        if self.abbr_type not in ('int', 'str', 'bool', 'arr'):
            raise ValueError('参数类型:{} 错误，应该为int, str, bool类型选项'.format(self.abbr_type))
        type_dict = {'int': 'integer', 'str': 'string', 'bool': 'boolean', 'arr': 'array'}
        return type_dict[self.abbr_type]

    @property
    def enum(self):
        enum_dict = {
            'int': [1, 2, 3, 4, 5, 10, 100, 0],
            'str': ['***', '???'],
            'bool': [True, False],
            'arr': [['a', 'b', 'c'], [1, 2, 3]]
        }
        return enum_dict[self.abbr_type]

    @property
    def data(self):
        if self.site in ('path', 'query'):
            return ParamFiled(self.name, self.site, self.type, '', self.enum, False)
        else:
            # self.site == 'body'
            return BodyField(self.name, self.type, '', self.enum)
