# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/3.
"""
from app.libs.blueprint import Blueprint

__author__ = 'Allen7D'


def create_blueprint_list(app):
    '''
    :param app: flask实例
    :return: (url_prefix, bp) ('/api/v1', v1)
    '''
    api_modules = {}
    for rp_api in app.config['ALL_RP_API_LIST']:
        [module_name, api_name] = rp_api.split('.')
        api = _import_redprint(module_name, api_name)
        app.config['SWAGGER_TAGS'].append(api.tag)
        # 将「红图列表」注册到蓝图中
        if module_name not in api_modules.keys():
            bp = Blueprint(module_name, '{}.{}'.format(__name__, module_name))
            api_modules.setdefault(module_name, bp)
        else:
            bp = api_modules.get(module_name)
        api.register(bp)
    return [('/api/{}'.format(module_name), bp) for module_name, bp in api_modules.items()]


def _import_redprint(module_name, api_name):
    """
    :param module_name: string: 红图的版本:'cms', 'v1'
    :param api_name: string: 红图的名称: 'token', 'user', ...
    :return: 红图列表
    """
    # __import__的参数level的取值：「等于0」绝对路径；「大于0」为相对路径
    # 当level=1，相对路径是从当前文件所在目录开始
    # 当level=1, module_name为'v1'时，module为 'app.api.v1'
    module = __import__('{}.{}'.format(module_name, api_name), globals(), fromlist=("***"), level=1)
    # 当level=0, 绝对路径必须从app目录开始
    # 当level=0, module_name为'app.api.v1'时，module为 'app.api.v1'
    # module = __import__('app.api.{}'.format(module_name), globals(), fromlist=('***'), level=0)
    api = getattr(module, 'api')
    return api
