# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/17.
"""
from flask import Blueprint

__author__ = 'Alimazing'

def create_blueprint_v2():
	bp_v1 = Blueprint('v2', __name__)
	return bp_v1
