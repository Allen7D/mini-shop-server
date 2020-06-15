# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
  ↓↓↓ 字典管理接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import dict as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.dict_type import DictType
from app.models.dict_data import DictData
from app.libs.error_code import Success

__author__ = 'Allen7D'

from app.validators.forms import DictTypeValidator

api = Redprint(name='dict', description='字典管理', api_doc=api_doc, alias='cms_dict')


@api.route('/type/list', methods=['GET'])
@api.route_meta(auth='查询字典类型列表', module='字典数据')
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


@api.route('/data/list', methods=['GET'])
@api.route_meta(auth='查询字典类型列表', module='字典数据')
@api.doc(args=['g.query.page', 'g.query.size', 'query.type'], auth=True)
@auth.group_required
def get_dict_data_list():
    '''查询字典类型列表'''
    page, size = paginate()
    type = DictTypeValidator().get_data('type')
    paginator = DictData.query.filter_by(type=type).paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/data/type/<string:type>', methods=['GET'])
@api.route_meta(auth='查询某类字典数据', module='字典数据')
@api.doc(args=['path.type'], auth=True)
@auth.group_required
def get_dict_data_by_type(type):
    '''查询某类字典的数据'''
    dict_datas = DictData.get_all(type=type)
    return Success({
        'items': dict_datas
    })
