# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/14.
"""
from flask import current_app
from flask.json import dumps

__author__ = 'Allen7D'


def jsonify(*args, **kwargs):
	indent = None
	separators = (',', ':')

	if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] or current_app.debug:
		indent = 2
		separators = (', ', ': ')

	if args and kwargs:
		raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
	elif len(args) == 1:  # single args are passed directly to dumps()
		data = args[0]
	else:
		data = args or kwargs
	return current_app.response_class(
		dumps(data, indent=indent, separators=separators) + '\n',
		mimetype=current_app.config['JSONIFY_MIMETYPE']
	).json
