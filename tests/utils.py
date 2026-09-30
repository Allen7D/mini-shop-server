# _*_ coding: utf-8 _*_
"""
  集成测试工具。

  说明：早期版本把 token 持久化到共享的 token.json，导致测试之间存在
  顺序耦合(test_get_token 会覆盖其它测试读取的 token)。现已改为在每个
  测试内自行登录获取 token，不再依赖磁盘上的共享文件。
"""
import base64


def login(client, account: str, secret: str, login_type: int = 101) -> str:
    """登录并返回 token 字符串。"""
    rv = client.post('/v1/token', json={
        'account': account,
        'secret': secret,
        'type': login_type
    })
    assert rv.status_code == 200, f'登录失败: {rv.get_json()}'
    return rv.get_json()['data']['token']


def authorization(token: str) -> str:
    """把 token 编码成 Basic auth 请求头(Basic base64(token:))。"""
    raw = base64.b64encode(bytes(token + ':', 'utf-8')).decode()
    return 'Basic ' + raw
