# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/18.
"""
from app.models.file import File

__author__ = 'Allen7D'

class FileDao():
    @staticmethod
    def create_folder(parent_id, filename):
        '''
        :param parent_id: 父级目录ID
        :param filename: 文件名
        :return:
        '''
        File.abort_repeat(parent_id=parent_id, name=filename, msg='文件名重复，请重命名!')
        File.create(parent_id=parent_id, name=filename)
