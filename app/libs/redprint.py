# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/31.
"""
from flasgger import swag_from

__author__ = 'Alimazing'


class RedPrint:
	def __init__(self, name):
		self.name = name
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

	def doc(self, specs=None, **options):
		if specs is not None:
			specs['tags'] = [self.name]
			return swag_from(specs=specs, **options)
