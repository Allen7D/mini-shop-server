# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/1/21.
"""
from functools import wraps
from werkzeug.contrib.cache import SimpleCache  # 新包地址 https://github.com/pallets/cachelib
from flask import request

__author__ = 'Allen7D'

cache = SimpleCache()


def cached(timeout=5 * 60, key='cached_{}_{}'):
	'''
	:param timeout: 缓存的秒数
	:param key: 缓存的key的格式
	:return:
	'''

	def decorator(f):
		@wraps(f)
		def decorated_function(*args, **kwargs):
			# 以 { key:value } 的形式存到内存
			query_args = dict(request.args.to_dict())
			body_args = request.get_json(silent=True) or {}
			req_args = {**query_args, **body_args}
			suffix = ''
			for (k, v) in req_args.items():
				suffix = suffix + '&{}={}'.format(k, v)
			cache_key = key.format(request.path, suffix)
			value = cache.get(cache_key)  # 获取
			if value is None:
				value = f(*args, **kwargs)
				cache.set(cache_key, value, timeout=timeout)  # 设置
			return value

		return decorated_function

	return decorator
