# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/8.
  print输出字体颜色: https://www.cnblogs.com/easypython/p/9084426.html
"""
import json
import time
from datetime import datetime
import logging
from logging.handlers import BaseRotatingHandler

from flask import g, request, _request_ctx_stack

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

    # 记录每次请求的性能
    @staticmethod
    def apply_request_log(app):
        @app.before_request
        def request_cost_time():
            g.request_start_time = time.time()
            g.request_time = lambda: "%.5f" % (time.time() - g.request_start_time)

        @app.after_request
        def log_response(res):
            message = '[%s] -> [%s] from:%s costs:%.3f ms' % (
                request.method,
                request.path,
                request.remote_addr,
                float(g.request_time()) * 1000
            )
            req_body = request.get_json() if request.get_json() else {}
            data = {
                'path': _request_ctx_stack.top.request.view_args,
                'query': request.args,
                'body': req_body
            }
            message += '\n\"data\": ' + json.dumps(data, indent=4, ensure_ascii=False)
            # 设置颜色开始(至多3类参数，以m结束)：\033[显示方式;前景色;背景色m
            print('\033[0;34m')
            if request.method in ('GET', 'POST', 'PUT', 'DELETE'):
                print(message)
            print('\033[0m')  # 终端颜色恢复
            return res
