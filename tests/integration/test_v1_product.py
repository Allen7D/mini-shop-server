# _*_ coding: utf-8 _*_
"""
  商品/主题相关接口(v1) 集成测试。
"""
import pytest

from app import create_app, connect_db
from app.models.theme import Theme
from tests.utils import authorization


@pytest.fixture()
def app():
    """初始化测试应用并建立数据库连接。"""
    _app = create_app()
    _app.config.update(
        TESTING=True,
        SQLALCHEMY_TRACK_MODIFICATIONS=False  # 屏蔽 sql alchemy 的 FSADeprecationWarning
    )
    with _app.app_context():
        connect_db(_app)
    return _app


@pytest.fixture()
def client(app):  # fixture 之间也可以互相依赖，同样按名字注入
    """
    返回基于 app() 的测试客户端。
    相当于一个**"假的浏览器/HTTP 客户端"，但不真正启动服务器、不占端口**
    """
    return app.test_client()


def test_get_recent(app, client):
    """测试按 id 查询主题(theme)详情接口。

    - 先在数据库新建一个主题, 再请求 GET /v1/theme/1
    - 预期: 状态码 200; error_code=0; 返回的 data 中含 name 字段(即能查到刚创建的主题)
    """
    with app.app_context():
        Theme.create(name='1231', description='1231',
                     topic_img_id=1, head_img_id=1)

    rv = client.get('/v1/theme/1')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['error_code'] == 0
    # 刚创建的主题应能按 id 查到(接口数据里带 name 字段)
    assert 'name' in json_data['data']


def test_get_user_list(client, super_admin_token):
    """测试分页查询用户列表(cms/user)接口。

    - 请求: GET /cms/user/list?page=1&size=10, 携带 super 授权的请求头
    - 预期: 状态码 200; error_code=0; 返回数据中含用户列表 items
    """
    rv = client.get('/cms/user/list?page=1&size=10', headers={
        'Authorization': authorization(super_admin_token)
    })
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert json_data['error_code'] == 0
    assert 'items' in json_data['data']
