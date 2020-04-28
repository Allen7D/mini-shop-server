# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/28.
"""
from importlib import import_module

from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin

from app.core.db import db
from .base import ModelView

__author__ = 'Allen7D'


class Extension():
    def __init__(self, name='', template_mode='bootstrap3'):
        self.admin = Admin(name=name, template_mode=template_mode)
        self.object_origins = {}

    def init_app(self, app):
        # 配置config
        app.config.from_object('app.extensions.orm_admin.config')
        self.load_model(app)
        self.apply_file_admin(app)
        self.apply_orm_admin()

        self.admin.init_app(app)

    def load_model(self, app):
        for module, items in app.config['ALL_MODEL_BY_MODULE'].items():
            for item in items:
                self.object_origins[item] = module

    def apply_orm_admin(self):
        for model_name, module_name in self.object_origins.items():
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
            self.admin.add_view(model_view(model, db.session,
                                           endpoint='admin.{}'.format(lower_model_name),
                                           url='/admin/{}'.format(lower_model_name)))

    def apply_file_admin(self, app):
        # Admin添加文件管理系统
        path = 'app' + app.static_url_path
        self.admin.add_view(FileAdmin(path, '/static/', name='静态资源'))
