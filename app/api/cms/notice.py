# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
  ↓↓↓ 通知(公告)接口 ↓↓↓
"""
from flask import g

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import notice as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.notice import Notice
from app.dao.notice import NoticeDao
from app.libs.error_code import Success
from app.validators.forms import CreateNoticeValidator, UpdateNoticeValidator

__author__ = 'Allen7D'

api = Redprint(name='notice', module='通知(公告)', api_doc=api_doc, alias='cms_notice')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询通知列表', module='通知(公告)')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_notice_list():
    '''查询通知列表'''
    page, size = paginate()
    paginator = Notice.query.paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.notice_id'])
@auth.group_required
def get_notice(id):
    '''查询通知'''
    notice = Notice.get_or_404(id=id)
    return Success(notice)


@api.route('', methods=['POST'])
@api.route_meta(auth='新建通知', module='通知(公告)')
@api.doc(args=['body.type', 'body.title', 'body.content', 'body.status', 'body.remark'], auth=True)
@auth.group_required
def create_notice():
    '''新建通知'''
    form = CreateNoticeValidator().dt_data
    Notice.create(create_by=g.user.nickname, **form)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新通知', module='通知(公告)')
@api.doc(args=['g.path.notice_id', 'body.type', 'body.title', 'body.content', 'body.status', 'body.remark'], auth=True)
@auth.group_required
def update_article(id):
    '''更新通知'''
    form = UpdateNoticeValidator().dt_data
    notice = NoticeDao.update_notice(id, update_by=g.user.nickname, **form)
    return Success(notice, error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(args=['g.path.notice_id'], auth=True)
@auth.group_required
def delete_notice(id):
    '''删除通知'''
    NoticeDao.delete_notice(id)
    return Success(error_code=2)
