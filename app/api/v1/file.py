# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/12/2.
  可以用来处理上传产品图片、Excel等
"""
from app.libs.redprint import RedPrint
from app.libs.success_code import Success

__author__ = 'Alimazing'


api = RedPrint(name='file', description='文件上传')

@api.route('/upload', methods=['POST'])
@api.doc()
def upload_file():
	'''文件上传'''
	return Success(123)
