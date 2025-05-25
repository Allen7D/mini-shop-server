# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/5.
  ↓↓↓ 权限组路由管理接口 ↓↓↓
"""
from flask import request

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import menu as api_doc
from app.core.token_auth import auth
from app.libs.error_code import Success
from app.dao.menu import MenuDao
from app.validators.forms import MenuGroupIdValidator

__author__ = 'Mohan'

api = Redprint(name='menu', module='菜单管理', api_doc=api_doc, alias='cms_menu')


@api.route('', methods=['GET'])
@api.doc(args=['query.group_id'], auth=True)
def get_routes():
    """根据权限组ID, 获取菜单"""
    gid = MenuGroupIdValidator().group_id.data
    return Success(MenuDao.get_routes(gid))


@api.route('', methods=['PUT'])
@api.doc(args=['body.routes', 'body.group_id'], auth=True)
def delete_route():
    """覆盖权限组的菜单列表"""
    MenuDao.cover_menus(**request.json)
    return Success()
