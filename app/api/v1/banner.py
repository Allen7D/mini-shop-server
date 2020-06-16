# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
  ↓↓↓ Banner接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import banner as api_doc
from app.models.banner import Banner
from app.libs.error_code import Success, BannerException

__author__ = 'Allen7D'

api = Redprint(name='banner', module='首页轮播图', api_doc=api_doc)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.banner_id'])
def get_banner(id):
    '''查询首页轮播图'''
    banner = Banner.query.filter_by(id=id).first_or_404(e=BannerException)
    return Success(banner)
