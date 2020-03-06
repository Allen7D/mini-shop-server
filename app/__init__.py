# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
from .app import Flask
from app.models.base import db
from app.web import web
from app.api import create_blueprint_list

__author__ = 'Allen7D'

bp_list = create_blueprint_list()

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
	db.init_app(app)
	with app.app_context():  # 手动将app推入栈
		db.create_all()  # 首次模型映射(ORM ==> SQL),若无则建表; 初始化使用

	# Debug模式下可以查阅 API文档
	if app.config['DEBUG']:
		from flasgger import Swagger
		tags = [tag for _, bp in bp_list for tag in bp.tags]
		# 默认与 config/setting.py 的 SWAGGER 合并
		# 可以将secure.py中的SWAGGER全部写入template
		swagger = Swagger(template={'tags': tags})
		swagger.init_app(app)

	# Debug模式下可以查阅 ORM 管理
	if app.config['DEBUG']:
		add_orm_admin(app)


def add_orm_admin(app):
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
			model_view_module = __import__('model_views.{}'.format(module_name), globals(), fromlist=('***'), level=1)
			model_view = getattr(model_view_module, '{}View'.format(model_name), ModelView)
		except ModuleNotFoundError as e:
			model_view = ModelView
		# admin添加model_view
		admin.add_view(model_view(model, db.session))

	# Admin添加文件管理系统
	from flask_admin.contrib.fileadmin import FileAdmin
	import os.path as op
	path = op.join(op.dirname(__file__), 'static')
	admin.add_view(FileAdmin(path, '/static/', name='静态资源'))

	admin.init_app(app, url='/admin')


def register_blueprint(app):
	'''注册蓝图'''
	for url_prefix, bp in bp_list:
		app.register_blueprint(bp, url_prefix=url_prefix)
	app.register_blueprint(web)
