# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from app.models.user_address import UserAddress as UserAddressModel

__author__ = 'Allen7D'


class UserAddressDao():
    # 更新「配送信息」
    @staticmethod
    def update_address(id, user_id, **form):
        address = UserAddressModel.get_or_404(id=id, user_id=user_id)
        address.update(**form)

    # 删除「配送信息」
    @staticmethod
    def delete_address(id, user_id):
        address = UserAddressModel.get_or_404(id=id, user_id=user_id)
        address.delete()
