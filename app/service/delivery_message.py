# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/23.
"""
import time
from datetime import datetime

from app.libs.error_code import OrderException
from app.service.wx_message import WxMessage

__author__ = 'Allen7D'


class DeliveryMessage(WxMessage):
    DELIVERY_MSG_ID = 'your template message id'

    def send_delivery_message(self, order, tpl_jump_page=''):
        if not order:
            raise OrderException()
        self.tlp_id = self.DELIVERY_MSG_ID
        self.form_id = order.prepay_id
        self.page = tpl_jump_page
        self.__prepare_message_data(order)
        return ''

    def __prepare_message_data(self, order):
        current_time = datetime.now()  # datetime.datetime(2020, 3, 23, 1, 44, 16, 703778)
        self.data = {
            'keyword1': {
                'value': '顺丰速运'
            },
            'keyword2': {
                'value': order.snap_name,
                'color': '#274088'
            },
            'keyword3': {
                'value': order.order_no
            },
            'keyword4': {
                'value': current_time.strftime("%Y-%m-%d %H:%M:%S")  # '2020-03-23 01:44:47'
            },
        }
