# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/11.
"""
__author__ = 'Allen7D'

# Swagger相关配置
description = """API接口分为cms版本和v1版本，大部分接口需要token权限才能访问。
访问之前，先使用/v1/token查询token，并将token放入Authorize中。
"""

'''
内部只支持http
外部（云服务器）支持 https 和 http 协议
'''
SWAGGER_TAGS = []  # 在'/app/api/__init__.py'中create_blueprint_list设置
SWAGGER = {
    "swagger_version": "2.0",
    "info": {
        "title": "微信小程序商城: API",
        "version": "0.3.0", # 项目版本
        "description": description,
        "contact": {
            "responsibleOrganization": "Shema(聆听)",
            "responsibleDeveloper": "Allen7D",
            "email": "bodanli159951@163.com",
            "url": "http://ivinetrue.com"
        },
        "termsOfService": "http://ivinetrue.com"
    },
    "host": '',
    "basePath": "/",  # base bash for blueprint registration
    "tags": SWAGGER_TAGS, # 接口在文档中的类别和顺序
    "schemes": ['http'], # 通信协议: http或https或多个，默认http
    "operationId": "getmyData",
    "securityDefinitions": {
        'basicAuth': {
            'type': 'basic'
        }
    }
}
