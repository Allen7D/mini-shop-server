# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/28.
  ↓↓↓ 异常日志接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import login_log as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate, time_interval
from app.core.db import db
from app.models.error_log import ErrorLog
from app.libs.error_code import Success
from app.validators.forms import IDCollectionValidator

__author__ = 'Allen7D'

api = Redprint(name='log/error', module='异常日志管理', api_doc=api_doc, alias='cms_error_log')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询日志列表', module='异常日志')
@api.doc(args=['g.query.page', 'g.query.size', 'g.query.start', 'g.query.end'], auth=True)
@auth.group_required
def get_log_list():
    '''查询异常日志列表'''
    page, size = paginate()
    start, end = time_interval()
    return Success()


@api.route('/<int:id>', methods=['GET'])
@api.route_meta(auth='查询日志', module='异常日志')
@api.doc(args=['g.path.log_id'], auth=True)
@auth.group_required
def get_log(id):
    '''查询异常日志'''
    return Success()


@api.route('/<string:ids>', methods=['DELETE'])
@api.route_meta(auth='删除日志', module='异常日志')
@api.doc(args=['g.path.ids'], auth=True)
@auth.admin_required
def delete_log(ids):
    '''删除异常日志'''
    ids = IDCollectionValidator().nt_data.ids
    return Success(error_code=2)


@api.route('/all', methods=['DELETE'])
@api.route_meta(auth='清除所有日志', module='异常日志')
@api.doc(auth=True)
@auth.admin_required
def delete_all_log():
    '''删除所有异常日志'''
    with db.auto_commit():
        ErrorLog.query.filter().delete(synchronize_session=False)
    return Success(error_code=2)
