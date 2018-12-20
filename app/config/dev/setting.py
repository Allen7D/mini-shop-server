# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
__author__ = 'Alimazing'

TOKEN_EXPIRATION = 30 * 24 * 3600
SERVER_URL = '118.25.25.229'
IMG_PREFIX = SERVER_URL + '/static/images'
UPLOAD_FOLDER = 'app/static/uploads'
SWAGGER = {
	"swagger_version": "2.0",
	"info": {
		# "
		"title": "微信小程序商城: API",
		"version": "0.3.0",
		"description": "简要描述一下这个api文档的功能",
		"contact": {
			"responsibleOrganization": "Shema(聆听)",
			"responsibleDeveloper": "A粒麦子",
			"email": "bodanli159951@163.com",
			"url": "www.me.com"
		},
		"termsOfService": "http://me.com/terms"
	},
	"host": 'SERVER_URL', #"api.ivinetrue.com",
	"basePath": "/",  # base bash for blueprint registration
	"tags": [
		{
			"name": "banner",
			"description": "***tags可以去掉***"
		}
	],
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
