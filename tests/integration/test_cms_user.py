# _*_ coding: utf-8 _*_
"""
  用户管理接口(cms/user) 集成测试。
"""
import pytest

from app import create_app
from tests.utils import authorization


@pytest.fixture()
def app():
    return create_app()


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_user_list(client, super_admin_token):
    """测试分页查询用户列表接口。

    - 请求: GET /cms/user/list?page=1&size=10, 携带超级管理员 token
    - 预期: 状态码 200; error_code=0; 返回分页信息 current_page/total 及用户列表 items
    """
    auth = authorization(super_admin_token)
    rv = client.get('/cms/user/list?page=1&size=10',
                    headers={'Authorization': auth})
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['error_code'] == 0
    assert json_data['data']['current_page'] == 1
    assert 'total' in json_data['data']
    assert 'items' in json_data['data']


def test_get_user(client, super_admin_token):
    """测试按 id 查询单个用户详情。

    - 先用 /v1/user 拿到 super 自己的 id, 再查询 /cms/user/{id} 校验返回一致
    - 预期: 状态码 200; error_code=0; 返回的用户 id 与请求的 uid 相同
    """
    auth = authorization(super_admin_token)
    # 用 v1/user 拿 super 自己的 id，再查 cms/user/{id}
    me = client.get(
        '/v1/user', headers={'Authorization': auth}).get_json()['data']
    uid = me['id']
    rv = client.get(f'/cms/user/{uid}', headers={'Authorization': auth})
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['error_code'] == 0
    assert json_data['data']['id'] == uid
