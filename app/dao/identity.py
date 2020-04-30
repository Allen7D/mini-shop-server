# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/17.
"""
from sqlalchemy import func
from flask import current_app

from app.core.db import db
from app.libs.enums import AtLeastEnum, ClientTypeEnum
from app.models.user import User
from app.models.identity import Identity
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
        identity_count = db.session.query(func.count(Identity.user_id)).filter(
            Identity.user_id == user_id).scalar()
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
                user = User.get(id=user_id)
                attr = ClientTypeEnum(type).name.lower()
                setattr(user, attr, identifier)
                Identity.create(commit=False, user_id=user_id, type=type,
                                identifier=identifier, credential=credential)
                user.save(commit=False)
        # 第三方平台，则无需修改用户信息
        else:
            Identity.create(user_id=user_id, type=type, identifier=identifier)

    # 更新身份
    @staticmethod
    def update_identity(commit=True, user_id=None, identifier=None, credential=None, type=None):
        identity = Identity.get(user_id=user_id, type=type)
        if identity:
            identity.update(commit=commit,
                            identifier=identifier, credential=credential)
        else:
            Identity.create(commit=commit, user_id=user_id, type=type,
                            identifier=identifier, credential=credential)

    # 删除身份
    @staticmethod
    def delete_identity(user_id, type):
        '''删除时，需要判断type的类型
           因为username、mobile、email的解绑需要清除user表的对应字段
        '''
        user = User.get(id=user_id)
        with db.auto_commit():
            # 判断是否是网站内部的身份类型
            if ClientTypeEnum(type) in current_app.config['CLINET_INNER_TYPES']:
                attr = ClientTypeEnum(type).name.lower()
                setattr(user, attr, None)
                user.save(commit=False)
            identity = Identity.get_or_404(user_id=user_id, type=type)
            identity.hard_delete(commit=False)  # 硬删除

    # 获取加密后的密码
    @staticmethod
    def get_credential(user_id):
        credential, = db.session.query(Identity._credential).filter(
            Identity.user_id == user_id,
            Identity.type.in_([
                ClientTypeEnum.USERNAME.value,
                ClientTypeEnum.EMAIL.value,
                ClientTypeEnum.MOBILE.value]),
            Identity._credential != None
        ).first()
        return credential