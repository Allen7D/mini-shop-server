# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/2.
  Flask 对配置项的限制，你必须保证命名全都大写，才能注入到current_app.config中
"""
import os

__author__ = 'Allen7D'

is_dev_mode = os.path.exists('app/config/dev.py')  # 'development' & 'product' (开发环境 or 生产环境)

# 应用于Swagger的URL，会自动添加协议前缀(http://或者https://)，因为会切换协议前缀
EXTERNAL_URL = 'server.mini-shop.ivinetrue.com'  # 外部（云服务器）地址
INTERNAL_URL = '0.0.0.0:8010'  # 内部（本地）地址
SERVER_URL = INTERNAL_URL if is_dev_mode else EXTERNAL_URL

IMG_PREFIX = SERVER_URL + '/static/images'
UPLOAD_FOLDER = 'app/static/uploads'

# flask-admin配置
FLASK_ADMIN_SWATCH = 'cerulean'

# Swagger配置
version = "0.3.0"  # 项目版本
description = """API接口分为cms版本和v1版本，大部分接口需要token权限才能访问。
访问之前，先使用/v1/token获取token，并将token放入Authorize中。
"""
EXTERNAL_SCHEMES = ["https", "http"]  # 外部（云服务器）支持 https 和 http 协议
INTERNAL_SCHEMES = ["http"]  # 内部只支持http
SERVER_SCHEMES = INTERNAL_SCHEMES if is_dev_mode else EXTERNAL_SCHEMES

SWAGGER = {
    "swagger_version": "2.0",
    "info": {
        "title": "微信小程序商城: API",
        "version": version,
        "description": description,
        "contact": {
            "responsibleOrganization": "Shema(聆听)",
            "responsibleDeveloper": "Allen7D",
            "email": "bodanli159951@163.com",
            "url": "http://ivinetrue.com"
        },
        "termsOfService": "http://ivinetrue.com"
    },
    "host": SERVER_URL,  # "api.ivinetrue.com",
    "basePath": "/",  # base bash for blueprint registration
    "tags": [],  # 在'/app/api/v1/__init__.py'定义
    "schemes": SERVER_SCHEMES,
    "operationId": "getmyData",
    "securityDefinitions": {
        'basicAuth': {
            'type': 'basic'
        }
    }
}

# SWAGGER的安全访问方式
specs_security = [
    {
        "basicAuth": []
    }
]

# all model by module for flask-admin
all_model_by_module = {
    'user': ['User'],
    'user_address': ['UserAddress'],
    'order': ['Order'],
    'banner': ['Banner'],
    'banner_item': ['BannerItem'],
    'theme': ['Theme'],
    'category': ['Category'],
    'product': ['Product'],
    'image': ['Image']
}

# all api by module(version)
all_api_by_module = {
    'v1': ['token', 'user', 'address', 'banner', 'theme', 'category', 'product', 'order', 'pay'],
    'cms': ['user', 'category', 'product', 'theme', 'file']
}

# 项目的github地址
GITHUB_URL = 'https://github.com/Allen7D/mini-shop-serve'
# 项目文档地址
DOC_URL = 'http://doc.mini-shop.ivinetrue.com'

# 临时token
tmp_token = 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4Mzk1MDE0NywiZXhwIjoxNTg2NTQyMTQ3fQ.eyJ1aWQiOjIsInR5cGUiOjEwMCwic2NvcGUiOiJBZG1pblNjb3BlIn0.k7QAXaa4Lm4w1CZZWCFulhJdNXhAdiSz9EA5LJWZpV1vjQ6OQUOng5vx2t2x-JHTywCVgJrP8W5frAopBNBDZg'
