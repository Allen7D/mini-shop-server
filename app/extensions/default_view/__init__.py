# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/9.
"""
from importlib import import_module

from flask import current_app, render_template, redirect

from app.core.error import APIException

__author__ = 'Allen7D'


def apply_default_view(app):
    '''
    :param app: Flask实例
    :return:
    '''
    app.config.from_object('app.extensions.default_view.config')

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
