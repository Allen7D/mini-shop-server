# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
from .app import Flask

__author__ = 'Allen7D'


def create_app():
	app = Flask(__name__, static_folder="./static", template_folder="./static/views")

	app.config.from_object('app.config.secure')
	app.config.from_object('app.config.setting')
	app.config.from_object('app.config.wx')

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
		from app.api.v1 import create_api_tags_v1
		from app.api.v2 import create_api_tags_v2
		template = {
			# 默认与 config/setting.py 的 SWAGGER 合并
			'tags': create_api_tags_v1() + create_api_tags_v2()  # 数组
		}
		swagger = Swagger(template=template)  # 可以将secure.py中的SWAGGER全部写入template
		swagger.init_app(app)

	# 缓存 Cache
	from app.libs.limiter import cache
	cache.init_app(app, config={"CACHE_TYPE": "simple"})
	with app.app_context():
		cache.clear()


def register_blueprint(app):
	from app.api.v1 import create_blueprint_v1
	app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
	from app.api.v2 import create_blueprint_v2
	app.register_blueprint(create_blueprint_v2(), url_prefix='/v2')
	from app.web import web
	app.register_blueprint(web)
