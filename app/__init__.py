# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
import os

from flask import Flask
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError

from app.core.db import db
from app.core.auth import load_endpint_infos, mount_route_meta_to_endpoint
from app.core.redprint import RedprintAssigner
from app.core.error import APIException, ServerError, RepeatException
from app.core.logger import apply_request_log
from app.extensions.api_docs.swagger import apply_swagger
from app.extensions.default_view import apply_default_view
from app.extensions.orm_admin import apply_orm_admin

__version__ = "1.0.0"
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


def register_plugin(app):
    apply_json_encoder(app)  # JSON序列化
    apply_cors(app)  # 应用跨域扩展，使项目支持请求跨域
    connect_db(app)  # 连接数据库
    handle_error(app)  # 统一处理异常

    # Debug模式(以下为非必选应用，且用户不可见)
    apply_default_view(app)  # 应用默认路由
    apply_orm_admin(app)  # 应用flask-admin, 可以进行简易的 ORM 管理
    apply_swagger(app)  # 应用flassger, 可以查阅Swagger风格的 API文档
    if app.config['DEBUG']:
        apply_request_log(app)  # 打印请求日志


def apply_json_encoder(app):
    from app.core.json_encoder import JSONEncoder
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


def handle_error(app):
    @app.errorhandler(Exception)
    def framework_error(e):
        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            return APIException(code=e.code, error_code=1007, msg=str(e.description))
        elif isinstance(e, IntegrityError) and 'Duplicate entry' in e.orig.errmsg:
            return RepeatException(msg='数据的unique字段重复')
        else:
            if not app.config['DEBUG']:
                return ServerError()  # 未知错误(统一为服务端异常)
            else:
                raise e
