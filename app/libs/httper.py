# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/22.
"""
__author__ = 'Alimazing'

import requests


class HTTP:
	@staticmethod
	def get(url, return_json=True):
		res = requests.get(url)
		if res.status_code != 200:
			return {} if return_json else ''
		return res.json() if return_json else res.text

