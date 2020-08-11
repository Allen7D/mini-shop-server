# -*- coding: utf-8 -*-
"""
  Created by Chai on 2020/7/13.
"""

from app.models.group import Group
from app.models.element import Element
from app.models.route import Route
from app.models.m2m import Group2Element
from app.core.db import db

__author__ = 'Chai'


class ElementDao:
    @staticmethod
    def get_element_by_group(group_id):
        group = Group.get_or_404(id=group_id)
        return group.elements

    @staticmethod
    def reset_permission(group_id, element_ids):
        with db.auto_commit():
            db.session.query(Group2Element).filter(Group2Element.group_id == group_id).delete(synchronize_session=False)
            for element_id in element_ids:
                Group2Element.create(group_id=group_id, element_id=element_id, commit=False)

    @staticmethod
    def create_element(form):
        Route.get_or_404(id=form['route_id'])
        Element.create(**form)

    @staticmethod
    def delete_element(ids):
        with db.auto_commit():
            Group2Element.query.filter(Group2Element.element_id.in_(ids)).delete(synchronize_session=False)
            Element.query.filre(Element.id.in_(ids)).delete(synchronize_session=False)
