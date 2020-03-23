# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/2.
"""
__author__ = 'Allen7D'


upload_file = {
	"parameters": [
		{
			"name": "file",
			"in": "formData",
			"type": "file",
			"required": 'false'
		}
	],
	"responses": {
		"200": {
			"description": "上传文件成功",
			"examples": {}
		}
	}
}


upload_double_file = {
	"parameters": [
		{
			"name": "origin",
			"in": "formData",
			"type": "file",
			"required": 'false'
		},
		{
			"name": "comparer",
			"in": "formData",
			"type": "file",
			"required": 'false'
		}
	],
	"responses": {
		"200": {
			"description": "上传文件成功",
			"examples": {}
		}
	}
}


download_file = {
	"parameters": [
		{
			"file_name": "",
			"in": "path",
			"type": "string",
			"enum": ['Python面向对象编程指南.epub'],
			"default": 'Python面向对象编程指南.epub',
			"required": 'true'
		},
	],
	"responses": {
		"200": {
			"description": "下载文件成功",
			"examples": {}
		}
	}
}
