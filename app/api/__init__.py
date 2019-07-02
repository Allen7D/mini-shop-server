# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/6/27.
"""
from app.api.v1 import create_api_tags_v1
from app.api.cms import create_api_tags_cms

__author__ = 'Allen7D'

tags = create_api_tags_v1() + create_api_tags_cms()