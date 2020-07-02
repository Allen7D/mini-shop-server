# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/30.
  ↓↓↓ Banner接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import banner as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.banner import Banner
from app.dao.banner import BannerDao
from app.libs.error_code import Success, BannerException

__author__ = 'Allen7D'

api = Redprint(name='banner', module='轮播图管理', api_doc=api_doc, alias='cms_banner')


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询轮播图列表', module='轮播图')
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.group_required
def get_banner_list():
    '''查询订单列表'''
    page, size = paginate()
    banner_list = BannerDao.get_list(page=page, size=size)
    return Success(banner_list)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.banner_id'])
def get_banner(id):
    '''查询轮播图'''
    banner = Banner.query.filter_by(id=id).first_or_404(e=BannerException)
    return Success(banner)
