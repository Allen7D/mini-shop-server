# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/10/25.
"""
__author__ = 'Allen7D'


class ParamFiled:
    def __init__(self, name, description, enum, required, default):
        self.name = name
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
        self.type = 'integer'
        self.site = 'query'
        super().__init__(name, description, enum, required, default)


class IntegerPathFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        self.type = 'integer'
        self.site = 'path'
        super().__init__(name, description, enum, required, default)


class StringQueryFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        self.type = 'string'
        self.site = 'query'
        super().__init__(name, description, enum, required, default)


class StringPathFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        self.type = 'string'
        self.site = 'path'
        super().__init__(name, description, enum, required, default)


class BooleanQueryFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        self.type = 'boolean'
        self.site = 'query'
        super().__init__(name, description, enum, required, default)


class BooleanPathFiled(ParamFiled):
    def __init__(self, name, description, enum=None, required=None, default=None):
        self.type = 'boolean'
        self.site = 'path'
        super().__init__(name, description, enum, required, default)


class ArrayQueryField():

    def __init__(self, name, description, item_type, enum, required, default):
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


class BodyFiled():
    '''Body'''

    def __init__(self, *args, description=''):
        self.args = args
        self.description = description

    @property
    def data(self):
        properties = {}
        for arg in self.args:
            if isinstance(arg, tuple):
                properties[arg[0]] = arg[1].data
            else:
                properties[arg.name] = arg.data

        return {
            "name": 'body',
            "in": 'body',
            "description": self.description,
            "schema": {
                "properties": properties
            }
        }


class BodyAttr():
    '''Body的参数'''

    def __init__(self, name, type, description, enum=None, default=None):
        self.name = name
        self.site = 'body'
        self.type = type
        self.description = description
        self.enum = enum
        self.default = default if default else enum[0]

    @property
    def data(self):
        return {
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
    path_fields = []
    query_fields = []
    body_fileds = []
    res_obj = {
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
        if site == 'path':
            path_fields.append(field.data)
        if site == 'query':
            query_fields.append(field.data)
        if site == 'body':
            body_fileds.append((field.name, field))
    res_obj['parameters'] = path_fields + query_fields
    if len(body_fileds) > 0:
        res_obj['parameters'].append(BodyFiled(*body_fileds, description=kwargs.get('description', '')).data)
    return res_obj

