# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
  print输出字体颜色: https://www.cnblogs.com/easypython/p/9084426.html
"""
import json
import time

from werkzeug.exceptions import HTTPException
from flask import redirect, url_for, g, request, _request_ctx_stack

from .app import Flask
from app.models.base import db
from app.web import web
from app.api import create_blueprint_list
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'Allen7D'

bp_list = create_blueprint_list()


def create_app():
    # 默认template_folder值就是'./templates'
    app = Flask(__name__, static_folder="./static", template_folder="./templates")

    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprint(app)
    register_plugin(app)

    return app


def register_plugin(app):
    apply_cors(app)  # 应用跨域扩展，使项目支持请求跨域
    connect_db(app)  # 连接数据库
    handle_error(app)  # 统一处理异常

    # Debug模式(以下为非必选应用，且用户不可见)
    if app.config['DEBUG']:
        apply_request_log(app) # 打印请求日志
        apply_default_router(app)  # 应用默认路由
        apply_orm_admin(app)  # 应用flask-admin, 可以进行简易的 ORM 管理
        apply_swagger(app)  # 应用flassger, 可以查阅Swagger风格的 API文档


def apply_cors(app):
    from flask_cors import CORS
    cors = CORS()
    cors.init_app(app, resources={"/*": {"origins": "*"}})


def connect_db(app):
    db.init_app(app)
    #  初始化使用
    with app.app_context():  # 手动将app推入栈
        db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表


def apply_default_router(app):
    @app.route('/')
    def index():
        '''跳转到「首页」'''
        return redirect(url_for('web.index'))

    @app.route('/doc')
    def doc():
        '''跳转到「api文档」'''
        return redirect('/apidocs/#/')


def apply_orm_admin(app):
    from flask_admin import Admin
    from app.model_views.base import ModelView

    from app.config.setting import all_model_by_module
    object_origins = {}
    for module, items in all_model_by_module.items():
        for item in items:
            object_origins[item] = module

    admin = Admin(name='商城后台', template_mode='bootstrap3')
    for model_name, module_name in object_origins.items():
        model_module = __import__('models.{}'.format(module_name), globals(), fromlist=('***'), level=1)
        model = getattr(model_module, model_name)
        try:
            # model_view_module 可能不存在
            model_view_module = __import__('model_views.{}'.format(module_name), globals(), fromlist=('***'),
                                           level=1)
            model_view = getattr(model_view_module, '{}View'.format(model_name), ModelView)
        except ModuleNotFoundError as e:
            model_view = ModelView
        # admin添加model_view
        admin.add_view(model_view(model, db.session))

    apply_file_admin(admin)
    admin.init_app(app, url='/admin')


def apply_file_admin(admin):
    # Admin添加文件管理系统
    from flask_admin.contrib.fileadmin import FileAdmin
    import os.path as op
    path = op.join(op.dirname(__file__), 'static')
    admin.add_view(FileAdmin(path, '/static/', name='静态资源'))


def apply_swagger(app):
    from flasgger import Swagger
    tags = [tag for _, bp in bp_list for tag in bp.tags]
    # 默认与 config/setting.py 的 SWAGGER 合并
    # 可以将secure.py中的SWAGGER全部写入template
    swagger = Swagger(template={'tags': tags})
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
        message += "\n\tdata: {\n\t\tpath: %s, \n\t\tquery: %s, \n\t\tbody: %s\n\t} " % (
            json.dumps(_request_ctx_stack.top.request.view_args, ensure_ascii=False),
            json.dumps(request.args, ensure_ascii=False),
            req_body
        )
        # 设置颜色开始(至多3类参数，以m结束)：\033[显示方式;前景色;背景色m
        print('\033[0;34m')
        print(message)
        print('\033[0m') # 终端颜色恢复
        return res


def handle_error(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            code = e.code
            msg = e.description
            error_code = 1007
            return APIException(code, error_code, msg)
        else:
            if not app.config['DEBUG']:
                return ServerError()  # 未知错误(统一为服务端异常)
            else:
                raise e


def register_blueprint(app):
    '''注册蓝图'''
    for url_prefix, bp in bp_list:
        app.register_blueprint(bp, url_prefix=url_prefix)
    app.register_blueprint(web, url_prefix='/web')
