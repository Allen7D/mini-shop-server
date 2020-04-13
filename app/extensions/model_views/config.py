# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/13.
"""
__author__ = 'Allen7D'

# flask-admin配置
FLASK_ADMIN_SWATCH = 'cerulean'

# all model by module for flask-admin
ALL_MODEL_BY_MODULE = {
    'user': ['User'],
    # 'user': {'name': '用户', 'modules': ['user.User', 'auth.Auth', 'group.Group', 'user_address.UserAddress']}
    'user_address': ['UserAddress'],
    'order': ['Order'],
    'banner': ['Banner'],
    'banner_item': ['BannerItem'],
    'theme': ['Theme'],
    'category': ['Category'],
    'product': ['Product'],
    'image': ['Image']
}
