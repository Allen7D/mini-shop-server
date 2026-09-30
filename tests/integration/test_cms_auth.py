# _*_ coding: utf-8 _*_
"""
  权限管理接口(cms/auth) 集成测试。
  需超级管理员权限(is_admin)。统一响应格式: {error_code, msg, data}
    - 新增成功:  error_code=1, code=201
    - 删除成功:  error_code=2, code=202
"""
from app import create_app
from tests.utils import authorization

app = create_app()


def test_append_auth_list(super_admin_token):
    """为指定用户组(group)追加权限列表。

    - 请求: PUT /cms/auth/append, 携带 group_id 和 auth_ids
    - 预期: 状态码 201 表示新增成功; error_code=1; 响应中包含 data 字段
    """
    with app.test_client() as client:
        rv = client.put('/cms/auth/append', headers={
            'Authorization': authorization(super_admin_token)
        }, json={
            'group_id': 5,
            'auth_ids': [1, 2, 3]
        })
        json_data = rv.get_json()
        assert rv.status_code == 201
        assert json_data['error_code'] == 1
        assert 'data' in json_data


def test_remove_auth_list(super_admin_token):
    """为指定用户组(group)删除权限列表。

    - 请求: PUT /cms/auth/remove, 携带 group_id 和 auth_ids
    - 预期: 状态码 202 表示删除成功; error_code=2; 响应中包含 data 字段
    """
    with app.test_client() as client:
        rv = client.put('/cms/auth/remove', headers={
            'Authorization': authorization(super_admin_token)
        }, json={
            'group_id': 5,
            'auth_ids': [1, 2, 3]
        })
        json_data = rv.get_json()
        assert rv.status_code == 202
        assert json_data['error_code'] == 2
        assert 'data' in json_data
