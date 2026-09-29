# -*- coding: utf-8 -*-

import pytest

from app import create_app
from app.libs.url import local_asset_url


@pytest.fixture
def app():
    return create_app()


def test_builds_full_url_with_subfolder_and_filename(app):
    with app.test_request_context(path='/v1/file', base_url='http://127.0.0.1:5000/'):
        result = local_asset_url('files', 'img/a.png')
    assert result == 'http://127.0.0.1:5000/static/files/img/a.png'


def test_handles_host_without_trailing_slash(app):
    # request.host_url 通常以 / 结尾，函数负责去掉，避免出现 //static
    with app.test_request_context(path='/v1/file', base_url='http://example.com/'):
        result = local_asset_url('files', 'img/a.png')
    assert result == 'http://example.com/static/files/img/a.png'


def test_handles_host_with_optional_port(app):
    with app.test_request_context(path='/v1/file', base_url='http://192.168.10.80:8010/'):
        result = local_asset_url('files', 'img/a.png')
    assert result == 'http://192.168.10.80:8010/static/files/img/a.png'