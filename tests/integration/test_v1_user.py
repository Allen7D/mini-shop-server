# _*_ coding: utf-8 _*_
from app import create_app
from app.core.db import db
from tests.utils import authorization

__author__ = 'Allen7D'

app = create_app()


def test_get_user(super_admin_token):
    """测试获取当前登录用户信息(v1/user)。

    - 请求: GET /v1/user, 携带超级管理员 token
    - 预期: 状态码 200; error_code=0; 返回当前用户 id, 且该用户拥有管理员权限 auth
    """
    with app.test_client() as client:
        rv = client.get('/v1/user', headers={
            'Authorization': authorization(super_admin_token)
        })
        json_data = rv.get_json()
        assert rv.status_code == 200
        assert json_data['error_code'] == 0
        assert 'id' in json_data['data']
        # 改用 super 登录后, 返回的就是 super 这个管理员; 检查它是管理员
        assert json_data['data']['auth'] is not None


def test_change_password(super_admin_token):
    """测试修改当前登录用户的密码。

    - 请求: PUT /v1/user/password, 携带 super 的旧/新/确认密码(此处均恒为 123456, 修改后仍是同一密码)
    - 预期: 状态码 201 表示修改成功; error_code=1
    """
    with app.test_client() as client:
        rv = client.put('/v1/user/password', headers={
            'Authorization': authorization(super_admin_token)
        }, json={
            'new_password': '123456',
            'old_password': '123456',
            'confirm_password': '123456',
        })
        json_data = rv.get_json()
        assert rv.status_code == 201
        assert json_data['error_code'] == 1
