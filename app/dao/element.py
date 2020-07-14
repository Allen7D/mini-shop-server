# -*- coding: utf-8 -*-
"""
  Created by Chai on 2020/7/13.
"""

from app.models.m2m import Element2Group
from app.models.element import Element
from app.models.route import Route
from app.core.db import db

__author__ = 'Chai'

class ElementDao:
    @staticmethod
    def get_element_by_group(group_id):
        element_list = []
        e2g_list = Element2Group.get_all(group_id=group_id)
        for e2g in e2g_list:
            element = Element.get(id=e2g.element_id)
            if element:
                route = Route.get(id=element.route_id)
                element_code = route.path + ":" + route.name + ":" + element.element_sign
                element_list.append(element_code)
        return element_list

    @staticmethod
    def deploy_permission(group_id, element_id):
        with db.auto_commit():
            db.session.query(Element2Group).filter(Element2Group.group_id == group_id).delete(synchronize_session=False)
            Element2Group.create(group_id=group_id, element_id=element_id, commit=False)

    @staticmethod
    def create_element(form):
        Route.get_or_404(id=form['route_id'])
        Element.create(**form)

    @staticmethod
    def delete_element(ids):
        with db.auto_commit():
            Element2Group.query.filter(Element2Group.element_id.in_(ids)).delete(synchronize_session=False)
            Element.query.filre(Element.id.in_(ids)).delete(synchronize_session=False)
