# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/26.
"""
from app.libs.swagger_filed import BodyAttr

__author__ = 'Allen7D'

name = BodyAttr('name', 'string', '姓名', ['董冬伟'])
mobile = BodyAttr('mobile', 'string', '手机号', ['13758787058'])
email = BodyAttr('email', 'string', '邮箱', ['462870781@qq.com'])
province = BodyAttr('province', 'string', '省', ['浙江', '江苏', '上海'])
city = BodyAttr('city', 'string', '市', ['杭州', '温州'])
country = BodyAttr('country', 'string', '县区', ['萧山', '滨江'])
detail = BodyAttr('detail', 'string', '详细地址', ['金地天逸三期2栋2单元701室'])