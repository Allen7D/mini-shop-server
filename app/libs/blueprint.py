# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2019/10/25.
"""
from flask import Blueprint as _Blueprint

__author__ = 'Allen7D'


class Blueprint(_Blueprint):

    def __init__(self, name, import_name, static_folder=None,
                 static_url_path=None, template_folder=None,
                 url_prefix=None, subdomain=None, url_defaults=None,
                 root_path=None):
        super(Blueprint, self).__init__(name, import_name, static_folder,
                                        static_url_path, template_folder,
                                        url_prefix, subdomain, url_defaults,
                                        root_path)

    def register_redprint_list(self, rp_list):
        for api in rp_list:
            api.register(self)
        return self
