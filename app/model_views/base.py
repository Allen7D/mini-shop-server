# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/3.
"""
from flask_admin.contrib.sqla import ModelView as _ModelView
from sqlalchemy import func

__author__ = 'Allen7D'


class ModelView(_ModelView):
	column_exclude_list = ['create_time', 'update_time', 'delete_time', 'status']  # 隐藏字段
	page_size = 10  # 分页
	column_display_pk = True # 是否显示主键
	can_create = True  # 可新增, 默认True
	can_edit = True  # 可修改, 默认True
	can_delete = True  # 可删除, 默认True

	def __add__(self, other):
		self.column_exclude_list = list(set(self.column_exclude_list + other.column_exclude_list))

		return self

	# 对于查询，进行条件过滤
	def get_query(self):
		return self.session.query(self.model).filter(self.model.status == 1)

	# 对于查询统计，进行条件过滤
	def get_count_query(self):
		return self.session.query(func.count('*')).filter(self.model.status == 1)
