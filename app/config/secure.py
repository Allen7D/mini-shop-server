# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/2.
"""
__author__ = 'Allen7D'

DEBUG = True

# Token 配置
SECRET_KEY = 'But you, Lord , are a shield around me, my glory, the One who lifts my head high.' # 加密
TOKEN_EXPIRATION = 30 * 24 * 3600 # 有效期: 30天

# MySQL 数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:159951@localhost:3306/zerd?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = 'utf-8'
