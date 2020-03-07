# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/19.
"""
from app.libs.blueprint import Blueprint

__author__ = 'Allen7D'

web = Blueprint('web', __name__)

from app.web import doc
