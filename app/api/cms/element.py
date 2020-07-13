# -*- coding: utf-8 -*-

__author__ = 'Chai'

from flask import request

from app.core.error import Success
from app.extensions.api_docs.cms import element as api_doc
from app.extensions.api_docs.redprint import Redprint
from app.dao.element import ElementDao
from app.models.element import Element
from app.core.utils import paginate
from app.validators.forms import ElementValidator, Element2GroupValidator, IDCollectionValidator, GroupIdValidator
from app.core.token_auth import auth


api = Redprint(name='element', module='元素管理', api_doc=api_doc, alias='cms_element')


@api.route('', methods=['POST'])
@api.route_meta(auth='新增页面元素', module='元素管理', mount=False)
@api.doc(args=['body.name', 'body.element_sign', 'body.route_id'], auth=True)
@auth.admin_required
def create_element():
    '''新增页面元素'''
    form = ElementValidator().dt_data
    ElementDao.add_element(form)
    return Success()


@api.route('/deploy', methods=['PUT'])
@api.route_meta(auth='配置页面元素', module='元素管理')
@api.doc(args=['body.group_id', 'body.element_id'], auth=True)
@auth.group_required
def deploy_permission():
    '''配置页面元素权限'''
    form = Element2GroupValidator().dt_data
    ElementDao.deploy_permission(form.group_id, form.element_id)
    return Success()


@api.route('/group_element')
@api.route_meta(auth='查询权限组所有的元素', module='元素管理')
@api.doc(args=['query.group_id'], auth=True)
@auth.group_required
def get_group_elemnet():
    '''查询权限组所有元素'''
    group_id = GroupIdValidator().nt_data.group_id
    group_element = ElementDao.get_group_element(group_id)
    return Success(group_element)


@api.route('/<string:ids>', methods=['DELETE'])
@api.route_meta(auth='删除页面元素', module='元素管理', mount=False)
@api.doc(args=['g.path.ids'], auth=True)
@auth.admin_required
def delete_element(ids):
    '''删除元素'''
    ids = IDCollectionValidator().nt_data.ids
    ElementDao.delete_element(ids)
    return Success(error_code=2)

@api.route('/list')
@api.route_meta(auth='查询所有元素', module='元素管理')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_element_list():
    '''查询所有元素'''
    page, size = paginate()
    elements = Element.query.filter_by().paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': elements.total,
        'current_page': elements.page,
        'items': elements.items
    })
