# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
  ↓↓↓ 字典管理接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import dict as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.dict import Dict
from app.libs.error_code import Success
from app.validators.forms import DictTypeValidator, UpdateDictValidator, CreateDictValidator

__author__ = 'Allen7D'

api = Redprint(name='dict', module='字典管理', api_doc=api_doc, alias='cms_dict')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询字典数据列表', module='字典数据')
@api.doc(args=['g.query.page', 'g.query.size', 'query.type'], auth=True)
@auth.group_required
def get_dict_list():
    '''查询字典数据列表'''
    page, size = paginate()
    type = DictTypeValidator().get_data('type')
    paginator = Dict.query.filter_by(type=type).paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/all', methods=['GET'])
@api.route_meta(auth='查询某类字典数据', module='字典数据')
@api.doc(args=['query.type'], auth=True)
@auth.group_required
def get_all_dict_by_type():
    '''查询某类字典数据'''
    type = DictTypeValidator().get_data('type')
    dict_datas = Dict.get_all(type=type)
    return Success({
        'items': dict_datas
    })


@api.route('/<int:id>', methods=['GET'])
@api.route_meta(auth='查询字典数据', module='字典数据')
@api.doc(args=['path.dict_id'], auth=True)
@auth.group_required
def get_dict(id):
    '''查询字典数据'''
    dict_data = Dict.get_or_404(id=id)
    return Success(dict_data)


@api.route('', methods=['POST'])
@api.route_meta(auth='新建字典数据', module='字典数据')
@api.doc(args=['body.order', 'body.label', 'body.value', 'body.type',
               'body.css_class', 'body.list_class',
               'body.is_default', 'body.status', 'body.remark'], auth=True)
@auth.group_required
def create_dict():
    '''新建字典数据'''
    form = CreateDictValidator().dt_data
    dict_data = Dict.create(**form)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新字典数据', module='字典数据')
@api.doc(args=['path.dict_id'], auth=True)
@auth.group_required
def update_dict(id):
    '''更新字典数据'''
    form = UpdateDictValidator().dt_data
    dict_data = Dict.get_or_404(id=id)
    dict_data.update(**form)
    return Success(dict_data, error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除字典数据', module='字典数据')
@api.doc(args=['path.dict_id'], auth=True)
@auth.group_required
def delete_dict(id):
    '''删除字典数据'''
    dict_data = Dict.get_or_404(id=id)
    dict_data.delete()
    return Success(error_code=2)
