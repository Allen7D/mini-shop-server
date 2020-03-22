# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/23.
"""
__author__ = 'Allen7D'


class WxMessage():
    def __init__(self):
        self.__send_url = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=%s'
        self.__touser = None
        self.__color = 'black'

        self.tlp_id = ''
        self.page = ''
        self.form_id = ''
        self.page = {}
        self.emphasis_keyword = ''
