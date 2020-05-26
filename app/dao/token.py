# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/17.
"""
from flask import g

__author__ = 'Allen7D'


class TokenDao():
    @staticmethod
    def is_valid_operate(checked_uid):
        if not checked_uid:
            raise Exception('检测uid时，必须传入一个被检查的uid')
        current_operate_uid = g.user.id
        return True if current_operate_uid == checked_uid else False

    @staticmethod
    def get_current_token_var(key):
        '''查询缓存中的变量'''
        pass
