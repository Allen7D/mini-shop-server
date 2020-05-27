# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/26.
"""
from app.models.article import Article
from app.core.db import db

__author__ = 'Allen7D'


class ArticleDao():
    # 查询文章
    @staticmethod
    def get_article(id):
        article = Article.get_or_404(id=id, msg='该文章不存在')
        article.update(views=article.views + 1)
        return article

    # 获取文章列表
    @staticmethod
    def get_article_list(type, page, size):
        paginator = Article.query \
            .filter_by(type=type) \
            .paginate(page=page, per_page=size, error_out=True)
        paginator.hide('content')
        return {
            'total': paginator.total,
            'current_page': paginator.page,
            'items': paginator.items
        }

    # 删除
    @staticmethod
    def delete_article(id):
        artitle = Article.get_or_404(id=id)
        artitle.delete()
