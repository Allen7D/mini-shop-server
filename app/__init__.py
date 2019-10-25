# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
from .app import Flask
from app.api.v1 import bp as v1_bp
from app.api.cms import bp as cms_bp
from app.web import web

__author__ = 'Allen7D'


def create_app():
	app = Flask(__name__, static_folder="./static", template_folder="./static/views")

	app.config.from_object('app.config.secure')
	app.config.from_object('app.config.setting')

	register_blueprint(app)
	register_plugin(app)

	return app


def register_plugin(app):
	# 解决跨域问题
	from flask_cors import CORS
	cors = CORS()
	cors.init_app(app, resources={"/*": {"origins": "*"}})

	# 连接数据库
	from app.models.base import db
	db.init_app(app)
	with app.app_context():  # 手动将app推入栈
		db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表; 初始化使用

	# Debug模式下可以查阅 API文档
	if app.config['DEBUG']:
		from flasgger import Swagger
		tags = v1_bp.tags + cms_bp.tags
		# 默认与 config/setting.py 的 SWAGGER 合并
		# 可以将secure.py中的SWAGGER全部写入template
		swagger = Swagger(template={'tags': tags})
		swagger.init_app(app)


def register_blueprint(app):
	app.register_blueprint(v1_bp, url_prefix='/v1')
	app.register_blueprint(cms_bp, url_prefix='/cms')
	app.register_blueprint(web)
