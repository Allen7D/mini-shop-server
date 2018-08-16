# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/12.
"""

from .app import Flask

__author__ = 'Alimazing'


def create_app():
	app = Flask(__name__)
	app.config.from_object('app.config.secure')
	app.config.from_object('app.config.setting')
	app.config.from_object('app.config.wx')

	register_blueprint(app)
	register_plugin(app)

	return app


def register_plugin(app):
	from app.models.base import db
	from flask_cors import CORS

	cors = CORS()
	cors.init_app(app, resources={"/*": {"origins": "*"}})

	db.init_app(app)
	with app.app_context():
		db.create_all()


def register_blueprint(app):
	from app.api.v1 import create_blueprint_v1
	app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
