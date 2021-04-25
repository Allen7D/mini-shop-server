# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from flask import current_app

from app.core.db import db
from app.core.auth import get_ep_name, find_auth_module, get_ep_id
from app.models.auth import Auth

__author__ = 'Allen7D'


class AuthDao():
    # 查询所有可分配的权限
    @staticmethod
    def get_auths():
        auths = current_app.config['EP_INFOS']
        return auths

    @staticmethod
    def append_auth_list(group_id, auth_ids=[]):
        '''
        :param group_id: 权限组id
        :param auth_ids: 权限id数组
        :return:
        '''
        auth_name_list = [get_ep_name(id) for id in auth_ids]
        with db.auto_commit():
            for name in auth_name_list:
                one = Auth.get(group_id=group_id, name=name)
                if not one:
                    meta = find_auth_module(name)
                    Auth.create(group_id=group_id, name=meta.name, module=meta.module, commit=False)

    @staticmethod
    def delete_auth_list(group_id, auth_ids=[]):
        '''
        :param group_id: 权限组id
        :param auth_ids: 权限id数组
        :return:
        '''
        auth_name_list = [get_ep_name(id) for id in auth_ids]
        with db.auto_commit():
            db.session.query(Auth).filter(
                Auth.name.in_(auth_name_list),
                Auth.group_id == group_id
            ).delete(synchronize_session=False)

    # 查询用户拥有的权限
    @staticmethod
    def get_auth_list(group_id):
        '''
        :param user: UserModel实例
        :return:
        '''
        auth_list = db.session.query(Auth.name, Auth.module) \
            .filter_by(group_id=group_id).all()
        auth_list = [{'id': get_ep_id(auth[0]), 'name': auth[0], 'module': auth[1]} for auth in auth_list]
        return auth_list

    # 清空某个权限组的权限
    @staticmethod
    def delete_auths_by_group(group_id):
        with db.auto_commit():
            db.session.query(Auth).filter(
                Auth.group_id == group_id
            ).delete(synchronize_session=False)
