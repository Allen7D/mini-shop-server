# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
  ↓↓↓ 字典管理接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import dict_type as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.dict_type import DictType
from app.libs.error_code import Success
from app.validators.forms import UpdateDictTypeValidator, CreateDictTypeValidator

__author__ = 'Allen7D'

api = Redprint(name='dict/type', module='字典类型', api_doc=api_doc, alias='cms_dict_type')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询字典类型列表', module='字典类型')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_dict_type_list():
    '''查询字典类型列表'''
    page, size = paginate()
    paginator = DictType.query.paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:id>', methods=['GET'])
@api.route_meta(auth='查询字典类型', module='字典类型')
@api.doc(args=['path.type_id'], auth=True)
@auth.group_required
def get_dict_type(id):
    '''查询字典类型'''
    dict_type = DictType.get_or_404(id=id)
    return Success(dict_type)


@api.route('', methods=['POST'])
@api.route_meta(auth='新建字典数据', module='字典类型')
@api.doc(args=['body.name', 'body.type', 'body.status', 'body.remark'], auth=True)
@auth.group_required
def create_dict_type():
    '''新建字典类型'''
    form = CreateDictTypeValidator().dt_data
    DictType.create(**form)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新字典数据', module='字典类型')
@api.doc(args=['path.type_id',
               'body.name', 'body.type', 'body.status', 'body.remark'], auth=True)
@auth.group_required
def update_dict_type(id):
    '''更新字典类型'''
    form = UpdateDictTypeValidator().dt_data
    dict_type = DictType.get_or_404(id=id)
    dict_type.update(**form)
    return Success(dict_type, error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除字典类型', module='字典类型')
@api.doc(args=['path.type_id'], auth=True)
@auth.group_required
def delete_dict_type(id):
    '''删除字典类型'''
    dict_type = DictType.get_or_404(id=id)
    dict_type.delete()
    return Success(error_code=2)
