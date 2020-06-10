# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/9.
"""
from functools import wraps
from flask import request

__author__ = 'Allen7D'

def apply_swagger(app):
    from flasgger import Swagger, LazyString
    from app.core.json_encoder import JSONEncoder as _JSONEncoder

    class JSONEncoder(_JSONEncoder):
        def default(self, obj):
            if isinstance(obj, LazyString):
                return str(obj)
            return super(JSONEncoder, self).default(obj)

    app.json_encoder = JSONEncoder

    # 访问swagger文档前自动执行(可以用于文档的安全访问管理)
    def before_access(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            return f(*args, **kwargs)

        return decorated

    def on_host():
        host = request.host
        if ',' in host:
            return host.split(',')[-1]
        return host

    swagger = Swagger(
        decorators=[before_access],
        template={
            'host': LazyString(on_host),  # Swagger请求的服务端地址
            'schemes': [LazyString(lambda: 'https' if request.is_secure else 'http')],  # 通信协议: http或https或多个
            'tags': app.config['SWAGGER_TAGS'],  # 接口在文档中的类别和顺序
        })
    swagger.init_app(app)


