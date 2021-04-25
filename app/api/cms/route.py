# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
  ↓↓↓ 文件上传下载接口 ↓↓↓
  可以用来处理上传产品图片、Excel等
"""
from flask import request

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import route as api_doc
from app.core.token_auth import auth
from app.libs.error_code import Success
from app.dao.route import RouteDao
from app.models.route import Route
from app.validators.forms import RouteNodeValidator, RouteNodeWithoutIdValidator

__author__ = 'Mohan'

api = Redprint(name='route', module='路由管理', api_doc=api_doc, alias='cms_route')


@api.route('/tree', methods=['GET'])
@api.doc(auth=True)
@auth.admin_required
def get_all_route_tree():
    """获取所有路由结构"""
    route_root = RouteDao.get_all_route_tree()
    route_tree = route_root['children']
    return Success(route_tree)


@api.route('/tree/with_element', methods=['GET'])
@api.doc(auth=True)
@auth.admin_required
def get_all_route_tree_with_element():
    """获取所有路由结构(含页面元素)"""
    route_root = RouteDao.get_all_route_tree_with_element()
    route_tree = route_root['children']
    return Success(route_tree)


@api.route('/tree', methods=['PUT'])
@api.doc(args=['body.nodes'], auth=True)
@auth.admin_required
def update_route_tree():
    """拖动修改路由结构"""
    RouteDao.change_route(request.json)
    return Success()


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['path.route_id'], auth=True)
@auth.admin_required
def get_route_node(id):
    """按ID获取路由节点"""
    route_node = Route.get_or_404(id=id, msg='路由节点不存在')
    return Success(route_node)


@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['path.route_id', 'body.route_id', 'body.parent_id', 'body.title',
               'body.name', 'body.icon', 'body.path', 'body.component', 'body.hidden'], auth=True)
# @auth.admin_required
def update_route_node(id):
    """按ID修改路由节点"""
    validator = RouteNodeValidator().dt_data # 包含对id的校验
    RouteDao.update(**validator)
    return Success()


@api.route('/<id>', methods=['DELETE'])
@api.doc(args=['path.route_id'], auth=True)
@auth.admin_required
def delete_route_node_by_id(id):
    """按ID删除路由节点"""
    RouteDao.delete(id)
    return Success()


@api.route('', methods=['POST'])
@api.doc(args=['body.parent_id', 'body.title', 'body.name', 'body.icon',
               'body.path', 'body.component', 'body.hidden'], auth=True)
@auth.admin_required
def create_route_node():
    """新增某个路由"""
    validator = RouteNodeWithoutIdValidator()
    route = RouteDao.create(**validator.dt_data)
    return Success(route)
