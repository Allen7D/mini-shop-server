# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
  flask-login文档：https://flask-login.readthedocs.io/en/latest/
  flask-admin文档：https://flask-admin.readthedocs.io/en/v1.0.9/quickstart/#
  中文版flask_admin官方文档: https://blog.csdn.net/ohonor_net/article/details/88860052
  Flask-admin 使用经验技巧总结: https://www.cnblogs.com/magicroc/p/6103773.html?utm_source=itdadao&utm_medium=referral
  Vue 2.0 起步(6) 后台管理Flask-Admin - 微信公众号RSS: https://www.jianshu.com/p/56cbb68f8797#
"""
from .app import Flask
from app.models.base import db
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

	# Debug模式下可以查阅 ORM 管理
	if app.config['DEBUG']:
		add_orm_admin(app)


def add_orm_admin(app):
	from flask_admin import Admin
	from app.libs.model_view import ModelView

	from app.config.setting import all_model_by_module
	object_origins = {}
	for module, items in all_model_by_module.items():
		for item in items:
			object_origins[item] = module

	admin = Admin(name='小程序商城:ORM管理', template_mode='bootstrap3')
	for model_name, module_name in object_origins.items():
		module = __import__('models.{}'.format(module_name), globals(), fromlist=(model_name), level=1)
		model = getattr(module, model_name)
		admin.add_view(ModelView(model, db.session))

	# Admin添加文件管理系统
	from flask_admin.contrib.fileadmin import FileAdmin
	import os.path as op
	path = op.join(op.dirname(__file__), 'static')
	admin.add_view(FileAdmin(path, '/static/', name='静态资源'))

	admin.init_app(app, url='/admin')


def register_blueprint(app):
	app.register_blueprint(v1_bp, url_prefix='/v1')
	app.register_blueprint(cms_bp, url_prefix='/cms')
	app.register_blueprint(web)
