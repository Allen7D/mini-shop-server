# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/12.
"""
import json
import base64

from flask import request, g

__author__ = 'Allen7D'


def write_token(data):
    obj = json.dumps(data)
    with open('token.json', 'w') as f:
        f.write(obj)


def get_token(key='token'):
    with open('token.json', 'r') as f:
        obj = json.loads(f.read())
        return obj[key]


def get_authorization():
    with open('token.json', 'r') as f:
        obj = json.loads(f.read())
        bytes_token = bytes(obj['token'] + ':', 'utf-8')
        encode_token = str(base64.b64encode(bytes_token)).strip('b\'')
        return 'Basic {}'.format(encode_token)


def format_print(json_data):
    message = '[%s] -> [%s] from:%s' % (
        request.method,
        request.path,
        request.remote_addr
    ) + '\n' + json.dumps(json_data, indent=4, ensure_ascii=False)
    print('>' * 22 + '[Test Response]' + '>' * 23)
    print(message)
    print('<' * 60)
