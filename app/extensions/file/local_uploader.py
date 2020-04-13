# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/4/11.
"""
from werkzeug.utils import secure_filename

from app.models.file import File
from app.core.file import Uploader

__author__ = 'Allen7D'


class LocalUploader(Uploader):

    def upload(self):
        ret = []
        self.mkdir_if_not_exists()
        for single in self._file_storage:
            file_md5 = self._generate_md5(single.read())
            single.seek(0)
            file = File.query.filter_by(md5=file_md5).first()
            if not file:
                absolute_path, relative_path, uuid_filename = self._get_store_path(single.filename)
                secure_filename(single.filename)
                single.save(absolute_path)
                File.create(
                    name=single.filename,
                    uuid_name=uuid_filename,
                    path=relative_path,
                    extension=self._get_ext(single.filename),
                    size=self._get_size(single),
                    md5=file_md5
                )
                file = File.get(md5=file_md5)
            ret.append(file)
        return ret
