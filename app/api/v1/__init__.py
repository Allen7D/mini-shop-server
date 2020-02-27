# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/10/25.
"""
from app.libs.blueprint import Blueprint
from app.api.v1 import token, user, \
	banner, theme, product, category, \
	address, order, pay

__author__ = 'Allen7D'

rp_list = [token, user, banner, theme, product, category, address, order, pay]
bp = Blueprint('v1', __name__).register_redprint(rp_list)
