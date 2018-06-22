# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/12.
"""
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'Alimazing'

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
			return ServerError()
		else:
			raise e

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
