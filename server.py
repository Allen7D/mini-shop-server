# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
try:
    from werkzeug.contrib.fixers import ProxyFix
except ImportError:
    from werkzeug.middleware.proxy_fix import ProxyFix
from flask_script import Manager, Server

from app import create_app

__author__ = 'Allen7D'

app = create_app()

app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app)
manager.add_command("run", Server())

if __name__ == '__main__':
    manager.run()
