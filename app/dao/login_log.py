# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/16.
"""
from app.models.login_log import LoginLog

__author__ = 'Allen7D'


class LoginLogDao(object):
    @staticmethod
    def get_log_list(page, size, start=None, end=None):
        log = LoginLog.query.filter_by()
        if start and end:
            log = log.filter(LoginLog.create_time.between(start, end))
        paginator = log.order_by(LoginLog.create_time.desc()) \
            .paginate(page=page, per_page=size, error_out=True)
        return paginator
