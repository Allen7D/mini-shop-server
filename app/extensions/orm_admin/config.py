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
    'identity': ['Identity'],
    # 'user': {'name': '用户', 'modules': ['user.User', 'auth.Auth', 'group.Group', 'address.Address']}
    'address': ['Address'],
    'order': ['Order'],
    'banner': ['Banner'],
    'banner_item': ['BannerItem'],
    'theme': ['Theme'],
    'category': ['Category'],
    'product': ['Product'],
    'image': ['Image'],
    'file': ['File'],
    'article': ['Article']
}
