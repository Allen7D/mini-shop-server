# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/30.
"""
from app.models.banner import Banner
__author__ = 'Allen7D'


class BannerDao(object):
    @staticmethod
    def get_list(page, size):
        paginator = Banner.query.filter_by() \
            .paginate(page=page, per_page=size, error_out=True)
        paginator.hide('items')
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }