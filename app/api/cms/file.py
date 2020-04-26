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
from app.service.file import FileService
from app.libs.error_code import Success
from app.validators.forms import UploadFileValidator, UploadPDFValidator, PaginateValidator

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
@api.doc(args=['g.query.page', 'g.query.size'], auth=True)
@auth.login_required
def get_file_list():
    '''查询文件列表'''
    validator = PaginateValidator().validate_for_api().nt_data
    paginator = File.query.filter_by() \
        .paginate(page=validator.page, per_page=validator.size, error_out=False)
    return Success({
        'total': paginator.total,
        'current_page': paginator.page,
        'items': paginator.items
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


@api.route('/upload/double', methods=['POST'])
@auth.login_required
def upload_double_file():
    '''双文件上传'''
    form = UploadPDFValidator().validate_for_api()
    origin_file = request.files[form.origin.name]
    origin_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], origin_file.filename))
    comparer_file = request.files[form.comparer.name]
    comparer_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], comparer_file.filename))
    return Success(error_code=1)


@api.route('/download/<string:file_name>', methods=['GET'])
@auth.login_required
def download_file(file_name):
    '''文件下载'''
    return Success(file_name)
# return send_from_directory(file_name, file_name, mimetype='application/octet-stream')
