# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/13.
"""
from app.core.swagger_filed import IntegerQueryFiled, IntegerPathFiled, StringPathFiled, StringQueryFiled, BodyField

__author__ = 'Allen7D'

# Token登录相关
token_in_body = BodyField(name='token', type='string', description='Token', enum=['eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NjM2ODEzMCwiZXhwIjoxNTg4OTYwMTMwfQ.eyJ1aWQiOjEsInR5cGUiOjEwMCwic2NvcGUiOiLns7vnu5_nrqHnkIblkZgifQ.ovFuc5Ti5zGm5B7JS7AGOBBmrYHGCRsVk9OFAWb88LhY7v9Ubw4c_3xGik7K8Emd6_fz4Ho6Hk3GI1_fjcSIww'])
account_in_body = BodyField(name='account', type='string', description='用户名(此处可以传邮箱，或者微信登录的code)', enum=["666@qq.com"])
secret_in_body = BodyField(name='secret', type='string', description='密码', enum=["123456"])
type_in_body = BodyField(name='type', type='integer', description='登录方式', enum=[101])

# 分页相关
page = IntegerQueryFiled(name='page', description="第几页", enum=[1, 2, 3, 4, 5], default=1)
size = IntegerQueryFiled(name='size', description="每页大小", enum=[10, 20, 30, 40, 50, 100], default=10)


uid_in_path = IntegerPathFiled(
    name='uid', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)
uid_in_query = IntegerQueryFiled(
    name='uid', description="用户ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)

product_id_in_path = IntegerPathFiled(
    name='id', description="商品 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
product_id_in_query = IntegerQueryFiled(
    name='id', description="商品 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

category_id_in_path = IntegerPathFiled(
    name='id', description="类别 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
category_id_in_query = IntegerQueryFiled(
    name='id', description="类别 ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

theme_id_in_path = IntegerPathFiled(
    name='id', description="主题ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
theme_id_in_query = IntegerQueryFiled(
    name='id', description="主题ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

banner_id_in_path = IntegerPathFiled(
    name='id', description="轮播图ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
banner_id_in_query = IntegerQueryFiled(
    name='id', description="轮播图ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

order_id_in_path = IntegerPathFiled(
    name='id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
order_id_in_query = IntegerQueryFiled(
    name='id', description="订单ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

# 权限组
group_id_in_path = IntegerPathFiled(
    name='id', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
group_id_in_query = IntegerQueryFiled(
    name='id', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)
group_id_in_body = BodyField(
    name='group_id', type='string', description="权限组ID", enum=[1, 2, 3, 4, 5, 10, 15, 20])

# 权限
auth_ids_in_body = BodyField(name='auth_ids', type='array', description='权限ID列表',
                             enum=[[6, 7, 8], [12, 13, 14]])

# Password
password_in_body = BodyField(name='password', type='string', description='密码', enum=['123456'])
old_password_in_body = BodyField(name='old_password', type='string', description='密码', enum=['123456'])
new_password_in_body = BodyField(name='new_password', type='string', description='密码', enum=['123456'])
confirm_password_in_body = BodyField(name='confirm_password', type='string', description='密码', enum=['123456'])

# User
nickname_in_body = BodyField(name='nickname', type='string', description='昵称', enum=['Allen7D'])
username_in_body = BodyField(name='username', type='string', description='用户名', enum=['Allen7D'])
email_in_body = BodyField(name='email', type='string', description='邮箱', enum=['462870781@qq.com'])
mobile_in_body = BodyField(name='mobile', type='string', description='手机', enum=['13758787058'])

# Address
address_id_in_path = IntegerPathFiled(
    name='id', description="地址ID", enum=[1, 2, 3, 4, 5, 10, 15, 20, 100], required=True)

# File
file_id_in_path = IntegerPathFiled(
    name='id', description="文件ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)
file_id_in_query = IntegerQueryFiled(
    name='id', description="文件ID", enum=[1, 2, 3, 4, 5, 10, 100], default=1, required=True)

filename_in_query = StringQueryFiled(name='filename', description='文件名', enum=['virtualmachine1.png', 'cellphone.png'], required=True)
