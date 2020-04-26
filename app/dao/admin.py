# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from app.libs.enums import ScopeEnum
from app.models.user import User

__author__ = 'Allen7D'


class AdminDao():
    # 查询管理员列表
    @staticmethod
    def get_admin_list(group_id, page, size):
        query_condition = {
            'auth': ScopeEnum.COMMON.value,
            'group_id': group_id  # 管理员(至少拥有权限组)
        } if group_id else {
            'auth': ScopeEnum.COMMON.value
        }
        user_list = User.query \
            .filter_by(**query_condition) \
            .paginate(page=page, per_page=size, error_out=False)

        return user_list

    # 新增管理员
    @staticmethod
    def create_admin(**form):
        User.abort_repeat(nickname=form.nickname.data, msg='用户名重复，请重新输入')
        User.create(auth=ScopeEnum.COMMON.value, **form.data)

    #
    @staticmethod
    def update_admin(uid, *form):
        user = User.get_or_404(id=uid, msg='用户不存在')

    @staticmethod
    def delete_admin(uid):
        user = User.get_or_404(id=uid, msg='用户不存在')
        user.hard_delete()