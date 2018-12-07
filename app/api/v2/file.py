# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/12/2.
  可以用来处理上传产品图片、Excel等
"""
import os

from flask import send_from_directory

from app.libs.redprint import RedPrint
from app.libs.success_code import Success

__author__ = 'Alimazing'

# 改变「当前工作目录」到「static目录下」(指定的路径)
# folder_path = '../../../static/files/'
# os.chdir(folder_path)

api = RedPrint(name='file', description='文件上传')

@api.route('/upload', methods=['POST'])
@api.doc()
def upload_file():
	'''文件上传'''
	return Success(123)

@api.route('/download/<string:file_name>', methods=['GET'])
@api.doc()
def download_file(file_name):
	'''文件下载'''
	print('file_name', file_name)
	return Success(file_name)
	# return send_from_directory(file_name, file_name, mimetype='application/octet-stream')