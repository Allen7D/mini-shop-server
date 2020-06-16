# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
  ↓↓↓ 参数配置接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import config as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.config import Config
from app.libs.error_code import Success
from app.validators.forms import CreateConfigValidator, UpdateConfigValidator

__author__ = 'Allen7D'

api = Redprint(name='config', module='参数配置管理', api_doc=api_doc, alias='cms_config')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询参数配置列表', module='参数')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_config_list():
    '''查询参数配置列表'''
    page, size = paginate()
    paginator = Config.query.paginate(page=page, per_page=size, error_out=True)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
    })


@api.route('/<int:id>', methods=['GET'])
@api.route_meta(auth='查询参数配置', module='参数')
@api.doc(args=['path.config_id'], auth=True)
@auth.group_required
def get_config(id):
    '''查询参数配置'''
    config = Config.get_or_404(id=id)
    return Success(config)


@api.route('/key/<string:key>', methods=['GET'])
@api.route_meta(auth='查询参数配置(基于key)', module='参数')
@api.doc(args=['path.key'], auth=True)
@auth.group_required
def get_config_by_key(key):
    '''查询参数配置(基于key)'''
    config = Config.get_or_404(key=key)
    return Success(config)


@api.route('', methods=['POST'])
@api.route_meta(auth='新建参数配置', module='参数')
@api.doc(args=['body.name', 'body.key', 'body.value', 'body.type', 'body.remark'], auth=True)
@auth.group_required
def create_config():
    '''新建参数配置'''
    form = CreateConfigValidator().dt_data
    Config.create(**form)
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新参数配置', module='参数')
@api.doc(args=['path.config_id', 'body.name', 'body.key', 'body.value', 'body.type', 'body.remark'], auth=True)
@auth.group_required
def update_config(id):
    '''更新参数配置'''
    form = UpdateConfigValidator().dt_data
    config = Config.get_or_404(id=id)
    config.update(**form)
    return Success(config, error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.route_meta(auth='删除参数配置', module='参数')
@api.doc(args=['path.config_id'], auth=True)
@auth.group_required
def delete_config(id):
    '''删除参数配置'''
    config = Config.get_or_404(id=id)
    config.delete()
    return Success(error_code=2)
