# mini-shop-server
基于 Flask框架开发的微信小程序后端，用于构建小程序商城。
* 借鉴慕课网的[《Python Flask构建可扩展的RESTful API》](http://coding.imooc.com/class/220.html)的设计模式
* 重构慕课网的[《微信小程序商城构建全栈应用》](https://coding.imooc.com/learn/list/97.html)，源项目基于TP5 + MINA框架
* QQ 交流群 163801325（聊天，斗图，学习，交流。伸手党勿进）


#### 三端分离
客户端: mini-shop-wx，基于美团的 [mpvue框架](http://mpvue.com/)开发的微信小程序。（未开始，占坑）

服务端: mini-shop-server，基于 Flask框架构建 RESTful API。（正在实现中）

CMS: mini-shop-cms, 基于 Flask框架。（未开始，占坑）

#### 开发工具
* Python 3.6（虚拟环境：pipenv）
* MySQL
* PyCharm（开发工具）
* Navicat（数据库可视化管理工具）

#### pipenv的安装
[《pipenv 的用法指南》](https://www.jianshu.com/p/00af447f0005)

如果还未安装pip3包管理工具，请先执行如下语句
> $ sudo apt install python3-pip

安装 pipenv
> $ pip3 install pipenv

#### 导入 mysql 数据
* [SQL文件](https://github.com/bodanli159951/mini-shop-server/blob/master/zerd.sql)

#### 本地启动
> $ git clone https://github.com/Alimazing/mini-shop-server.git <br>
$ cd mini-shop-server <br>
$ pipenv shell # 进入虚拟环境 or 构建新的虚拟环境<br>
$ pipenv install # 安装包依赖<br>
$ python shema.py # 启动入口文件

#### 目录结构
```
| |____app.py
| |____api
| | |______init__.py
| | |____v1
| | | |______init__.py
| | | |____address.py
| | | |____user.py
| | | |____token.py
| | | |____theme.py
| | | |____client.py
| | | |____order.py
| | | |____product.py
| | | |____banner.py
| | | |____category.py
| |____validators
| | |____params.py
| | |______init__.py
| | |____forms.py
| | |____base.py
| |____service
| | |______init__.py
| | |____app_token.py
| | |____token.py
| | |____order.py
| | |____user_token.py
|____fake.py
|____README.md
|____code.md
|____Pipfile
|____.gitignore
```

#### 生成临时管理员信息 
> $ python fake.py

#### 自动生成 api 接口文档
[Swagger](https://swagger.io/) 是一个规范和完整的框架，用于生成、描述、调用和可视化 RESTful 风格的 Web 服务。

本项目使用[flasgger库](https://github.com/rochacbruno/flasgger)自动生成 Swagger风格[(Demo)](https://editor.swagger.io/?_ga=2.211085136.492521077.1539840591-1920768432.1536803925)的API文档。

查阅API文档
> 在浏览器端输入：http://localhost:5001/apidocs/#/
