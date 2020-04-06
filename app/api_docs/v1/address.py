# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/11/26.
"""
from app.libs.swagger_filed import BodyField

__author__ = 'Allen7D'

name = BodyField(name='name', type='string', description='姓名', enum=['董冬伟'])
mobile = BodyField(name='mobile', type='string', description='手机号', enum=['13758787058'])
email = BodyField(name='email', type='string', description='邮箱', enum=['462870781@qq.com'])
province = BodyField(name='province', type='string', description='省', enum=['浙江', '江苏', '上海'])
city = BodyField(name='city', type='string', description='市', enum=['杭州', '温州'])
country = BodyField(name='country', type='string', description='县区', enum=['萧山', '滨江'])
detail = BodyField(name='detail', type='string', description='详细地址', enum=['金地天逸三期2栋2单元701室'])