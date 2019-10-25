# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/10/25.
"""
from app.libs.blueprint import Blueprint
from app.api.cms import user, file

__author__ = 'Allen7D'

rp_list = [user, file]
bp = Blueprint('cms', __name__, rp_list).register_redprint()
