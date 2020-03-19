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
        self.type = type # type的类型: string、integer、boolean
        self.description = description
        self.enum = enum
        self.default = default if default else enum[0]

    @property
    def data(self):
        return {
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "enum": self.enum,
            "default": self.default
        }


def inject(*args, **kwargs):
    # 使用kwargs应该也可以接受 自定义的dict
    def decorator(f):
        return init_specs(*args, **kwargs)

    return decorator


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
