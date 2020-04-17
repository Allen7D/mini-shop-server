# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""

from sqlalchemy import desc

from app.models.product import Product as ProductModel

__author__ = 'Allen7D'


class ProductDao():
    @staticmethod
    def create_product():
        pass

    @staticmethod
    def update_product():
        pass

    @staticmethod
    def delete_product(id):
        product = ProductModel.get_or_404(id=id)
        product.delete()

    # 获取最近上架的商品
    @staticmethod
    def get_most_recent(count):
        return ProductModel.query.order_by(desc(ProductModel.create_time)) \
            .limit(count).all_by_wrap(wrap='items')

    # 获取某商品详情
    @staticmethod
    def get_product_detail(id):
        return ProductModel.get_or_404(id=id).hide('category_id')

    # 查询某类别商品列表
    @staticmethod
    def get_list_by_category(category_id, page, size):
        paginator = ProductModel.query \
            .filter_by(category_id=category_id) \
            .paginate(page=page, per_page=size, error_out=False)
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }
