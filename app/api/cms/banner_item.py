# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/30.
  ↓↓↓ BannerItem接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import banner_item as api_doc
from app.core.token_auth import auth
from app.models.banner_item import BannerItem
from app.libs.error_code import Success, BannerException

__author__ = 'Allen7D'

api = Redprint(name='banner_item', module='轮播子图管理', api_doc=api_doc, alias='cms_banner_item')


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.banner_item_id'])
def get_banner_item(id):
    '''查询轮播子图'''
    banner_item = BannerItem.query.filter_by(id=id).first_or_404(e=BannerException)
    return Success(banner_item)


@api.route('', methods=['POST'])
@api.route_meta(auth='新建轮播子图', module='轮播子图')
@api.doc(args=[], auth=True)
@auth.group_required
def create_banner_item():
    '''新建轮播子图'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['PUT'])
@api.route_meta(auth='更新字典数据', module='字典数据')
@api.doc(args=['g.path.banner_item_id'], auth=True)
@auth.group_required
def update_banner_item(id):
    '''更新轮播子图'''
    return Success(error_code=1)


@api.route('/<int:id>', methods=['POST'])
@api.route_meta(auth='删除轮播子图', module='轮播子图')
@api.doc(args=['g.path.banner_item_id'])
@auth.group_required
def delete_banner_item(id):
    '''删除轮播子图'''
    banner_item = BannerItem.get_or_404(id=id)
    banner_item.delete()
    return Success(error_code=2)
