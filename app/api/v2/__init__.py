# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from flask import Blueprint

from app.api.v2 import book

__author__ = 'Alimazing'

def create_blueprint_v2():
	bp_v2 = Blueprint('v2', __name__)
	book.api.register(bp_v2)
	return bp_v2
