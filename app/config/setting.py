# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
import os

__author__ = 'Alimazing'

is_dev_mode = os.path.exists('app/config/dev.py') # 'development' & 'product' (开发环境 or 生产环境)

TOKEN_EXPIRATION = 30 * 24 * 3600
EXTERNAL_URL = 'api.ivinetrue.com' # 外部（远程）地址
INTERNAL_URL = '0.0.0.0:8080' # 内部（本地）地址
SERVER_URL = INTERNAL_URL if is_dev_mode else EXTERNAL_URL
IMG_PREFIX = SERVER_URL + '/static/images'
UPLOAD_FOLDER = 'app/static/uploads'
SWAGGER = {
	"swagger_version": "2.0",
	"info": {
		"title": "微信小程序商城: API",
		"version": "0.3.0",
		"description": "简要描述一下这个api文档的功能",
		"contact": {
			"responsibleOrganization": "Shema(聆听)",
			"responsibleDeveloper": "Allen7D",
			"email": "bodanli159951@163.com",
			"url": "http://ivinetrue.com"
		},
		"termsOfService": "http://ivinetrue.com"
	},
	"host": SERVER_URL, #"api.ivinetrue.com",
	"basePath": "/",  # base bash for blueprint registration
	"tags": [],
	"schemes": [
		"http",
		"https"
	],
	"operationId": "getmyData",
	"securityDefinitions": {
		'basicAuth': {
			'type': 'basic'
		}
	}
}
