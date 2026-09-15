# _*_ coding: utf-8 _*_
"""
  本地静态资源 URL 拼接工具。
  从 model 层抽出，避免 model 直接依赖 Flask 的 request / current_app（属表现层关注点）。
"""
from flask import current_app, request


def local_asset_url(subfolder, filename):
    """本地静态资源完整 URL：<host>/<static_url_path>/<subfolder>/<filename>"""
    host_url = request.host_url
    host_url = host_url.split(',')[-1] if ',' in host_url else host_url
    host_url = host_url[:-1]  # 去掉末尾 '/'，如 http://192.168.10.80:8010
    static_url_path = '{0}/{1}'.format(current_app.static_url_path[1:], subfolder)
    return '{0}/{1}/{2}'.format(host_url, static_url_path, filename)