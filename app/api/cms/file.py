# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/2.
  ↓↓↓ 文件上传下载接口 ↓↓↓
  可以用来处理上传产品图片、Excel等
"""
from flask import request

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import file as api_doc
from app.extensions.file.local_uploader import LocalUploader
from app.core.token_auth import auth
from app.models.file import File
from app.dao.file import FileDao
from app.service.file import FileService
from app.libs.error_code import Success
from app.validators.forms import UploadFileValidator, FileParentIDValidator, PaginateValidator, IDCollectionValidator, \
    CreateFileValidator, UpdateFileValidator, MoveOrCopyFileValidator

__author__ = 'Allen7D'

api = Redprint(name='file', description='文件管理', api_doc=api_doc, alias='cms_file')


@api.route('', methods=['POST'])
@api.route_meta(auth='上传文件', module='文件')
@api.doc(auth=True)
@auth.group_required
def upload_file():
    '''上传文件'''
    files = request.files
    uploader = LocalUploader(files)
    res = uploader.upload()
    return Success(res)


@api.route('/list', methods=['GET'])
@api.route_meta(auth='查询文件列表', module='文件')
@api.doc(args=['g.query.parent_id'], auth=True)
@auth.group_required
def get_file_list():
    '''查询文件列表'''
    page_validator = PaginateValidator().nt_data
    other_validator = FileParentIDValidator().dt_data

    files = File.query.filter_by(**other_validator) \
        .paginate(page=page_validator.page, per_page=page_validator.size, error_out=False)
    return Success({
        'total': files.total,
        'current_page': files.page,
        'items': files.items
    })


@api.route('/<int:id>', methods=['GET'])
@api.route_meta(auth='查询文件详情', module='文件')
@api.doc(args=['g.path.file_id'], auth=True)
@auth.login_required
def get_file(id):
    '''查询文件详情'''
    file = File.query.filter_by(id=id).first_or_404()
    return Success(file)


@api.route('/all/by_name', methods=['GET'])
@api.route_meta(auth='查询文件(基于文件名)', module='文件')
@api.doc(args=['g.query.filename'], auth=True)
@auth.group_required
def get_file_list_by_name():
    '''查询文件(基于文件名)'''
    filename = request.args.get('filename')
    files = File.query.filter_by(name=filename).all()
    return Success({
        'items': files
    })


@api.route('/new', methods=['POST'])
@api.route_meta(auth='新建文件夹', module='文件')
@api.doc(args=['g.query.parent_id', 'g.query.filename'], auth=True)
@auth.group_required
def create_folder():
    '''新建文件夹'''
    validator = CreateFileValidator().dt_data
    FileDao.create_folder(**validator)
    return Success()


@api.route('/move', methods=['PUT'])
@api.route_meta(auth='移动文件', module='文件')
@api.doc(args=['g.query.parent_id', 'g.query.file_id'], auth=True)
@auth.group_required
def move_files():
    '''移动文件'''
    validator = MoveOrCopyFileValidator().nt_data
    FileDao.move_file(
        dest_parent_id=validator.parent_id,
        file_id=validator.file_id
    )
    return Success(error_code=1)


@api.route('/copy', methods=['POST'])
@api.route_meta(auth='复制文件', module='文件')
@api.doc(args=['g.query.parent_id', 'g.query.file_id'], auth=True)
@auth.group_required
def copy_file():
    '''复制文件'''
    validator = MoveOrCopyFileValidator().nt_data
    FileDao.copy_file(
        dest_parent_id=validator.parent_id,
        src_file_id=validator.file_id
    )
    return Success(error_code=1)


@api.route('/rename', methods=['PUT'])
@api.doc(args=['g.query.filename', 'g.query.file_id'], auth=True)
@auth.group_required
def rename_file():
    '''重命名文件'''
    validator = UpdateFileValidator().nt_data
    FileDao.rename_file(file_id=validator.file_id, new_filename=validator.filename)
    return Success(error_code=1)


@api.route('', methods=['DELETE'])
@api.route_meta(auth='删除多个文件', module='文件', mount=True)
@api.doc(args=['g.query.file_ids'], auth=True)
@auth.group_required
def delete_files():
    '''删除多个文件'''
    ids = IDCollectionValidator().nt_data.ids
    FileDao.delete_files(ids)
    return Success(error_code=2)


@api.route('/upload', methods=['POST'])
@auth.login_required
def post_file():
    '''文件上传(废弃)'''
    validator = UploadFileValidator().nt_data
    filename = FileService(file=validator.file).save()
    return Success(msg='{} 保存成功'.format(filename), error_code=1)
