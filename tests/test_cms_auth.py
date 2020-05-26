# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/13.
"""
from app import create_app
from tests.utils import get_authorization

__author__ = 'Allen7D'

app = create_app()


def test_create_auth_list():
    with app.test_client() as client:
        rv = client.post('/cms/auth/append', headers={
            'Authorization': get_authorization()
        }, json={
            'group_id': 5,
            'auth_ids': [1, 2, 3]
        })
        json_data = rv.get_json()
        print(json_data)


def test_delete_auth_list():
    with app.test_client() as client:
        rv = client.post('/cms/auth/remove', headers={
            'Authorization': get_authorization()
        }, json={
            'group_id': 5,
            'auth_ids': [1, 2, 3]
        })
        json_data = rv.get_json()
        print(json_data)


test_create_auth_list()
test_delete_auth_list()
