# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/19.
"""
from flask import render_template, redirect
from . import web

__author__ = 'Allen7D'


# @web.route('/', defaults={'path': ''})
# @web.route('/<path:path>')
@web.route('/')
def index():
    '''默认跳转的 API 文档'''
    return redirect('/apidocs/#/')
    # return render_template("index.html")
