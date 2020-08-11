# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/8/11.
"""
from flask import current_app
from werkzeug.utils import secure_filename

from app.libs.enums import UrlFromEnum
from app.models.file import File
from app.dao.file import FileDao
from app.core.file import Uploader
from app.core.error import QiniuExcepition
from qiniu import Auth, put_data

__author__ = 'Allen7D'

class QiniuUploader(Uploader):
    # 定位文件所属的文件夹位置
    def locate(self, parent_id=0):
        self.parent_id = parent_id

    def upload(self):
        ret = []
        for single in self._file_storage:
            file_md5 = self._generate_md5(single.read())
            single.seek(0)
            file = File.query.filter_by(md5=file_md5).first()
            parent_folder = File.get_or_404(id=self.parent_id)
            if file and self.parent_id != file.parent_id:
                if not File.query.filter_by(parent_id=self.parent_id, md5=file_md5).first():
                    file = FileDao.copy_file(
                        dest_parent_id=self.parent_id,
                        src_file_id=file.id,
                        user_id=parent_folder.user_id
                    )
                    file = File.get(md5=file_md5)

            if not file:
                absolute_path, relative_path, uuid_filename = self._get_store_path(single.filename)
                # 上传到七牛云，获取存储地址
                path = self.save(single.filename, single.read())
                if path:
                    secure_filename(single.filename)
                    File.create(
                        parent_id=self.parent_id,
                        name=single.filename,
                        uuid_name=uuid_filename,
                        path=path,
                        extension=self._get_ext(single.filename),
                        size=self._get_size(single),
                        md5=file_md5,
                        _from=UrlFromEnum.NETWORK.value
                    )
                file = File.get(parent_id=self.parent_id, md5=file_md5)
            ret.append(file)
        return ret

    def save(self, filename, file):
        '''存储到七牛云'''
        config = current_app.config.get('QINIU')
        domain = config['DOMAIN'] # 所有上传文件的前缀地址
        bucket_name = config['BUCKET_NAME'] #要上传的空间
        q = Auth(access_key=config['ACCESS_KEY'], secret_key=config['SECRET_KEY']) # 构建鉴权对象
        token = q.upload_token(bucket_name, None, 3600)
        try:
            ret, info = put_data(token, None, file)
        except Exception as e:
            return False  # 配置的七牛云参数异常

        if info.status_code == 200:
            # 返回存储地址
            return domain + ret.get("key")
        else:
            return False