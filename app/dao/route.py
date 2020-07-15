# _*_ coding: utf-8 _*_
"""
  Created by Mohan on 2020/4.
"""
from app.models.element import Element
from app.models.route import Route
from app.models.menu import Menu
from app.core.db import db
from app.core.error import Forbidden
from app.libs.utils import OrderNode, OrderTree

__author__ = 'Mohan'


class RouteNode(OrderNode):
    def __init__(self, id=None, order=None, parent_id=None, title=None,
                 name=None, icon=None, path=None, component=None, hidden=None, **kwargs):
        super(RouteNode, self).__init__(id=id, parent_id=parent_id, order=order)
        self.title = title
        self.name = name
        self.icon = icon
        self.path = path
        self.component = component
        self.hidden = hidden

    def keys(self):
        attrs = super(RouteNode, self).keys()
        return attrs + ('order', 'title', 'name', 'icon', 'path', 'component', 'hidden')


class RouteTree(OrderTree):
    def __init__(self, root=None, nodeType=RouteNode):
        super(RouteTree, self).__init__(root, nodeType)

    def serialize(self) -> dir:
        def serialize_node(tree_node):
            result = dict(tree_node)
            result['meta'] = {
                'icon': result['icon'],
                'title': result['title']
            }
            result.pop('icon')
            result.pop('title')
            result['children'] = [serialize_node(sub_node) for sub_node in tree_node.children]
            result['children'].sort(key=lambda ele: ele['order']) if len(result['children']) != 0 else None
            return result

        return serialize_node(self.root)


class RouteDao(object):
    # 获取整体嵌套路由(对应页面组件)
    @staticmethod
    def get_all_route_tree() -> dir:
        t = RouteTree()
        t.generate_by_list(Route.query.all())
        return t.serialize()

    # 获取整体嵌套路由(对应页面组件)和所有路由所含的页面元素
    @staticmethod
    def get_all_route_tree_with_element() -> dir:
        def process_route_with_element(route):
            if route.get('children', None):
                for child_route in route['children']:
                    process_route_with_element(child_route)
            else:
                elements = Element.get_all(route_id=route['id'])
                if elements:
                    route['elements'] = elements

        route_root = RouteDao.get_all_route_tree()
        process_route_with_element(route_root)
        return route_root

    @staticmethod
    def change_route(route_list: list):
        cur_t = RouteTree()
        cur_t.generate_by_dir({
            'id': 0,
            'children': route_list
        })
        cur_list = cur_t.deserialize()
        with db.auto_commit():
            for cur_route in cur_list:
                old_route = Route.get(id=cur_route['id'])
                if old_route and \
                        (old_route.parent_id != cur_route['parent_id'] or
                         old_route.order != cur_route['order']):
                    old_route.update(id=cur_route['id'], parent_id=cur_route['parent_id'],
                                     order=cur_route['order'], commit=False)

    @staticmethod
    def get_route_node(id) -> dir:
        return Route.filte(id=id).first()

    @staticmethod
    def update(id: int, **kwargs):
        route = Route.get_or_404(id=id, msg='该节点不存在')
        route.update(**kwargs)

    @staticmethod
    def delete(id: int):
        route = Route.get_or_404(id=id, msg='路由不存在, 删除失败')
        if Menu.get(route_id=id):
            raise Forbidden(msg='存在权限组绑定路由，不可删除')

        with db.auto_commit():
            route.delete(commit=False)
            Route.query.filter_by(parent_id=id).delete(synchronize_session=False)

    @staticmethod
    def create(**kwargs):
        Route.abort_repeat(msg='唯一键重复', name=kwargs['name'])
        route = Route.create(**kwargs)
