# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/16.
  ↓↓↓ 服务监控接口 ↓↓↓
"""
from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import server as api_doc
from app.core.token_auth import auth
from app.libs.server import Server
from app.libs.error_code import Success

__author__ = 'Allen7D'

api = Redprint(name='server', module='服务监控', api_doc=api_doc, alias='cms_server')

@api.route('', methods=['GET'])
@api.route_meta(auth='查询服务器信息', module='服务监控')
@api.doc(auth=True)
# @auth.group_required
def get_server_info():
    '''查询服务器信息'''
    server = Server()
    return Success({
        'system': server.system, # 系统
        'cpu': server.cpu, # CPU
        'memory': server.memory, # 内存
        'disk': server.disk, # 硬盘
        'project': {} # 项目信息
    })