# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/19.
"""
from flask import Blueprint

__author__ = 'Alimazing'

web = Blueprint('web', __name__)

from app.web import auth
