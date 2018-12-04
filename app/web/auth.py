# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/19.
"""
from flask import render_template, redirect
from . import web

__author__ = 'Alimazing'


@web.route('/', defaults={'path': ''})
@web.route('/<path:path>')
def index(path):
    return redirect('/apidocs/#/')
    # return render_template("index.html")
