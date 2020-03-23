# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/12.
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.api_docs.cms import theme as api_doc
from app.models.theme import Theme
from app.validators.forms import PaginateValidator

__author__ = 'Allen7D'

api = RedPrint(name='theme', description='主题管理', api_doc=api_doc, alias='cms_theme')


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_list():
    '''获取主题列表(分页)'''
    page_validator = PaginateValidator().validate_for_api()
    page = page_validator.page.data
    size = page_validator.size.data

    return Success()


@api.route('/<int:id>', methods=['PUT'])
@api.doc(auth=True)
@auth.login_required
def update_one(id):
    '''更新主题信息'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(auth=True)
@auth.login_required
def delete_one(id):
    '''删除某主题'''
    return Success(error_code=2)
