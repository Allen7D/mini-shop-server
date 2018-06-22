# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/16.
"""

from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.banner import Banner
from app.validators.params import IDMustBePositiveInt

__author__ = 'Alimazing'

api = RedPrint('banner')


@api.route('/<id>', methods=['GET'])
def get_banner(id):
	id = IDMustBePositiveInt().validate_for_api().id.data
	banner = Banner.get_banner_by_id(id=id)
	# banner.hide('description') # 临时隐藏
	return Success(banner)
