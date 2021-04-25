# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/12.
"""
from app import create_app
from tests.utils import write_token, get_token, format_print

__author__ = 'Allen7D'

app = create_app()


def test_get_token():
    with app.test_client() as client:
        rv = client.post('/v1/token', json={
            "account": "999@qq.com",
            "secret": "123456",
            "type": 101
        })
        json_data = rv.get_json()
        format_print(json_data)
        write_token(json_data['data'])
        assert json_data['data']['token'] is not None
        assert rv.status_code == 200


def test_decrypt_token():
    with app.test_client() as client:
        rv = client.post('/v1/token/verify', json={
            'token': get_token()
        })
        json_data = rv.get_json()
        format_print(json_data)


test_get_token()
test_decrypt_token()
