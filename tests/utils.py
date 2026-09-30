# _*_ coding: utf-8 _*_
"""
  集成测试工具。

  说明：早期版本把 token 持久化到共享的 token.json，导致测试之间存在
  顺序耦合(test_get_token 会覆盖其它测试读取的 token)。现已改为在每个
  测试内自行登录获取 token，不再依赖磁盘上的共享文件。
"""
import base64


def login(client, account: str, secret: str, login_type: int = 101) -> str:
    """登录并返回 token 字符串。

    :param client: Flask 测试客户端(test_client)，用于发起登录请求。
    :param account: 登录账号，邮箱登录时传邮箱地址。
    :param secret: 登录密码。
    :param login_type: 登录方式。101 = 邮箱登录。

    :return: 登录成功后返回的 token 字符串(token 取自响应 data.token)。

    :raises AssertionError: 登录接口必须返回 200，否则断言失败并携带响应内容。
    """
    rv = client.post('/v1/token', json={
        'account': account,
        'secret': secret,
        'type': login_type
    })
    assert rv.status_code == 200, f'登录失败: {rv.get_json()}'
    return rv.get_json()['data']['token']


def authorization(token: str) -> str:
    """把 token 编码成 Basic auth 请求头(Basic base64(token:))。

    :param token: 登录接口返回的 token 字符串。

    :return: Basic auth 请求头字符串。
    """
    raw = base64.b64encode(bytes(token + ':', 'utf-8')).decode()
    return 'Basic ' + raw
