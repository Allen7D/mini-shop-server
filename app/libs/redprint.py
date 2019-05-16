# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""
from functools import wraps
from flasgger import swag_from

__author__ = 'Allen7D'


class RedPrint:
	def __init__(self, name, description, api_doc=None):
		self.name = name
		self.description = description
		self.mound = []
		self.api_doc = api_doc

	def route(self, rule, **options):
		def decorator(f):
			self.mound.append((f, rule, options))
			return f

		return decorator

	def register(self, bp, url_prefix=None):
		if url_prefix is None:
			url_prefix = '/' + self.name
		for f, rule, options in self.mound:
			endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
			bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

	'''
		装饰器执行的顺序(初始化会被执行至 f层；如同洋葱层)
		装饰器到底要的是什么？无非是对函数进行包裹 & 获取函数信息
		对装饰器完善; doc改为swag_from就更好理解
			对于第三方的装饰器，如何「扩张其功能」
			==> 能不能写一个修饰「装饰器」的函数
	'''
	def doc(self, *_args, **_kwargs):
		def decorator(f):
			specs = getattr(self.api_doc, f.__name__, None)
			if specs:
				specs['tags'] = [self.name]
				# 对f.__doc__处理
				if f.__doc__ and '\n\t' in f.__doc__:
					f.__doc__ = f.__doc__.split('\n\t')[0]

				@swag_from(specs=specs)
				@wraps(f)
				def wrapper(*args, **kwargs):
					return f(*args, **kwargs)

				return wrapper
			else:
				@wraps(f)
				def wrapper(*args, **kwargs):
					return f(*args, **kwargs)

				return wrapper

		return decorator

	@property
	def tag(self):
		return {
			'name': self.name,
			'description': self.description
		}
