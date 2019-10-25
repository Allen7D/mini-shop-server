# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/2.
"""
import os

__author__ = 'Allen7D'

is_dev_mode = os.path.exists('app/config/dev.py') # 'development' & 'product' (开发环境 or 生产环境)

EXTERNAL_URL = 'server.mini-shop.ivinetrue.com' # 外部（云服务器）地址
INTERNAL_URL = '0.0.0.0:8010' # 内部（本地）地址
SERVER_URL = INTERNAL_URL if is_dev_mode else EXTERNAL_URL

EXTERNAL_SCHEMES = ["https", "http"] # 外部（云服务器）支持 https 和 http 协议
INTERNAL_SCHEMES = ["http"] # 内部只支持http
SERVER_SCHEMES = INTERNAL_SCHEMES if is_dev_mode else EXTERNAL_SCHEMES

IMG_PREFIX = SERVER_URL + '/static/images'
UPLOAD_FOLDER = 'app/static/uploads'
VERSION = "0.3.0" # 项目版本
SWAGGER = {
	"swagger_version": "2.0",
	"info": {
		"title": "微信小程序商城: API",
		"version": VERSION,
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
	"tags": [], # 在'/app/api/v1/__init__.py'定义
	"schemes": SERVER_SCHEMES,
	"operationId": "getmyData",
	"securityDefinitions": {
		'basicAuth': {
			'type': 'basic'
		}
	}
}
