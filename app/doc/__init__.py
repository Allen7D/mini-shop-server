# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/11/5.
"""
from app.libs.param_filed import IntegerQueryFiled, StringQueryFiled, BooleanQueryFiled, \
	IntegerPathFiled, StringPathFiled, BooleanPathFiled

__author__ = 'Alimazing'

banner_id_in_path = StringPathFiled(
	name='id', description="banner id", enum=[1, 2], default=1, required=True).data

get_banner = {
	"parameters": [banner_id_in_path],
	"responses": {
		"200": {
			"description": "banner",
			"examples": {}
		}
	}
}
