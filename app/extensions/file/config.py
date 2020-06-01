# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/11.
"""
__author__ = 'Allen7D'

# 文件相关配置
UPLOAD_FOLDER = 'app/static/files'
IMG_FOLDER = 'static/images'

FILE = {
    "STORE_DIR": UPLOAD_FOLDER,  # 'app/assets',
    "SINGLE_LIMIT": 1024 * 1024 * 2,
    "TOTAL_LIMIT": 1024 * 1024 * 20,
    "NUMS": 10,
    "INCLUDE": set(['jpg', 'jpeg', 'png'] +
                   ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf', 'md'] +
                   ['mp3', 'mp4'] +
                   ['zip']),
    "EXCLUDE": set([])
}
