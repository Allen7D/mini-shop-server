# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/8.
  操作日志
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, SmallInteger, JSON

from app.core.db import BaseModel as Base, db
from app.libs.enums import OperTyepEnum

__author__ = 'Allen7D'


class OperLog(Base):
    __tablename__ = 'oper_log'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, comment='用户id')
    user_name = Column(String(50), comment='用户当时的昵称')
    module = Column(String(20), comment='系统模块')
    auth = Column(String(100), comment='访问哪个权限')
    _type = Column('type', SmallInteger, default=OperTyepEnum.OTHER.value, comment='操作类型')
    path = Column(String(50), comment='请求路径')
    endpoint = Column(String(100), comment='端点')
    request_method = Column(String(20), comment='请求方法(GET、PUT...)')
    request_param = Column(JSON, comment='请求参数: path、query、body')
    message = Column(String(450), comment='日志信息')
    status_code = Column(Integer, comment='请求的http返回码')
    create_time = Column('create_time', Integer, comment='创建时间')

    def __init__(self):
        # 时间戳
        self.create_time = int(round(datetime.now().timestamp()))

    def keys(self):
        self.hide('_type').append('type')
        return self.fields

    @property
    def type(self):
        type_dcit = {
            'OTHER': '其他',
            'CREATE': '新增',
            'UPDATE': '修改',
            'DELETE': '删除',
            'GRANT': '授权',
            'EXPORT': '导出',
            'IMPORT': '导入',
            'FORCE': '强退',
            'GEN_CODE': '生成代码',
            'CLEAN': '清空数据'
        }
        return type_dcit[OperTyepEnum(self._type).name]

    @type.setter
    def type(self, raw):
        self._type = raw
