# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
import unittest

from app import db, create_app, connect_db
from app.models.theme import Theme
from app.models.product import Product as ProductModel
from app.models.user import User as UserModel
from tests.utils import format_print, get_authorization

__author__ = 'Allen7D'


class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        app = create_app()
        app.config.update(
            TESTING=True,
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:159951@localhost:3306/test?charset=utf8',
            SQLALCHEMY_ENCODING='utf-8',
            SQLALCHEMY_TRACK_MODIFICATIONS = False  # 屏蔽 sql alchemy 的 FSADeprecationWarning
        )
        cls.app = app
        cls.client = app.test_client()
        with cls.app.app_context():
            connect_db(app)

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')
        # with self.app.app_context():
        #     db.session.remove()
        #     db.drop_all()

    def test_get_recent(self):
        with self.app.app_context():
            theme = Theme.create(name='1231', description='1231', topic_img_id=1, head_img_id=1)

        with self.client as client:
            rv = client.get('/v1/theme/1')
            json_data = rv.get_json()
            format_print(json_data)

    def test_get_user_list(self):
        # with self.app.app_context():
        #     UserModel.create(email='999@qq.com', username='super', auth=2, password='123456')

        with self.client as client:
            rv = client.get('/cms/user/list?page=1&size=10', headers={
                'Authorization': get_authorization()
            })
            json_data = rv.get_json()
            format_print(json_data)


if __name__ == '__main__':
    unittest.main()
