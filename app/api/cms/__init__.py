# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/10/25.
"""
from app.libs.blueprint import Blueprint
from app.api.cms import user, category, product, file

__author__ = 'Allen7D'

rp_list = [user, category, product, file]
bp = Blueprint('cms', __name__).register_redprint(rp_list)
