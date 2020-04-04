# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 类别接口 ↓↓↓
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.category import Category
from app.libs.token_auth import auth
from app.api_docs.v1 import category as api_doc
from app.validators.forms import PaginateValidator

__author__ = 'Allen7D'

api = RedPrint(name='category', description='产品类别', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc()
def get_category_all():
    '''获取所有产品的分类'''
    categories = Category.get_all_categories()
    return Success(categories)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_category_list():
    '''获取类别列表(分页)'''
    page_validator = PaginateValidator().validate_for_api()
    page = page_validator.page.data
    size = page_validator.size.data

    paginator = Category.query.filter_by().paginate(page=page, per_page=size, error_out=False)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:id>', methods=['POST'])
@api.route_meta(auth='新增类别', module='类别')
@api.doc(auth=True)
@auth.group_required
def create_category(id):
    '''新增类别'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新类别', module='类别')
@api.doc(auth=True)
@auth.group_required
def update_category(id):
    '''更新类别信息'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除类别', module='类别')
@api.doc(auth=True)
@auth.group_required
def delete_category(id):
    '''删除类别'''
    return Success(error_code=2)
