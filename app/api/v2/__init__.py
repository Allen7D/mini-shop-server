# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/7.
"""
from flask import Blueprint

from app.api.v2 import file

__author__ = 'Allen7D'


def create_blueprint_v2():
	bp_v2 = Blueprint('v2', __name__)
	file.api.register(bp_v2)

	return bp_v2


def create_api_tags_v2():
	return [
		file.api.tag
	]
