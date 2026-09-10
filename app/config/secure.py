# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/2.
  敏感配置(密钥、密码等)一律从环境变量读取，禁止硬编码明文。
"""
import os

__author__ = 'Allen7D'

DEBUG = False

# Token 配置
SECRET_KEY = os.environ.get('SECRET_KEY')  # 加密
TOKEN_EXPIRATION = 30 * 24 * 3600  # 有效期: 30天

# MySQL 数据库配置
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_ENCODING = 'utf-8'
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 屏蔽 sql alchemy 的 FSADeprecationWarning

# 微信·小程序
APP_ID = os.environ.get('APP_ID')
APP_SECRET = os.environ.get('APP_SECRET')
LOGIN_URL = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'

# 微信·开放平台(OPEN)登录[第三方(Third-Party)]
OPEN_APP_ID = os.environ.get('OPEN_APP_ID')
OPEN_APP_SECRET = os.environ.get('OPEN_APP_SECRET')
OPEN_SCOPE = 'snsapi_login'
OPEN_STATE = os.environ.get('OPEN_STATE')
REDIRECT_URI = 'https%3a%2f%2fapi.ivinetrue.com%2ftoken%2fuser'
OPEN_AUTHORIZE_URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={0}&redirect_uri={1}&response_type=code&scope={2}&state={3}#wechat_redirect'.format(
    OPEN_APP_ID, OPEN_APP_SECRET, OPEN_SCOPE, OPEN_STATE
)
OPEN_ACCESS_TOKEN_URL = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={0}&secret={1}&code={2}&grant_type=authorization_code'
OPEN_USER_INFO_URL = 'https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh_CN'

# 微信·公众平台(Account)·服务号登录
ACCOUNT_APP_ID = os.environ.get('ACCOUNT_APP_ID')
ACCOUNT_APP_SECRET = os.environ.get('ACCOUNT_APP_SECRET')
REDIRECT_URI = 'https%3a%2f%2fwww.ivinetrue.com'