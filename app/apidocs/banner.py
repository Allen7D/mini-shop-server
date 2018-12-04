# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/11/26.
"""
from app.libs.swagger_filed import StringPathFiled

__author__ = 'Alimazing'

banner_id_in_path = StringPathFiled(
	name='id', description="banner id", enum=['1'], default='1', required=True).data

get_banner = {
	"parameters": [banner_id_in_path],
	"responses": {
		"200": {
			"description": "轮播图",
			"examples": {}
		}
	}
}
