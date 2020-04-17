# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""

from app.core.db import db
from app.models.group import Group as GroupModel
from app.models.auth import Auth as AuthModel
from app.models.user import User as UserModel
from app.core.auth import find_auth_module, get_ep_name
from app.core.error import Forbidden

__author__ = 'Allen7D'


class GroupDao():
    @staticmethod
    def create_group(name, auth_ids, info):
        '''
        :param name: 权限组名
        :param auth_ids: 权限ids
        :param info: 权限组名描述
        :return:
        '''
        auth_list = [get_ep_name(auth_id) for auth_id in auth_ids]  # 权限名列表
        with db.auto_commit():
            group = GroupModel.create(name=name, info=info, commit=False)
            db.session.flush()
            for auth in auth_list:
                meta = find_auth_module(auth)
                if meta:
                    AuthModel.create(auth=meta.name, module=meta.module, group_id=group.id, commit=False)

    @staticmethod
    def update_group(id, name, info):
        '''
        :param id: 权限组id
        :param name: 权限组名
        :param info: 权限组名描述
        :return:
        '''
        group = GroupModel.get_or_404(id=id, msg='分组不存在，更新失败')
        group.update(name=name, info=info)

    @staticmethod
    def delete_group(id):
        '''
        :param id: 权限组id
        :return:
        '''
        group = GroupModel.get_or_404(id=id, msg='分组不存在，删除失败')
        if UserModel.get(group_id=id):
            raise Forbidden(msg='分组下存在用户，不可删除')

        # 删除group拥有的权限
        AuthModel.query.filter_by(group_id=id).delete()
        group.delete()
