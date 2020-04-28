# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
  ↓↓↓ 文件上传下载接口 ↓↓↓
  可以用来处理上传产品图片、Excel等
"""
from flask import g
from flask import request

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import menu as api_doc
from app.core.token_auth import auth
from app.libs.error_code import Success
from app.models.menu import Menu
from app.models.route import Route
from app.models.group import Group
from app.dao.menu import MenuDao
from app.validators.forms import MenuGroupIdValidator, MenuValidator

__author__ = 'Mohan'

api = Redprint(name='menu', alias='cms_menu', description='菜单', api_doc=api_doc)


@api.route('/', methods=['GET'])
@api.doc(args=['query.group_id'], auth=True)
# @auth.admin_required
def get_routes():
    """根据用户组ID, 获取菜单"""
    form = MenuGroupIdValidator().dt_data
    gid = int(form['group_id'])
    return Success(MenuDao.get_routes(gid))


@api.route('/', methods=['POST'])
@api.doc(args=['body.group_id', 'body.routes'], auth=True)
# @auth.admin_required
def add_routes():
    """向指定用户组的菜单中, 添加路由节点"""
    form = MenuValidator().nt_data
    MenuDao.add_route(gid=form.group_id, routes=form.routes)
    return Success()


@api.route('/', methods=['DELETE'])
@api.doc(args=['body.group_id', 'body.routes'], auth=True)
# @auth.admin_required
def delete_route():
    """从指定用户组的菜单中, 删除路由节点"""
    form = MenuValidator().nt_data
    MenuDao.delete_routes(gid=form.group_id, routes=form.routes)
    return Success()
