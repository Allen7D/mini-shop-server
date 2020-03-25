# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
"""
from flask import current_app
from werkzeug.local import LocalProxy

from app.models.auth import Auth as AuthModel
from app.libs.error_code import NotFound

__author__ = 'Allen7D'

ep_meta = LocalProxy(lambda: get_ep_meta())


def get_ep_meta():
    _ep_meta = current_app.config['EP_META']
    return _ep_meta if _ep_meta else {}


def find_auth_module(auth):
    '''通过权限寻找meta信息
    :param auth: '新增商品'
    :return: meta(auth='新增商品', module='商品')
    '''
    for _, meta in ep_meta.items():
        if meta.auth == auth:
            return meta
    return None


def get_ep_name(id):
    ep_info_list = current_app.config['EP_INFO_LIST']
    ep_name = None
    for ep_info in ep_info_list:
        if ep_info['id'] == id:
            ep_name = ep_info['auth']
    if not ep_name:
        raise NotFound(msg='权限ID:{} 不存在'.format(id))
    return ep_name


def get_ep_id(name):
    ep_info_list = current_app.config['EP_INFO_LIST']
    ep_id = None
    for ep_info in ep_info_list:
        if ep_info['auth'] == name:
            ep_id = ep_info['id']
    if not ep_id:
        raise NotFound(msg='权限名:{} 不存在'.format(name))
    return ep_id


def is_in_auth_scope(group_id, endpoint):
    meta = current_app.config['EP_META'].get(endpoint)
    allowed = False
    if meta:
        allowed = AuthModel.get(group_id=group_id, auth=meta.auth, module=meta.module)
    return True if allowed else False
