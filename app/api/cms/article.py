# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/26.
  ↓↓↓ 文章管理接口 ↓↓↓
"""
from flask import g

from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.cms import article as api_doc
from app.core.token_auth import auth
from app.core.utils import paginate
from app.models.article import Article
from app.dao.article import ArticleDao
from app.libs.error_code import Success
from app.validators.article import ArticleValidator, ArticleTypeValidator

__author__ = 'Allen7D'

api = Redprint(name='article', module='文章管理', api_doc=api_doc, alias='cms_article')


@api.route('/list', methods=['GET'])
@api.doc(args=['query.type', 'g.query.page', 'g.query.size'])
def get_article_list():
    '''查询文章列表'''
    type = ArticleTypeValidator().get_data('type')
    page, size = paginate()
    articles = ArticleDao.get_article_list(type, page, size)
    return Success(articles)


@api.route('/latest', methods=['GET'])
@api.doc(args=['query.type', 'g.query.page', 'g.query.size'])
def get_latest_article_list():
    '''查询最新文章列表'''
    type = ArticleTypeValidator().get_data('type')
    page, size = paginate()
    articles = ArticleDao.get_recent_article_list(type, page, size)
    return Success(articles)


@api.route('/<int:id>', methods=['GET'])
@api.doc(args=['g.path.article_id'])
def get_article(id):
    '''查询文章'''
    article = ArticleDao.get_article(id)
    return Success(article)


@api.route('/<int:id>', methods=['PUT'])
@api.doc(args=['g.path.article_id'], auth=True)
@auth.group_required
def update_article(id):
    '''更新文章'''
    form = ArticleValidator().dt_data
    article = ArticleDao.update_article(id, **form)
    return Success(article, error_code=1)


@api.route('/<int:id>', methods=['DELETE'])
@api.doc(args=['g.path.article_id'], auth=True)
@auth.group_required
def delete_user(id):
    '''删除文章'''
    ArticleDao.delete_article(id)
    return Success(error_code=2)


@api.route('', methods=['POST'])
@api.doc(args=['*int.body.type', '*str.body.title', '*str.body.summary', '*str.body.content', '*str.body.img'],
         auth=True)
@auth.group_required
def create_group():
    '''新建文章'''
    form = ArticleValidator().dt_data
    Article.create(author_id=g.user.id, **form)
    return Success(error_code=1)
