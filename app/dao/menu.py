# _*_ coding: utf-8 _*_
"""
    Created by Mohan on 2020/05/06
    [mini-shop-server]Menu:

"""
__author__ = "Mohan"

from app.models.group import Group
from app.models.route import Route
from app.models.menu import Menu
from app.dao.route import RouteTree, RouteNode
from app.core.db import db


class MenuDao(object):
    @staticmethod
    def get_routes(gid: int) -> dir:
        id2route_node = {route.id: dict(route) for route in Group.get_or_404(id=gid).route}
        id2route_node_clone = id2route_node.copy()

        def add_parent_node(cur_route_node):
            if cur_route_node['parent_id'] == cur_route_node['id'] == 0:
                pass
            else:
                if not cur_route_node['parent_id'] in id2route_node.keys():
                    parent_route = Route.get_or_404(id=cur_route_node['parent_id'])
                    id2route_node_clone[parent_route.id] = dict(parent_route)
                    add_parent_node(dict(parent_route))

        for route_node in id2route_node.values():
            add_parent_node(route_node)

        t = RouteTree(RouteNode)
        t.generate_by_list([route_node for route_node in id2route_node_clone.values()])
        return t.serialize()['children']

    @staticmethod
    def add_route(gid, routes):
        with db.auto_commit():
            Group.get_or_404(id=gid, msg='无指定权限组')
            for route_id in routes:
                Route.get_or_404(id=route_id, msg='无指定路由节点')
                Menu.abort_repeat(group_id=gid, route_id=route_id)
                Menu.create(group_id=gid, route_id=route_id)

    @staticmethod
    def delete_routes(gid, routes):
        with db.auto_commit():
            Menu.query.filter(
                Menu.group_id == gid,
                Menu.route_id.in_(routes)
            ).delete(synchronize_session=False)

    @staticmethod
    def cover_menus(group_id, routes):
        Menu.query.filter_by(group_id=group_id).delete(synchronize_session=False)
        t = RouteTree()
        t.generate_by_dir({
            'id': 0,
            'children': routes
        })

        with db.auto_commit():
            for route in t.deserialize():
                Menu.create(group_id=group_id, route_id=route['id'])

