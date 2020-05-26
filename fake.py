# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
from app import create_app
from app.core.db import db
from app.models.user import User

__author__ = 'Allen7D'

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.openid = '999'
        user.email = '999@qq.com'
        user.nickname = '超级管理员'
        user.username = 'super'
        user.auth = 2
        user.password = '123456'
        db.session.add(user)

    with db.auto_commit():
        # 创建一个普通管理员
        user = User()
        user.openid = '777'
        user.email = '777@qq.com'
        user.nickname = '普通管理员'
        user.username = 'admin'
        user.auth = 1
        user.password = '123456'
        db.session.add(user)

    with db.auto_commit():
        # 创建一个用户
        user = User()
        user.openid = '111'
        user.email = '111@qq.com'
        user.nickname = '我是用户'
        user.username = 'user'
        user.auth = 1
        user.password = '123456'
        db.session.add(user)
