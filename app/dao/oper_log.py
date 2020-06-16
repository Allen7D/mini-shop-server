# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/19.
"""
from sqlalchemy import text

from app.core.db import db
from app.models.oper_log import OperLog

__author__ = 'Allen7D'


class OperLogDao(object):
    @staticmethod
    def get_log_list_by_search(page, size, start=None, end=None, user_name=None, keyword=None):
        log = OperLog.query.filter_by()
        if keyword:
            log = log.filter(OperLog.message.like(f'%{keyword}%'))
        if user_name:
            log = log.filter_by(user_name=user_name)
        if start and end:
            log = log.filter(OperLog.create_time.between(start, end))
        paginator = log.order_by(OperLog.create_time.desc()) \
            .paginate(page=page, per_page=size, error_out=True)
        return paginator

    @staticmethod
    def get_user_list(page, size):
        paginator = db.session.query(OperLog.user_name) \
            .group_by(text('user_name')) \
            .having(text('count(user_name) > 0')) \
            .paginate(page=page, per_page=size, error_out=True)
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': [user_name[0] for user_name in paginator.items]
        }
