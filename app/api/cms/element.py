# -*- coding: utf-8 -*-
"""
  Created by Chai on 2020/7/13.
  ↓↓↓ 页面元素管理接口 ↓↓↓
"""
from app.core.error import Success
from app.extensions.api_docs.cms import element as api_doc
from app.extensions.api_docs.redprint import Redprint
from app.dao.element import ElementDao
from app.models.element import Element
from app.core.utils import paginate
from app.validators.forms import ElementValidator, Group2ElementValidator, IDCollectionValidator, GroupIdValidator
from app.core.token_auth import auth

__author__ = 'Chai'

api = Redprint(name='element', module='页面元素管理', api_doc=api_doc, alias='cms_element')


@api.route('', methods=['POST'])
@api.route_meta(auth='新增页面元素', module='页面元素', mount=False)
@api.doc(args=['body.name', 'body.element_sign', 'body.route_id'], auth=True)
@auth.admin_required
def create_element():
    '''新增页面元素'''
    form = ElementValidator().dt_data
    ElementDao.create_element(form)
    return Success(error_code=1)


@api.route('/deploy', methods=['PUT'])
@api.route_meta(auth='配置页面元素', module='页面元素')
@api.doc(args=['body.group_id', 'body.element_id'], auth=True)
@auth.group_required
def deploy_permission():
    '''配置页面元素权限'''
    form = Group2ElementValidator().dt_data
    ElementDao.deploy_permission(form.group_id, form.element_id)
    return Success()


@api.route('/by_group')
@api.route_meta(auth='查询页面元素(基于权限组)', module='页面元素')
@api.doc(args=['g.query.group_id'], auth=True)
@auth.group_required
def get_elemnet_by_group():
    '''查询页面元素(基于权限组)'''
    group_id = GroupIdValidator().nt_data.group_id
    element_list = ElementDao.get_element_by_group(group_id)
    return Success({
        'items': element_list
    })


@api.route('/<string:ids>', methods=['DELETE'])
@api.route_meta(auth='删除页面元素', module='页面元素', mount=False)
@api.doc(args=['g.path.ids'], auth=True)
@auth.admin_required
def delete_element(ids):
    '''删除页面元素'''
    ids = IDCollectionValidator().nt_data.ids
    ElementDao.delete_element(ids)
    return Success(error_code=2)


@api.route('/by_route')
@api.route_meta(auth='查询页面元素(基于路由)', module='页面元素')
@api.doc(args=['g.query.page', 'g.query.size', 'query.route_id'], auth=True)
def get_element_by_route():
    '''查询页面元素(基于路由)'''
    page, size = paginate()
    route_id = 7
    elements = Element.query.filter_by(route_id=route_id).paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': elements.total,
        'current_page': elements.page,
        'items': elements.items
    })
