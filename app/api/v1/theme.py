# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/17.
  ↓↓↓ 主题接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import theme as api_doc
from app.core.token_auth import auth
from app.models.theme import Theme
from app.dao.theme import ThemeDao
from app.libs.error_code import Success
from app.core.validator import BaseValidator
from app.validators.forms import PaginateValidator, IDCollectionValidator

__author__ = 'Allen7D'

api = Redprint(name='theme', description='主题', api_doc=api_doc)


@api.route('', methods=['GET'])
@api.doc(args=['theme_ids'])
def get_simple_list():
    '''基于一组id的主题
    只查询存在的id，不存在的则不返回结果
    :arg /theme?ids=id1,id2,id3,...
    :return: 一组theme模型
    '''
    ids = IDCollectionValidator().validate_for_api().ids.data
    themes = Theme.query.filter(Theme.id.in_(ids)).all()
    return Success({
        'items': themes
    })


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.theme_id'])
def get_complex_one(id):
    '''查询主题详情
    :param id: 专题theme的id
    :return: 专题theme的详情
    '''
    theme = ThemeDao.get_theme_detail(id=id)
    return Success(theme)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_theme_list():
    '''查询主题列表(分页)'''
    validator = PaginateValidator().nt_data
    page, size = validator.page, validator.size
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
@api.doc(args=['g.path.theme_id'], auth=True)
@auth.group_required
def delete_theme(id):
    '''删除主题'''
    return Success(error_code=2)


@api.route('/<int:id>/product', methods=['POST'])
@api.route_meta(auth='添加商品到主题', module='主题')
@api.doc(args=['g.path.theme_id', 'g.query.product_id'], auth=True)
@auth.group_required
def append_product(id):
    '''添加商品到主题'''
    product_id = BaseValidator.get_args_json().product_id
    ThemeDao.append_product(t_id=id, p_id=product_id)
    return Success(error_code=1)


@api.route('/<int:id>/product', methods=['DELETE'])
@api.route_meta(auth='删除商品从主题', module='主题')
@api.doc(args=['g.path.theme_id', 'g.query.product_id'], auth=True)
@auth.group_required
def delete_product(id):
    '''删除商品从主题'''
    product_id = BaseValidator.get_args_json().product_id
    ThemeDao.delete_product(t_id=id, p_id=product_id)
    return Success(error_code=2)
