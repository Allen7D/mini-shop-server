# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from collections import namedtuple

from app.core.db import db
from app.libs.enums import ScopeEnum, ClientTypeEnum
from app.models.user import User
from app.models.identity import Identity
from app.dao.identity import IdentityDao

__author__ = 'Allen7D'


class UserDao():
    inner_identity_types = [ClientTypeEnum.USERNAME.value, ClientTypeEnum.EMAIL.value, ClientTypeEnum.MOBILE.value] # 内部登录类型: username、email、mobile
    # 更改密码
    @staticmethod
    def change_password(uid, old_password, new_password):
        identity = Identity.get_or_404(user_id=uid)  # 找到一个
        if identity.check_password(old_password):
            identity_list = Identity.query.filter(
                Identity.type.in_(UserDao.inner_identity_types),
                Identity.user_id == uid
            ).all()
            with db.auto_commit():
                for item in identity_list:
                    item.update(commit=False, password=new_password)

    # 重置密码
    @staticmethod
    def reset_password(uid, password):
        identity_list = Identity.query.filter(
            Identity.type.in_(UserDao.inner_identity_types),
            Identity.user_id == uid
        ).all()
        with db.auto_commit():
            for item in identity_list:
                item.update(commit=False, password=password)

    # 站内注册(用户名、手机号、邮箱、密码)，可以同时绑定多个
    @staticmethod
    def create_user(form: namedtuple):
        # form在validator层已经校验了必须包含username
        with db.auto_commit():
            # 用户昵称(姓名)，可以重名
            user = User.create(commit=False, nickname=getattr(form, 'nickname', None), auth=ScopeEnum.COMMON.value)
            password = form.password
            # 以下多个绑定可以同步进行
            # 用户登录时的账号(必定)
            if (hasattr(form, 'username')):
                identifier = form.username
                Identity.abort_repeat(identifier=identifier, msg='该用户名已被使用，请重新输入新的用户名')
                Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.USERNAME.value, verified=1,
                                identifier=identifier, password=password)

            # 用户登录时的手机号(可选)
            if (hasattr(form, 'mobile')):
                identifier = form.mobile
                Identity.abort_repeat(identifier=identifier, msg='手机号已被使用，请重新输入新的手机号')
                Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.MOBILE.value, verified=1,
                                identifier=identifier, password=password)
            # 用户登录时的邮箱号(可选)
            if (hasattr(form, 'email')):
                identifier = form.email
                Identity.abort_repeat(identifier=identifier, msg='邮箱已被使用，请重新输入新的邮箱号')
                Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.EMAIL.value, verified=1,
                                identifier=identifier, password=password)

    @staticmethod
    def register_by_wx_mina(openid: str):
        """小程序注册"""
        with db.auto_commit():
            user = User.create(commit=False)
            Identity.create(
                commit=False, user_id=user.id,
                type=ClientTypeEnum.WX_MINA.value,
                identifier=openid, verified=1
            )
        return user

    @staticmethod
    def register_by_wx_open(form):
        """微信第三方注册
        :param form: 属性包含(openid、unionid、nickname、headimgurl)
        """
        return User.create(**form)

    @staticmethod
    def register_by_wx_account():
        pass

    # 更新用户
    @staticmethod
    def update_user(uid, form):
        # 第1步: 核对需修改的信息(用户名、手机号、邮箱)
        identity_infos = []
        if (hasattr(form, 'username')):
            identity_infos.append(
                {'identifier': form.username, 'type': ClientTypeEnum.USERNAME.value, 'msg': '该用户名已被使用，请重新输入新的用户名'})
        if (hasattr(form, 'mobile')):
            identity_infos.append(
                {'identifier': form.mobile, 'type': ClientTypeEnum.MOBILE.value, 'msg': '手机号已被使用，请重新输入新的手机号'})
        if (hasattr(form, 'email')):
            identity_infos.append(
                {'identifier': form.email, 'type': ClientTypeEnum.EMAIL.value, 'msg': '邮箱已被使用，请重新输入新的邮箱号'})
        # 第2步: 修改用户信息
        with db.auto_commit():
            # 第2.1步: 获取用户信息
            user = User.query.filter_by(id=uid).first_or_404()
            credential = IdentityDao.get_credential(user_id=uid)
            # 第2.2步: 修改用户昵称
            if hasattr(form, 'nickname'):
                user.update(commit=False, nickname=form.nickname)
            # 第2.3步: 依次修改用户身份信息(用户名、手机号、邮箱)
            for item in identity_infos:
                Identity.abort_repeat(identifier=item['identifier'], msg=item['msg'])
                IdentityDao.update_identity(
                    commit=False, user_id=uid, identifier=item['identifier'], credential=credential, type=item['type']
                )

    # 更新头像
    @staticmethod
    def set_avatar(id, avatar):
        '''
        :param id: 用户id
        :param avatar: 头像url
        :return:
        '''
        with db.auto_commit():
            user = User.get(id=id)
            user._avatar = avatar

    # 删除用户
    @staticmethod
    def delete_user(uid):
        user = User.query.filter_by(id=uid).first_or_404()
        with db.auto_commit():
            Identity.query.filter_by(user_id=user.id).delete(commit=False)
            user.delete(commit=False)

    # 更换权限组
    @staticmethod
    def change_group(uid, group_id):
        user = User.get_or_404(id=uid)
        user.update(group_id=group_id)

    # 获取用户列表
    @staticmethod
    def get_user_list(page, size):
        paginator = User.query \
            .filter_by(auth=ScopeEnum.COMMON.value) \
            .paginate(page=page, per_page=size, error_out=True)
        paginator.hide('address')
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }
