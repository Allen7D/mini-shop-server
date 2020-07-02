# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/15.
  ↓↓↓ 登录日志接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import login_log as api_doc
from app.core.db import db
from app.core.token_auth import auth
from app.core.utils import paginate, time_interval
from app.models.login_log import LoginLog
from app.dao.login_log import LoginLogDao
from app.libs.error_code import Success

__author__ = 'Allen7D'

api = Redprint(name='log/login', module='登录日志管理', api_doc=api_doc, alias='cms_login_log')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询日志列表', module='登录日志')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.start', 'g.query.end'], auth=True)
@auth.group_required
def get_log_list():
    '''查询登录日志列表'''
    page, size = paginate()
    start, end = time_interval()
    paginator = LoginLogDao.get_log_list(page, size, start, end)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:id>', methods=['GET'])
@api.route_meta(auth='查询日志', module='登录日志')
@api.doc(args=['g.path.log_id'], auth=True)
@auth.group_required
def get_log(id):
    '''查询登录日志'''
    log = LoginLog.get_or_404(id=id)
    return Success(log)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除日志', module='登录日志')
@api.doc(args=['g.path.log_id'], auth=True)
@auth.admin_required
def delete_log(id):
    '''删除登录日志'''
    LoginLog.get_or_404(id=id).delete()
    return Success(error_code=2)


@api.route('/all', methods=['DELETE'])
@api.route_meta(auth='清除所有日志', module='登录日志')
@api.doc(auth=True)
@auth.admin_required
def delete_all_log():
    '''删除所有登录日志'''
    with db.auto_commit():
        LoginLog.query.filter().delete(synchronize_session=False)
    return Success(error_code=2)
