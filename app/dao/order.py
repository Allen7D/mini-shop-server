# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/16.
"""
from app.models.order import Order

__author__ = 'Allen7D'


class OrderDao():
    @staticmethod
    def get_summary_by_user(uid, page=1, size=10):
        paginator = Order.query.filter_by(user_id=uid) \
            .order_by(Order.create_time.desc()) \
            .paginate(page=page, per_page=size, error_out=True)
        paginator.hide('snap_items', 'snap_address', 'prepay_id')
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }

    @staticmethod
    def get_summary(page=1, size=10, start=None, end=None):
        paginator = Order.query.filter(
            Order.create_time.between(start, end)
        ).order_by(
            Order.create_time.desc()
        ).paginate(
            page=page,
            per_page=size,
            error_out=True
        )
        paginator.hide('snap_items', 'snap_address', 'prepay_id').append('create_time')
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }
