# -*- coding: utf-8 -*-
"""
pytest 共享 fixture。
"""
import pytest

from app import create_app
from tests.utils import login

# fake.py 生成的固定测试账号(见 docs): super / 123456 为超级管理员(is_admin=True)
SUPER_ACCOUNT = 'super@qq.com'
SUPER_SECRET = '123456'


# scope="session" 是 pytest fixture 的作用域，表示这个 fixture 在整个 pytest 测试会话期间只创建一次，结果被所有测试复用。
@pytest.fixture(scope="session")
def super_admin_token():
    """超级管理员 token (super@qq.com/123456)，整个测试会话复用一次登录。

    集成测试用它访问 cms/admin 相关接口；避免每个测试重复打 DB 登录。
    """
    with create_app().test_client() as client:
        return login(client, SUPER_ACCOUNT, SUPER_SECRET)
