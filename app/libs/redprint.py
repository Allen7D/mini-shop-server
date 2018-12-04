# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/31.
"""
from functools import wraps
from flasgger import swag_from

from app import apidocs

__author__ = 'Alimazing'


class RedPrint:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.mound = []

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

	def doc(self, *ty_args, **ty_kwargs):
		def decorator(f):
			specs = getattr(apidocs, f.__name__)
			specs['tags'] = [self.name]

			@swag_from(specs=specs)
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
