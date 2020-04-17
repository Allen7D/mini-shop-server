# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/17.
"""
from sqlalchemy import func
from flask import current_app

from app.core.db import db
from app.libs.enums import AtLeastEnum, ClientTypeEnum
from app.models.user import User as UserModel
from app.models.identity import Identity as IdentityModel
from app.libs.error_code import AtLeastOneClientException

__author__ = 'Allen7D'


class IdentityDao():
    # 绑定用户
    @staticmethod
    def bind(user_id, identifier, type):
        IdentityDao.create_identity(
            user_id=user_id,
            identifier=identifier,
            credential=None,
            type=type)

    # 解绑用户
    @staticmethod
    def unbind(user_id, type):
        identity_count = db.session.query(func.count(IdentityModel.user_id)).filter(
            IdentityModel.user_id == user_id).scalar()
        # 至少保留一种登录方式
        if identity_count <= AtLeastEnum.ONE.value:
            raise AtLeastOneClientException()
        IdentityDao.delete_identity(user_id, type)

    # 新建身份
    @staticmethod
    def create_identity(user_id, identifier, credential, type):
        # 判断是否是网站内部的身份类型
        if ClientTypeEnum(type) in current_app.config['CLINET_INNER_TYPES']:
            with db.auto_commit():
                attr = ClientTypeEnum(type).name.lower()
                user = UserModel.get(id=user_id)
                setattr(user, attr, identifier)
                user.save(commit=False)
                IdentityModel.create(commit=False, user_id=user_id, type=type,
                                     identifier=identifier, credential=credential)
        # 第三方平台，则无需修改用户信息
        else:
            IdentityModel.create(user_id=user_id, type=type, identifier=identifier)

    # 删除身份
    @staticmethod
    def delete_identity(user_id, type):
        '''删除时，需要判断type的类型
           因为username、mobile、email的解绑需要清除user表的对应字段
        '''
        user = UserModel.get(id=user_id)
        with db.auto_commit():
            # 判断是否是网站内部的身份类型
            if ClientTypeEnum(type) in current_app.config['CLINET_INNER_TYPES']:
                attr = ClientTypeEnum(type).name.lower()
                setattr(user, attr, None)
                user.save(commit=False)
            identity = IdentityModel.get_or_404(user_id=user_id, type=type)
            identity.hard_delete(commit=False)  # 硬删除
