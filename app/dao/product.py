# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""

from sqlalchemy import desc

from app.core.db import db
from app.models.product import Product
from app.models.m2m import Product2Image
from app.libs.error_code import ProductException

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
        product = Product.get_or_404(id=id)
        product.delete()

    # 获取最近上架的商品
    @staticmethod
    def get_most_recent(count):
        return Product.query.order_by(desc(Product.create_time)) \
            .limit(count).all_by_wrap(wrap='items')

    # 获取某商品详情
    @staticmethod
    def get_product_detail(id):
        return Product.get_or_404(id=id).hide('category_id')

    # 查询某类别商品列表
    @staticmethod
    def get_list_by_category(category_id, page, size):
        paginator = Product.query \
            .filter_by(category_id=category_id) \
            .paginate(page=page, per_page=size, error_out=False)
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }

    # 排序商品图片
    @staticmethod
    def reorder_image(p_id, src_order, dest_order):
        '''
        :param p_id: 商品id
        :param src_order: 图片的原顺序
        :param dest_order: 图片的新顺序
        :return:
        '''
        [min, max] = sorted([src_order, dest_order])
        pending_reorder_list = Product2Image.query.filter(
            Product2Image.product_id == p_id,
            Product2Image.order.between(min, max)
        ).order_by(Product2Image.order.asc()).all()

        if len(pending_reorder_list) <= 1:
            raise ProductException(msg='该商品仅有一张图片，无法重新排序')
        
        # 往后移动(1,2,「3」,4,5 ==> 1,2,4,5,「3」)
        # 3放在5的位置(即prev_order为3，next_order为5)
        if src_order < dest_order:
            with db.auto_commit():
                src_obj = pending_reorder_list.pop(0) # 抛除首位
                dest_obj = pending_reorder_list[-1]
                src_obj.update(commit=False, order=dest_obj.order)
                # order向前移动(变小)
                for obj in pending_reorder_list:
                    obj.update(commit=False, order=obj.order-1)

        # 往后移动(1,2,「3」,4,5 ==> 「3」,1,2,4,5)
        # 3放在5的位置(即prev_order为3，next_order为1)
        if src_order >= dest_order:
            with db.auto_commit():
                src_obj = pending_reorder_list.pop() # 抛除末位
                dest_obj = pending_reorder_list[0]
                src_obj.update(commit=False, order=dest_obj.order)
                # order向后移动(变大)
                for obj in pending_reorder_list:
                    obj.update(commit=False, order=obj.order+1)
