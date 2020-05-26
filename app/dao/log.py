# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/19.
"""
from app.core.db import db
from app.models.log import Log

__author__ = 'Allen7D'


class LogDao(object):
    @staticmethod
    def create_log(**kwargs):
        log = Log()
        for key in kwargs.keys():
            if hasattr(log, key):
                setattr(log, key, kwargs[key])
        db.session.add(log)
        if kwargs.get('commit') is True:
            db.session.commit()
        return log
