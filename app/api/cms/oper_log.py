# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/15.
  ↓↓↓ 操作日志接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import oper_log as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate, time_interval
from app.core.db import db
from app.models.oper_log import OperLog
from app.dao.oper_log import OperLogDao
from app.libs.error_code import Success
from app.validators.forms import LogSearchValidator

__author__ = 'Allen7D'

api = Redprint(name='log/oper', description='操作日志管理', api_doc=api_doc, alias='cms_oper_log')


@api.route('/list/search', methods=['GET'])
@api.route_meta(auth='搜索操作日志', module='操作日志')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.start', 'g.query.end',
               'g.query.username', '*str.query.keyword'], auth=True)
@auth.group_required
def get_log_list_by_search():
    '''搜索操作日志(按人员&时间&内容)'''
    page, size = paginate()
    start, end = time_interval()
    user_name, keyword = LogSearchValidator().get_data('username', 'keyword')
    paginator = OperLogDao.get_log_list_by_search(page, size, start, end, user_name, keyword)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/user/list', methods=['GET'])
@api.route_meta(auth='查询用户列表', module='操作日志')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_users():
    '''查询用户列表'''
    page, size = paginate()
    paginator = OperLogDao.get_user_list(page, size)
    return Success(paginator)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除操作日志', module='操作日志')
@api.doc(args=['g.path.log_id'], auth=True)
@auth.admin_required
def delete_log(id):
    '''删除操作日志'''
    OperLog.get_or_404(id=id).delete()
    return Success(error_code=2)


@api.route('/all', methods=['DELETE'])
@api.route_meta(auth='清除所有操作日志', module='操作日志')
@api.doc(auth=True)
@auth.admin_required
def delete_all_log():
    '''删除所有操作日志'''
    with db.auto_commit():
        OperLog.query.filter().delete(synchronize_session=False)
    return Success(error_code=2)
