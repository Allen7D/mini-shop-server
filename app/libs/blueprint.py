# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/10/25.
"""
from flask import Blueprint as _Blueprint

__author__ = 'Allen7D'


class Blueprint(_Blueprint):
	'''新增rp_list属性'''
	def __init__(self, name, import_name, static_folder=None,
				 static_url_path=None, template_folder=None,
				 url_prefix=None, subdomain=None, url_defaults=None,
				 root_path=None):
		self.rp_list = []
		super(Blueprint, self).__init__(name, import_name, static_folder,
										static_url_path, template_folder,
										url_prefix, subdomain, url_defaults,
										root_path)

	@property
	def tags(self):
		'''
		Swagger API 文档分类
		数组中的顺序代表 Swagger 中的顺序
		'''
		return [api.tag for api in self.rp_list]

	def register_redprint(self, rp_list):
		self.rp_list = rp_list
		for api in self.rp_list:
			api.register(self)
		return self
