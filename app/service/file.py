# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/3/23.
"""
import os
from flask import current_app

__author__ = 'Allen7D'


class FileService():
    def __init__(self, file):
        self.prefix_path = current_app.config['UPLOAD_FOLDER']
        self.file = file

    def save(self, filename=None, prefix_path=None):
        '''
        :param filename: 文件名
        :param save_path: 默认路径为current_app.config['UPLOAD_FOLDER']
        :return:
        '''
        filename = filename if filename else self.file.filename
        prefix_path = prefix_path if prefix_path else self.prefix_path
        save_path = os.path.join(prefix_path, filename)
        self.file.save(save_path)
        return filename
