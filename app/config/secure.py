# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/4/2.
"""
__author__ = 'Alimazing'

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:159951@localhost:3306/zerd?charset=utf8'
SECRET_KEY = 'But you, Lord , are a shield around me, my glory, the One who lifts my head high.'
SWAGGER = {
	"swagger_version": "2.0",
	"info": {
		"title": "微信小程序商城 API",
		"version": "0.1.1",
		"description": "简要描述一下这个api文档的功能",
		"contact": {
			"responsibleOrganization": "Shema(聆听)",
			"responsibleDeveloper": "A粒麦子",
			"email": "bodanli159951@163.com",
			"url": "www.me.com"
		},
		"termsOfService": "http://me.com/terms"
	},
	"host": "localhost:5001",
	"basePath": "/",  # base bash for blueprint registration
	"tags": [
		{
			"name": "banner",
			"description": "banner的数据"
		}
	],
	"schemes": [
		"http",
		"https"
	],
	"operationId": "getmyData",
	"securityDefinitions": {
		"token": {
			"type": "apiKey",
			"name": "token",
			"in": "header"
		}
	}
}
