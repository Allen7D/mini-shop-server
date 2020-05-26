# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/8.
"""
from datetime import datetime
import logging
from logging.handlers import BaseRotatingHandler

__author__ = 'Allen7D'


class Logger():
    def __init__(self, app):
        self.app = app
        self.register_log()

    def register_log(self):
        self.app.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        logging.basicConfig(level=logging.DEBUG)
        filename = datetime.now().strftime("%Y-%m-%d")
        handler = BaseRotatingHandler(filename, mode='a', encoding='UTF-8', delay=False)
        handler.setFormatter(formatter)

        if not self.app.debug:
            self.app.logger.addHandler(handler)
