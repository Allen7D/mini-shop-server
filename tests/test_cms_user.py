# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/12.
"""
from app import create_app
from tests.utils import get_authorization

__author__ = 'Allen7D'

app = create_app()


def test_get_user_list():
    with app.test_client() as client:
        rv = client.get('/cms/user/list?page=1&size=10', headers={
            'Authorization': get_authorization()
        })
        json_data = rv.get_json()
        print(json_data)


def test_get_user():
    with app.test_client() as client:
        rv = client.get('/cms/user/2', headers={
            'Authorization': get_authorization()
        })
        json_data = rv.get_json()
        print(json_data)


test_get_user_list()
test_get_user()
