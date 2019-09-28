# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/12.
"""
from werkzeug.exceptions import HTTPException
from werkzeug.contrib.fixers import ProxyFix
from flask_script import Manager, Server

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'Allen7D'

app = create_app()

@app.errorhandler(Exception)
def framework_error(e):
	if isinstance(e, APIException):
		return e
	elif isinstance(e, HTTPException):
		code = e.code
		msg = e.description
		error_code = 1007
		return APIException(code, error_code, msg)
	else:
		if not app.config['DEBUG']:
			return ServerError() # 未知错误(统一为服务端异常)
		else:
			raise e


app.wsgi_app = ProxyFix(app.wsgi_app)
manager = Manager(app)
manager.add_command("run", Server())

if __name__ == '__main__':
	manager.run()
