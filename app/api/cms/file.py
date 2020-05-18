# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/2.
  ↓↓↓ 文件上传下载接口 ↓↓↓
  可以用来处理上传产品图片、Excel等
"""
import os

from flask import request, current_app
from flask import send_from_directory

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
@api.doc(auth=True)
@auth.login_required
def upload_file():
    '''文件上传'''
    files = request.files
    uploader = LocalUploader(files)
    res = uploader.upload()
    return Success(res)


@api.route('/list', methods=['GET'])
@api.doc(args=['g.query.parent_id'], auth=True)
@auth.group_required
def get_file_list():
    '''查询文件夹下列表'''
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
@api.doc(args=['g.path.file_id'], auth=True)
@auth.login_required
def get_file(id):
    '''查询文件·基于文件ID'''
    file = File.query.filter_by(id=id).first_or_404()
    return Success(file)


@api.route('/by_name', methods=['GET'])
@api.doc(args=['g.query.filename'], auth=True)
@auth.login_required
def get_file_by_name():
    '''查询文件·基于文件名
    可能存在同名文件，返回结果为list
    '''
    filename = request.args.get('filename')
    file_list = File.query.filter_by(name=filename).all()
    return Success({
        'items': file_list
    })


@api.route('/upload', methods=['POST'])
@auth.login_required
def post_file():
    '''文件上传'''
    validator = UploadFileValidator().validate_for_api()
    filename = FileService(file=validator.file.data).save()
    return Success(msg='{} 保存成功'.format(filename), error_code=1)


@api.route('/new', methods=['POST'])
@api.doc(args=['g.query.parent_id', 'g.query.filename'], auth=True)
@auth.group_required
def create_folder():
    '''新建文件夹'''
    validator = CreateFileValidator().dt_data
    FileDao.create_folder(**validator)
    return Success()


@api.route('/move', methods=['PUT'])
@api.doc(args=['g.query.parent_id', 'g.query.file_id'], auth=True)
@auth.group_required
def move_file():
    '''移动文件'''
    validator = MoveOrCopyFileValidator().nt_data
    file = File.get_or_404(id=validator.file_id)
    file.update(parent_id=validator.parent_id)
    return Success(error_code=1)


@api.route('/copy', methods=['POST'])
@api.doc(args=['g.query.parent_id', 'g.query.file_id'], auth=True)
@auth.group_required
def copy_file():
    '''复制文件'''
    validator = MoveOrCopyFileValidator().nt_data
    return Success(error_code=1)


@api.route('/rename', methods=['PUT'])
@api.doc(args=['g.query.filename', 'g.query.file_id'], auth=True)
@auth.group_required
def rename_file():
    '''重命名文件'''
    validator = UpdateFileValidator().nt_data
    file = File.get_or_404(id=validator.file_id)
    file.update(name=validator.filename)
    return Success(file)


@api.route('', methods=['DELETE'])
@api.route_meta(auth='删除多个文件', module='文件', mount=True)
@api.doc(args=['g.query.file_ids'], auth=True)
@auth.group_required
def delete_file_list():
    '''删除多个文件'''
    ids = IDCollectionValidator().nt_data.ids
    return Success(ids)


@api.route('/download/<string:file_name>', methods=['GET'])
@auth.login_required
def download_file(file_name):
    '''文件下载'''
    return Success(file_name)
