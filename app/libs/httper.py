# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/22.
"""
import requests

__author__ = 'Allen7D'


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        res = requests.get(url)
        if res.status_code != 200:
            return {} if return_json else ''
        return res.json() if return_json else res.text