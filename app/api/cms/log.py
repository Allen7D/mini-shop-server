# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/15.
  ↓↓↓ 日志接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import log as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate, time_interval
from app.dao.log import LogDao
from app.libs.error_code import Success
from app.validators.forms import LogFindValidator, LogSearchValidator

__author__ = 'Allen7D'

api = Redprint(name='log', description='日志管理', api_doc=api_doc, alias='cms_log')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询日志列表', module='日志')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.start', 'g.query.end'], auth=True)
@auth.group_required
def get_log_list():
    '''查询日志列表(按人员&时间)'''
    page, size = paginate()
    start, end = time_interval()
    user_name = LogFindValidator().get_data('user')
    paginator = LogDao.get_log_list(page, size, user_name, start, end)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/search', methods=['GET'])
@api.route_meta(auth='搜索日志', module='日志')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.start', 'g.query.end'], auth=True)
@auth.group_required
def get_log_list_by_keyword():
    '''搜索日志(按人员&时间&内容)'''
    page, size = paginate()
    start, end = time_interval()
    user_name, keyword = LogSearchValidator().get_data('user', 'keyword')
    paginator = LogDao.get_log_list_by_keyword(page, size, user_name, keyword, start, end)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/user/list', methods=['GET'])
@api.route_meta(auth='查询用户列表', module='日志')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_users():
    '''查询用户列表'''
    page, size = paginate()
    users = LogDao.get_user_list(page, size)
    return Success({
        'items': users
    })
