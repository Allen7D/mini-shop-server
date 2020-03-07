# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/4/19.
"""
from flask import current_app
from flask import render_template

from . import web

__author__ = 'Allen7D'


@web.route('/')
def index():
	'''跳转到项目目录'''
	url = {
		'github': current_app.config['GITHUB_URL'],
		'doc': current_app.config['DOC_URL'],
	}
	return render_template("index.html", url=url)


@web.route('/raw')
def render_raw():
	raw_html = """
		<style type="text/css">
			body{
				background: #fff;
				font-family:"Century Gothic","Microsoft yahei";
				color: #333;
				font-size:18px;
			}
			a {
				margin: 10px;
				color: #2E5CD5;
				cursor: pointer;
				text-decoration: none
        	}
			a:hover {
				text-decoration: underline;
        	}
		</style>
		<div style="padding: 24px 48px;">
			<p style="font-size:38px">
				小程序商城项目<br/>
				<span style="font-size:30px">欢迎你</span>
			</p>
			<a href="/">项目目录</a>
		</div>
		"""
	return raw_html
