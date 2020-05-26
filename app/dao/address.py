# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from app.models.address import Address

__author__ = 'Allen7D'


class AddressDao():
    # 更新「配送信息」
    @staticmethod
    def update_address(id, user_id, **form):
        address = Address.get_or_404(id=id, user_id=user_id)
        address.update(**form)

    # 删除「配送信息」
    @staticmethod
    def delete_address(id, user_id):
        address = Address.get_or_404(id=id, user_id=user_id)
        address.delete()
