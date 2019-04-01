# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/1/21.
"""
from functools import wraps

from flask import request
from werkzeug.contrib.cache import SimpleCache

__author__ = 'Allen7D'

class Limiter(object):
    cache = SimpleCache()

    def limited(self, callback):
        self.limited_callback = callback
        return callback

    def limit(self, key='', key_func=None, time_delta=60):
        def decorator(f):
            key_prefix = "limiter/"

            @wraps(f)
            def wrapper(*args, **kwargs):
                # global cache
                full_key = key_prefix + key_func() if key_func else key
                value = Limiter.cache.get(full_key)
                if not value:
                    Limiter.cache.set(full_key, time_delta, timeout=time_delta)
                    return f(*args, **kwargs)
                else:
                    return self.limited_callback()

            return wrapper

        return decorator

cache = SimpleCache()

def cached(timeout=5 * 60, key='view_%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            value = cache.get(cache_key)
            if value is None:
                value = f(*args, **kwargs)
                cache.set(cache_key, value, timeout=timeout)
            return value
        return decorated_function
    return decorator
