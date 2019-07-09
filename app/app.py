# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/13.
"""
from datetime import date
from flask import Flask as _Flask, _request_ctx_stack
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


__author__ = 'Allen7D'


class JSONEncoder(_JSONEncoder):
	def default(self, o):
		if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
			return dict(o)
		if isinstance(o, date):
			return o.strftime('%Y-%m-%d')
		raise ServerError()


class Flask(_Flask):
	json_encoder = JSONEncoder

	def dispatch_request(self):
		req = _request_ctx_stack.top.request
		if req.routing_exception is not None:
			self.raise_routing_exception(req)
		rule = req.url_rule

		if getattr(rule, 'provide_automatic_options', False) \
				and req.method == 'OPTIONS':
			return self.make_default_options_response()

		return self.view_functions[rule.endpoint](**req.view_args)