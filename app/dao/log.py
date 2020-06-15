# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/19.
"""
from sqlalchemy import text

from app.core.db import db
from app.models.log import Log

__author__ = 'Allen7D'


class LogDao(object):
    @staticmethod
    def get_log_list(page, size, user_name=None, start=None, end=None):
        log = Log.query.filter_by()
        if user_name:
            log = log.filter_by(user_name=user_name)
        if start and end:
            log = log.filter(Log.time.between(start, end))
        paginator = log.order_by(Log.create_time.desc()) \
            .paginate(page=page, per_page=size, error_out=True)
        return paginator

    @staticmethod
    def get_log_list_by_keyword(page, size, user_name=None, keyword=None, start=None, end=None):
        log = Log.query.filter(Log.message.like(f'%{keyword}%'))
        if user_name:
            log = log.filter_by(user_name=user_name)
        if start and end:
            log = log.filter(Log.time.between(start, end))
        paginator = log.order_by(Log.create_time.desc()) \
            .paginate(page=page, per_page=size, error_out=True)
        return paginator

    @staticmethod
    def get_user_list(page, size):
        paginator = db.session.query(Log.user_name) \
            .group_by(text('user_name')) \
            .having(text('count(user_name) > 0')) \
            .paginate(page=page, per_page=size, error_out=True)
        users = [user_name[0] for user_name in paginator.items]
        return users

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
