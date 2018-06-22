# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/31.
"""
from flask import Blueprint

from app.api.v1 import user, book, client, token, gift, \
						banner, theme, product, category

__author__ = 'Alimazing'

def create_blueprint_v1():
	bp_v1 = Blueprint('v1', __name__)
	# 将 红图user.api注册进 蓝图bp_v1
	user.api.register(bp_v1)
	book.api.register(bp_v1)
	client.api.register(bp_v1)
	token.api.register(bp_v1)
	gift.api.register(bp_v1)
	banner.api.register(bp_v1)
	theme.api.register(bp_v1)
	product.api.register(bp_v1)
	category.api.register(bp_v1)
	return bp_v1
