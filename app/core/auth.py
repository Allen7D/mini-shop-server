# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/24.
  权限相关的变量与方法
"""
from flask import current_app
from werkzeug.local import LocalProxy

from app.models.auth import Auth
from app.core.error import NotFound
from app.core.redprint import route_meta_infos

__author__ = 'Allen7D'

ep_meta = LocalProxy(lambda: get_ep_meta())


def get_ep_meta():
    _ep_meta = current_app.config['EP_META']
    return _ep_meta if _ep_meta else {}


def find_auth_module(name):
    '''通过权限寻找meta信息
    :param name: '新增商品'
    :return: meta(name='新增商品', module='商品')
    '''
    for _, meta in ep_meta.items():
        if meta.name == name:
            return meta
    return None


def get_ep_name(id):
    '''根据id查询对应的endpoint_info，返回endpoint的name(中文)
    :param id: endpoint_info的id(id每次都是自动生成的)
    :return:
    '''
    ep_info_list = current_app.config['EP_INFO_LIST']
    ep_name = None
    for ep_info in ep_info_list:
        if ep_info['id'] == id:
            ep_name = ep_info['name']
    if not ep_name:
        raise NotFound(msg='权限ID:{} 不存在'.format(id))
    return ep_name


def get_ep_id(name):
    '''根据name查询对应的endpoint_info，返回endpoint的id
    :param name:
    :return:
    '''
    ep_info_list = current_app.config['EP_INFO_LIST']
    ep_id = None
    for ep_info in ep_info_list:
        if ep_info['name'] == name:
            ep_id = ep_info['id']
    if not ep_id:
        raise NotFound(msg='权限名:{} 不存在'.format(name))
    return ep_id


def is_in_auth_scope(group_id, endpoint):
    meta = current_app.config['EP_META'].get(endpoint)
    allowed = False
    if meta:
        allowed = Auth.get(group_id=group_id, name=meta.name, module=meta.module)
    return True if allowed else False


def load_endpint_infos(app):
    """
    返回权限管理中的所有视图函数的信息，包含它所属module
    :return:
    """
    infos = {}
    index = 0
    for ep, meta in app.config['EP_META'].items():
        index += 1
        # 此处的id仅作为Vue的v-for使用，无实际意义
        endpint_info = {'id': index, 'name': meta.name, 'module': meta.module}
        module = infos.get(meta.module, None)
        #  infos是否已经存在该module
        if module:
            module.append(endpint_info)
        else:
            infos[meta.module] = [endpint_info]
        app.config['EP_INFO_LIST'].append(endpint_info)
    app.config['EP_INFOS'] = infos
    return infos


def mount_route_meta_to_endpoint(app):
    '''
    将route_mate挂载到对应的endpoint上
    :param app:
    :return:
    '''
    for endpoint, func in app.view_functions.items():
        info = route_meta_infos.get(func.__name__ + str(func.__hash__()), None)
        if info:
            app.config['EP_META'].setdefault(endpoint, info)
