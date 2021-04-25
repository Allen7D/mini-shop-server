# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/6.
"""
from app.core.db import db
from app.models.theme import Theme
from app.models.product import Product
from app.libs.error_code import ThemeException, ThemeNotFound, ProductNotFound

__author__ = 'Allen7D'


class ThemeDao():
    @staticmethod
    def get_theme_detail(id):
        theme_detail = Theme.get_or_404(id=id, e=ThemeException)
        return theme_detail.append('products')

    @staticmethod
    def append_product(t_id, p_id):
        theme, product = ThemeDao._check_relation_exist(t_id, p_id)
        with db.auto_commit():
            theme.products.append(product)

    @staticmethod
    def delete_product(t_id, p_id):
        theme, product = ThemeDao._check_relation_exist(t_id, p_id)
        with db.auto_commit():
            theme.products.remove(product)

    @staticmethod
    def _check_relation_exist(t_id, p_id):
        theme = Theme.get_or_404(id=t_id, e=ThemeNotFound)
        product = Product.get_or_404(id=p_id, e=ProductNotFound)
        return theme, product
