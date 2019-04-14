# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/16.
"""

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.banner import Banner
from app.validators.params import IDMustBePositiveInt
from app.libs.limiter import cached
from app.api_docs import banner as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='banner', description='首页轮播图', api_doc=api_doc)


@api.route('/<int:id>', methods=['GET'])
@api.doc()
@cached()
def get_banner(id):
	'''获取「首页轮播图」'''
	id = IDMustBePositiveInt().validate_for_api().id.data
	banner = Banner.get_banner_by_id(id=id)
	# banner.hide('description') # 临时隐藏
	return Success(banner)
