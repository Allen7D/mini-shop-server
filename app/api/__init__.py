# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/3.
"""
from app.libs.blueprint import Blueprint

__author__ = 'Allen7D'


def create_blueprint_list(app):
    bp_list = []
    for module_name, api_name_list in app.config['ALL_API_BY_MODULE'].items():
        rp_list = _import_redprint(module_name, api_name_list)
        app.config['SWAGGER_TAGS'].extend([api.tag for api in rp_list])
        # 将「红图列表」注册到蓝图中
        bp = Blueprint(module_name, '{}.{}'.format(__name__, module_name))
        bp.register_redprint_list(rp_list)
        url_prefix = '/{}'.format(module_name)
        bp_list.append((url_prefix, bp))
    return bp_list


def _import_redprint(module_name, api_name_list):
    """
    :param module_name: string: 红图的版本:'cms', 'v1'
    :param api_name_list: list: 红图名的列表: ['token', 'user', ...]
    :return: 红图列表
    """
    rp_list = []
    for api_name in api_name_list:
        # __import__的参数level的取值：「等于0」绝对路径；「大于0」为相对路径
        # 当level=1，相对路径是从当前文件所在目录开始
        # 当level=1, module_name为'v1'时，module为 'app.api.v1'
        module = __import__('{}.{}'.format(module_name, api_name), globals(), fromlist=("***"), level=1)
        # 当level=0, 绝对路径必须从app目录开始
        # 当level=0, module_name为'app.api.v1'时，module为 'app.api.v1'
        # module = __import__('app.api.{}'.format(module_name), globals(), fromlist=('***'), level=0)
        api = getattr(module, 'api')
        rp_list.append(api)
    return rp_list
