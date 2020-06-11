# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2020/6/11.
"""
from app.models.notice import Notice

__author__ = 'Allen7D'


class NoticeDao():
    @staticmethod
    def delete_notice(id):
        notice = Notice.get_or_404(id=id)
        notice.delete()

    @staticmethod
    def update_notice(id, type, title, content, status, remark, update_by):
        '''
        :param id: 通知类型
        :param type: 通知类型
        :param title: 通知标题
        :param content: 通知内容
        :param status: 通知状态(0正常 1关闭)
        :param remark: 通知备注
        :param update_by: 更新者
        :return:
        '''
        notice = Notice.get_or_404(id=id)
        notice.update(type=type, title=title, content=content, status=status, remark=remark, update_by=update_by)
        return notice
