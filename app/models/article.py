# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/5/26.
"""
from sqlalchemy import Column, ForeignKey, Integer, String, SmallInteger, Text, event

from app.core.db import EntityModel as Base, db
from app.libs.utils import discard_html
__author__ = 'Allen7D'


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False, comment='外键，用户id')
    type = Column(SmallInteger, comment='文章类型')
    title = Column(String(255), comment='文章标题')
    summary = Column(Text, comment='文章摘要')
    content = Column(Text, comment='文章内容')
    img = Column(String(255), comment='主图路径')
    theme = Column(SmallInteger, comment='文章主题')
    views = Column(Integer, default=0, comment='浏览量')

    @property
    def author(self):
        from app.models.user import User
        user = User.get(id=self.author_id)
        return user.nickname if user else '匿名'

    def keys(self):
        self.hide('author_id')
        self.append('author', 'create_time')
        return self.fields


@event.listens_for(Article.content, 'set')
def on_content(target, value, oldvalue, initiator):
    '''
    :param target: 有监听事件发生的 Article实例对象
    :param value: 被监听字段的变化值
    :param oldvalue: 被监听字段的初始值
    :param initiator:
    :return:
    '''
    # 不填写摘要
    if not target.summary:
        target.update(summary=discard_html(value[:60]) + '...')
    else:
        target.update(summary=discard_html(value[:60]) + '...')

    # # 文章更新时
    # if target.summary and target.summary in oldvalue:
    #     target.summary = value[:100] + '...'
