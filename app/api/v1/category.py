# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 类别接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import RedPrint
from app.extensions.api_docs.v1 import category as api_doc
from app.core.token_auth import auth
from app.models.category import Category
from app.libs.error_code import Success
from app.validators.forms import PaginateValidator

__author__ = 'Allen7D'

api = RedPrint(name='category', description='产品类别', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc()
def get_all_category():
    '''查询所有「产品类别」'''
    category_list = Category.query.all()
    return Success(category_list)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
def get_category_list():
    '''查询「产品类别」列表'''
    paginate = PaginateValidator().get_data()
    page = paginate.page
    size = paginate.size

    paginator = Category.query.paginate(page=page, per_page=size, error_out=False)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('', methods=['POST'])
@api.route_meta(auth='新增类别', module='类别')
@api.doc(auth=True)
@auth.group_required
def create_category():
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
