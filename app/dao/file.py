# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/18.
"""
from app.core.db import db
from app.models.file import File
from app.libs.utils import TreeNode, Tree

__author__ = 'Allen7D'


class FolderNode(TreeNode):
    def __init__(self, id=None, parent_id=None, name=None, **kwargs):
        super(FolderNode, self).__init__(id=id, parent_id=parent_id)
        self.name = name

    def keys(self):
        attrs = super(FolderNode, self).keys()
        return attrs + ('name',)


class FolderTree(Tree):
    def __init__(self, root=None):
        super(FolderTree, self).__init__(root, nodeType=FolderNode)


class FileDao():
    # 新建文件夹
    @staticmethod
    def create_folder(parent_id, filename):
        '''
        :param parent_id: 父级目录ID
        :param filename: 文件名
        :return:
        '''
        File.abort_repeat(parent_id=parent_id, name=filename, msg='文件名重复，请重命名!')
        File.create(parent_id=parent_id, name=filename)

    # 重命名文件或文件夹
    @staticmethod
    def rename_file(file_id, new_filename):
        file = File.get_or_404(id=file_id)
        File.abort_repeat(parent_id=file.parent_id, name=new_filename, msg='文件名重复，请重命名!')
        file.update(name=new_filename)

    # 批量删除文件或文件夹
    @staticmethod
    def delete_files(ids):
        with db.auto_commit():
            db.session.query(File).filter(
                File.id.in_(ids),
            ).delete(synchronize_session=False)

    # 批量移动文件或文件夹
    @staticmethod
    def move_files(dest_parent_id, file_ids):
        '''
        :param dest_parent_id: 目标父级目录ID
        :param file_id: 文件ID
        :return:
        '''
        file_list = File.query.filter(File.id.in_(file_ids)).all()
        # 如果不重名则可以复制
        with db.auto_commit():
            for file in file_list:
                File.abort_repeat(parent_id=dest_parent_id, name=file.name, extension=file.extension,
                                  msg='文件名重复，无法移动！')
                file.update(parent_id=dest_parent_id, commit=False, )

    # 复制文件或文件夹
    @staticmethod
    def copy_file(dest_parent_id, src_file_id):
        '''
        :param dest_parent_id: 目标父级目录ID
        :param src_file_id: 源文件ID
        :return:
        '''
        src_file = File.get_or_404(id=src_file_id)
        File.create(
            parent_id=dest_parent_id,
            uuid_name=src_file.uuid_name,
            name=src_file.name,
            path=src_file.path,
            extension=src_file.extension,
            _from=src_file._from,
            size=src_file.size,
            md5=src_file.md5
        )

    @staticmethod
    def get_folder_tree():
        folder_list = File.get_all(extension=None)
        t = FolderTree()
        t.generate_by_list(folder_list)
        return t.serialize()
