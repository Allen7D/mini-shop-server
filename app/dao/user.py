# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from app.core.db import db
from app.libs.enums import ScopeEnum, ClientTypeEnum
from app.models.user import User as UserModel
from app.models.identity import Identity as IdentityModel

__author__ = 'Allen7D'


class UserDao():
    # 更改密码
    @staticmethod
    def change_password(uid, old_password, new_password):
        identity = IdentityModel.get_or_404(user_id=uid)  # 找到一个
        if identity.check_password(old_password):
            identity_list = IdentityModel.query.filter(
                IdentityModel.type.in_([
                    ClientTypeEnum.USERNAME.value,
                    ClientTypeEnum.EMAIL.value,
                    ClientTypeEnum.MOBILE.value]),
                IdentityModel.user_id == uid
            ).all()
            with db.auto_commit():
                for item in identity_list:
                    item.update(commit=False, password=new_password)

    # 重置密码
    @staticmethod
    def reset_password(uid, password):
        identity_list = IdentityModel.query.filter(
            IdentityModel.type.in_([
                ClientTypeEnum.USERNAME.value,
                ClientTypeEnum.EMAIL.value,
                ClientTypeEnum.MOBILE.value]),
            IdentityModel.user_id == uid
        ).all()
        with db.auto_commit():
            for item in identity_list:
                item.update(commit=False, password=password)

    # 站内注册(用户名、手机号、邮箱、密码)
    @staticmethod
    def create_user(form):
        with db.auto_commit():
            user = UserModel.create(
                commit=False,
                username=getattr(form, 'username', None),
                mobile=getattr(form, 'mobile', None),
                email=getattr(form, 'email', None),
                nickname=getattr(form, 'nickname', None),
                auth=ScopeEnum.COMMON.value
            )
            if (hasattr(form, 'username')):
                IdentityModel.abort_repeat(identifier=form.username, msg='该用户名已被使用，请重新输入新的用户名')
                IdentityModel.create(commit=False, user_id=user.id, type=ClientTypeEnum.USERNAME.value, verified=1,
                                     identifier=form.username, password=form.password)
            if (hasattr(form, 'mobile')):
                IdentityModel.abort_repeat(identifier=form.mobile, msg='手机号已被使用，请重新输入新的手机号')
                IdentityModel.create(commit=False, user_id=user.id, type=ClientTypeEnum.MOBILE.value,
                                     identifier=form.mobile, password=form.password)
            if (hasattr(form, 'email')):
                IdentityModel.abort_repeat(identifier=form.email, msg='邮箱已被使用，请重新输入新的邮箱号')
                IdentityModel.create(commit=False, user_id=user.id, type=ClientTypeEnum.EMAIL.value,
                                     identifier=form.email, password=form.password)

    @staticmethod
    def register_by_wx_mina(openid: str):
        """小程序注册"""
        with db.auto_commit():
            user = UserModel.create(commit=False)
            IdentityModel.create(
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
        return UserModel.create(**form)

    @staticmethod
    def register_by_wx_account():
        pass

    # 更新用户
    @staticmethod
    def update_user(uid, form):
        user = UserModel.query.filter_by(id=uid).first_or_404()
        identity_infos = []
        with db.auto_commit():
            if (hasattr(form, 'username')):
                identity_infos.append(
                    {'identifier': form.username, 'type': ClientTypeEnum.USERNAME.value, 'msg': '该用户名已被使用，请重新输入新的用户名'})
            if (hasattr(form, 'mobile')):
                identity_infos.append(
                    {'identifier': form.mobile, 'type': ClientTypeEnum.MOBILE.value, 'msg': '手机号已被使用，请重新输入新的手机号'})
            if (hasattr(form, 'email')):
                identity_infos.append(
                    {'identifier': form.email, 'type': ClientTypeEnum.EMAIL.value, 'msg': '邮箱已被使用，请重新输入新的邮箱号'})
            for item in identity_infos:
                IdentityModel.abort_repeat(identifier=item['identifier'], msg=item['msg'])
                identity = IdentityModel.get(user_id=uid, type=item['type'])
                if not identity:
                    IdentityModel.create(
                        commit=False, user_id=user.id, type=item['type'], identifier=item['identifier'])
                else:
                    identity.update(commit=False, identifier=item['identifier'])

            user.update(
                commit=False,
                username=getattr(form, 'username', None),
                mobile=getattr(form, 'mobile', None),
                email=getattr(form, 'email', None),
                nickname=getattr(form, 'nickname', None)
            )

    # 删除用户
    @staticmethod
    def delete_user(uid):
        user = UserModel.query.filter_by(id=uid).first_or_404()
        user.delete()

    # 更换权限组
    @staticmethod
    def change_group(uid, group_id):
        user = UserModel.get_or_404(id=uid)
        user.update(group_id=group_id)

    # 获取用户列表
    @staticmethod
    def get_user_list(page, size):
        paginator = UserModel.query \
            .filter_by(auth=ScopeEnum.COMMON.value) \
            .paginate(page=page, per_page=size, error_out=True)
        paginator.hide('user_address')
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }
