# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
  print输出字体颜色: https://www.cnblogs.com/easypython/p/9084426.html
"""
import os
import json
import time
from functools import wraps
from importlib import import_module

from werkzeug.exceptions import HTTPException
from flask import Flask, redirect, url_for, g, request, _request_ctx_stack, current_app, render_template

from app.core.db import db
from app.core.json_encoder import JSONEncoder
from app.core.redprint import RedprintAssigner, route_meta_infos
from app.core.error import APIException, ServerError

__author__ = 'Allen7D'


def create_app():
    # 默认template_folder值就是'./templates'
    app = Flask(__name__, static_folder="./static", template_folder="./templates")

    load_config(app)
    register_blueprint(app)
    register_plugin(app)

    return app


def load_config(app):
    if os.environ.get('ENV_MODE') == 'dev:local':
        app.config.from_object('app.config.local_secure')
        app.config.from_object('app.config.local_setting')
    else:
        app.config.from_object('app.config.secure')
        app.config.from_object('app.config.setting')

    app.config.from_object('app.extensions.file.config')


def register_blueprint(app):
    '''注册蓝图'''
    app.config.from_object('app.extensions.api_docs.config')
    assigner = RedprintAssigner(app=app, rp_api_list=app.config['ALL_RP_API_LIST'])

    # 将红图的每个api的tag注入SWAGGER_TAGS中
    @assigner.handle_rp
    def handle_swagger_tag(api):
        app.config['SWAGGER_TAGS'].append(api.tag)

    bp_list = assigner.create_bp_list()
    for url_prefix, bp in bp_list:
        app.register_blueprint(bp, url_prefix=url_prefix)
    mount_route_meta_to_endpoint(app)
    load_endpint_infos(app)


def load_endpint_infos(app):
    """
    返回权限管理中的所有视图函数的信息，包含它所属module
    :return:
    """
    infos = {}
    index = 0
    for ep, meta in app.config['EP_META'].items():
        index += 1
        # 此处的id仅作为Vue的v-for使用，无实际意义
        endpint_info = {'id': index, 'name': meta.name, 'module': meta.module}
        module = infos.get(meta.module, None)
        #  infos是否已经存在该module
        if module:
            module.append(endpint_info)
        else:
            infos[meta.module] = [endpint_info]
        app.config['EP_INFO_LIST'].append(endpint_info)
    app.config['EP_INFOS'] = infos
    return infos


def mount_route_meta_to_endpoint(app):
    '''
    将route_mate挂载到对应的endpoint上
    :param app:
    :return:
    '''
    for endpoint, func in app.view_functions.items():
        info = route_meta_infos.get(func.__name__ + str(func.__hash__()), None)
        if info:
            app.config['EP_META'].setdefault(endpoint, info)


def register_plugin(app):
    apply_json_encoder(app)  # JSON序列化
    apply_cors(app)  # 应用跨域扩展，使项目支持请求跨域
    connect_db(app)  # 连接数据库
    handle_error(app)  # 统一处理异常

    # Debug模式(以下为非必选应用，且用户不可见)
    if app.config['DEBUG']:
        apply_request_log(app)  # 打印请求日志
        apply_default_view(app)  # 应用默认路由
        apply_orm_admin(app)  # 应用flask-admin, 可以进行简易的 ORM 管理
        apply_swagger(app)  # 应用flassger, 可以查阅Swagger风格的 API文档


def apply_json_encoder(app):
    app.json_encoder = JSONEncoder


def apply_cors(app):
    from flask_cors import CORS
    cors = CORS()
    cors.init_app(app, resources={"/*": {"origins": "*"}})


def connect_db(app):
    db.init_app(app)
    #  初始化使用
    with app.app_context():  # 手动将app推入栈
        db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表


def apply_default_view(app):
    @app.route('/')
    def index():
        '''跳转到「首页」'''
        url = {
            'github': current_app.config['GITHUB_URL'],
            'doc': current_app.config['DOC_URL'],
        }
        return render_template("index.html", url=url)

    @app.route('/doc')
    def doc():
        '''跳转到「api文档」'''
        return redirect('/apidocs/#/')

    apply_error_code_view(app)


def apply_orm_admin(app):
    from flask_admin import Admin
    from app.extensions.orm_admin.base import ModelView
    # 配置config
    app.config.from_object('app.extensions.orm_admin.config')

    object_origins = {}
    for module, items in app.config['ALL_MODEL_BY_MODULE'].items():
        for item in items:
            object_origins[item] = module

    admin = Admin(name='商城后台', template_mode='bootstrap3')
    for model_name, module_name in object_origins.items():
        model_module = import_module('app.models.{}'.format(module_name))
        model = getattr(model_module, model_name)
        try:
            # model_view_module 可能不存在
            model_view_module = import_module('app.extensions.orm_admin.model_views.{}'.format(module_name))
            model_view = getattr(model_view_module, '{}View'.format(model_name), ModelView)
        except ModuleNotFoundError as e:
            model_view = ModelView
        # admin添加model_view
        # endpoint & url有默认值，也可以随意修改
        lower_model_name = model_name.lower()
        admin.add_view(model_view(model, db.session,
                                  endpoint='admin.{}'.format(lower_model_name),
                                  url='/admin/{}'.format(lower_model_name)))

    apply_file_admin(admin)
    admin.init_app(app)


def apply_file_admin(admin):
    # Admin添加文件管理系统
    from flask_admin.contrib.fileadmin import FileAdmin
    import os.path as op
    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name='静态资源'))


def apply_error_code_view(app):
    def load_exception():
        module = import_module('app.libs.error_code')
        exception_list = []
        for elem_name in dir(module):
            elem = getattr(module, elem_name)
            if type(elem) == type and issubclass(elem, APIException):
                exception_list.append(elem())
        exception_list.sort(key=lambda x: x.error_code)
        return exception_list

    exception_list = load_exception()

    @app.route('/error_code')
    def error_code():
        return render_template('error_code.html', exception_list=exception_list)


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


def apply_request_log(app):
    @app.before_request
    def request_cost_time():
        g.request_start_time = time.time()
        g.request_time = lambda: "%.5f" % (time.time() - g.request_start_time)

    @app.after_request
    def log_response(res):
        message = '[%s] -> [%s] from:%s costs:%.3f ms' % (
            request.method,
            request.path,
            request.remote_addr,
            float(g.request_time()) * 1000
        )
        req_body = request.get_json() if request.get_json() else {}
        data = {
            'path': _request_ctx_stack.top.request.view_args,
            'query': request.args,
            'body': req_body
        }
        message += '\n\"data\": ' + json.dumps(data, indent=4, ensure_ascii=False)
        # 设置颜色开始(至多3类参数，以m结束)：\033[显示方式;前景色;背景色m
        print('\033[0;34m')
        if request.method in ('GET', 'POST', 'PUT', 'DELETE'):
            print(message)
        print('\033[0m')  # 终端颜色恢复
        return res


def handle_error(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            return APIException(code=e.code, error_code=1007, msg=e.description)
        else:
            if not app.config['DEBUG']:
                return ServerError()  # 未知错误(统一为服务端异常)
            else:
                raise e
