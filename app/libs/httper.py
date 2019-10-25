# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/6/22.
"""
import requests
import os
from uuid import uuid1

__author__ = 'Allen7D'

# os.getcwd() 获取当前工作目录，执行「python命令」所在的目录
dir_name = {
	'avatar': os.getcwd() + '/app/static/avatars',
}


class HTTP:
	@staticmethod
	def get(url, return_json=True):
		res = requests.get(url)
		if res.status_code != 200:
			return {} if return_json else ''
		return res.json() if return_json else res.text

	@staticmethod
	def download_pic(url, type='avatar'):
		'''下载图片，并生成「32位随机不重复的字符串 + .jpeg」
		其中，uuid来生成机器唯一标识
		:param url: 图片的url地址
		:param type: 保存的路径(基于图片用途的类别: 头像)
		:return: 图片的命名.jpeg
		'''
		file_name = ''
		if (type == 'avatar'):
			file_name = uuid1().hex + '.jpeg'
			file_path = dir_name[type] + '/' + file_name

		with open(file_path, 'wb') as f:
			res = requests.get(url)
			f.write(res.content)
		return file_name
