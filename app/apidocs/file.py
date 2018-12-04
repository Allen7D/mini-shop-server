# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/12/2.
"""
__author__ = 'Alimazing'

upload_file = {
	"parameters": [
		{
			"name": "源文件",
			"in": "formData",
			"type": "file",
			"required": 'false'
		},
		{
			"name": "对比件",
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
