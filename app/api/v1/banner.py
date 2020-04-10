# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
  ↓↓↓ Banner接口 ↓↓↓
"""
from app.libs.error_code import Success, BannerException
from app.libs.redprint import RedPrint
from app.models.banner import Banner
from app.api_docs.v1 import banner as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='banner', description='首页轮播图', api_doc=api_doc)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.banner_id'])
def get_banner(id):
    '''查询首页轮播图'''
    banner = Banner.query.filter_by(id=id).first_or_404(e=BannerException)
    return Success(banner)
