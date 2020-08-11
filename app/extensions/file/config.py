# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/11.
"""
__author__ = 'Allen7D'

# 文件相关配置
UPLOAD_FOLDER = 'app/static/files'
IMG_FOLDER = 'static/images'

FILE = {
    "STORE_DIR": UPLOAD_FOLDER,  # 文件的存储路径(主目录),
    "SINGLE_LIMIT": 1024 * 1024 * 100,  # 单个文件的大小
    "TOTAL_LIMIT": 1024 * 1024 * 500,  # 总文件(多文件上传)的大小
    "NUMS": 10,
    "INCLUDE": set(['jpg', 'jpeg', 'png', 'gif'] +
                   ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'pdf', 'md'] +
                   ['mp3'] +
                   ['mp4', 'wmv'] +
                   ['zip']),
    "EXCLUDE": set([])
}

### 七牛云相关配置 ###

# 七牛云SDK地址 https://developer.qiniu.com/kodo/sdk/1242/python#upload-flow
QINIU = dict(
    DOMAIN='', # 所有文件的链接地址
    #  Access Key 和 Secret Key
    ACCESS_KEY='Access_Key',
    SECRET_KEY='Secret_Key',
    # 上传的空间(在七牛云上预先配置)
    BUCKET_NAME='Bucket_Name',
)
