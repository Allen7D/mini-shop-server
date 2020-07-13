# -*- coding: utf-8 -*-
from app.models.m2m import Element2Group
from app.models.element import Element
from app.models.route import Route
from app.core.db import db


class ElementDao:
    @staticmethod
    def get_group_element(group_id):
        element_list = []
        element_group = Element2Group.get_all(group_id=group_id)
        for eg in element_group:
            element = Element.get(id=eg.element_id)
            if element:
                route = Route.get(id=element.route_id)
                element_code = route.path + ":" + route.name + ":" + element.element_sign
                element_list.append(element_code)
        return element_list

    @staticmethod
    def deploy_permission(group_id, element_id):
        with db.auto_commit():
            db.session.query(Element2Group).filter(Element2Group.group_id == group_id).delete(synchronize_session=False)
            Element2Group.create(group_id=group_id, element_id=element_id)

    @staticmethod
    def add_element(data):
        route = Route.get_or_404(id=data['route_id'])
        Element.create(**data)


    @staticmethod
    def delete_element(ids):
        with db.auto_commit():
            Element2Group.query.filter(
                Element2Group.element_id.in_(ids)
            ).delete(synchronize_session=False)
            Element.query.filre(
                Element.id.in_(ids)
            ).delete(synchronize_session=False)
