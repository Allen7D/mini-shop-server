# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 主题接口 ↓↓↓
"""
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.api_docs.v1 import theme as api_doc
from app.models.theme import Theme
from app.validators.forms import PaginateValidator, IDCollectionValidator

__author__ = 'Allen7D'

api = RedPrint(name='theme', description='主题', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['theme_ids'])
def get_simple_list():
    '''基于一组id的主题\n\t
    :arg /theme?ids=id1,id2,id3,...
    :return: 一组theme模型
    '''
    ids = IDCollectionValidator().validate_for_api().ids.data
    theme = Theme.get_themes(ids=ids)
    return Success(theme)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.theme_id'])
def get_complex_one(id):
    '''主题详情接口\n\t
    :param id: 专题theme的id
    :return: 专题theme的详情
    '''
    theme_detail = Theme.get_theme_detail(id=id)
    return Success(theme_detail)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_theme_list():
    '''查询主题列表(分页)'''
    page_validator = PaginateValidator().validate_for_api()
    page = page_validator.page.data
    size = page_validator.size.data
    paginator = Theme.query.filter_by().paginate(page=page, per_page=size, error_out=False)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('', methods=['POST'])
@api.route_meta(auth='新增主题', module='主题')
@api.doc(auth=True)
@auth.group_required
def create_theme():
    '''新增主题'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新主题', module='主题')
@api.doc(auth=True)
@auth.group_required
def update_theme(id):
    '''更新主题信息'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除主题', module='主题')
@api.doc(auth=True)
@auth.group_required
def delete_theme(id):
    '''删除主题'''
    return Success(error_code=2)
