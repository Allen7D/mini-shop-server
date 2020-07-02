# -*- coding: utf-8 -*-
from flask import request

from app.core.error import Success
from app.extensions.api_docs.cms import route as api_doc
from app.extensions.api_docs.redprint import Redprint
from app.dao.element import ElementDao
from app.models.element import Element
api = Redprint(name='element', module='元素管理', api_doc=api_doc, alias='cms_element')


@api.route('', methods=['POST'])
def create_element():
    """新增页面元素"""
    ElementDao.add_element(request.json)
    return Success()


@api.route('/deploy', methods=['PUT'])
def deploy_permission():
    """配置页面元素权限"""
    ElementDao.deploy_permission(request.json['group_id'], request.json['element_id'])
    return Success()


@api.route('/group_element')
def get_group_elemnet():
    group_id = request.args.get('group_id')
    group_element = ElementDao.get_group_element(group_id)
    return Success(group_element)


@api.route('/<id>', methods=['DELETE'])
def delete_element(id):
    """删除元素"""
    ElementDao.delete_element(id)
    return Success()

@api.route('/list')
def get_element_list():
    elements = Element.get_all()
    return Success(elements)
