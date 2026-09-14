# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
  生成临时账号（用户及其登录身份）。
  提示：用户名、邮箱、微信openid 均为唯一约束，重复运行会报唯一约束错误。
"""
from app import create_app
from app.core.db import db
from app.libs.enums import ScopeEnum, ClientTypeEnum
from app.models.user import User
from app.models.identity import Identity

__author__ = 'Allen7D'

# (昵称, 用户名, 邮箱, 微信小程序 openid, 密码, 权限)
ACCOUNTS = [
    ('超级管理员', 'super', 'super@qq.com', 'wx111111', '123456', ScopeEnum.ADMIN.value),
    ('普通管理员', 'admin', 'admin@qq.com', 'wx222222', '123456', ScopeEnum.COMMON.value),
    ('用户', 'user', 'user@qq.com', 'wx333333', '123456', ScopeEnum.COMMON.value),
]

app = create_app()
with app.app_context():
    for nickname, username, email, openid, password, auth in ACCOUNTS:
        with db.auto_commit():
            user = User.create(commit=False, nickname=nickname, auth=auth)
            db.session.flush()  # 先分配 user.id，供下方身份关联使用
            # 用户名身份
            Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.USERNAME.value,
                            identifier=username, password=password, verified=1)
            # 邮箱身份
            Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.EMAIL.value,
                            identifier=email, password=password, verified=1)
            # 微信小程序 openid 身份
            Identity.create(commit=False, user_id=user.id, type=ClientTypeEnum.WX_MINA.value,
                            identifier=openid, verified=1)
    print('账号生成完毕：super/123456（超级管理员）、admin/123456（普通管理员）、user/123456（普通用户）')