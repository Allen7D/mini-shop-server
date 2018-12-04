<h1 align="center">
  mini-shop-server
</h1>
<h4 align="center">
	构建微信小程序(商城)后端<br>🤜基于 Flask框架开发的=🤛
</h4>
<div align="center">
  <img alt="Header" src="https://ws1.sinaimg.cn/large/006tNbRwly1fx19fcgb2pg308w099kjl.gif" width="88%">
</div>


* 借鉴慕课网的[《Python Flask构建可扩展的RESTful API》](http://coding.imooc.com/class/220.html)的设计模式
* 重构慕课网的[《微信小程序商城构建全栈应用》](https://coding.imooc.com/learn/list/97.html)，源项目基于TP5 + MINA框架
* QQ 交流群 163801325（聊天，斗图，学习，交流。伸手党勿进）

## 

## 亮点
- 基于原生的 Flask构建 RESTfull API
- 更灵活的 API文档生成方式
- AOP(面向切面编程)设计，实现**参数校验层**&**异常统一处理层**


## 目录
- [亮点](#亮点)
- [服务器部署](#服务器部署)

## 三端分离
#### 1.客户端: mini-shop-wx
基于美团的 [mpvue框架](http://mpvue.com/)开发的微信小程序。（未开始，占坑）

#### 2.服务端: mini-shop-server
基于 Flask框架构建 RESTful API。（正在实现中）<br>
点击查阅 [API文档](http://api.ivinetrue.com/apidocs/#/)(Swagger风格，可以带token)

#### 3.CMS: mini-shop-cms
基于 Flask框架。（未开始，占坑）


## 开发工具
* Python 3.6（虚拟环境：pipenv）
* MySQL
* PyCharm（开发工具）
* Navicat（数据库可视化管理工具）

### pipenv的安装
[《pipenv 的用法指南》](https://www.jianshu.com/p/00af447f0005)

如果还未安装pip3包管理工具，请先执行如下语句
> $ sudo apt install python3-pip

安装 pipenv
> $ pip3 install pipenv

### 本地启动
> $ git clone https://github.com/Alimazing/mini-shop-server.git <br>
$ cd mini-shop-server <br>
$ pipenv shell # 进入虚拟环境 or 构建新的虚拟环境<br>
$ pipenv install # 安装包依赖<br>
$ python shema.py run # 启动入口文件(默认5000端口)
$ python shema.py run -p 8080 # 启动入口文件(改为8080端口)

### 目录结构
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

### 生成临时管理员信息 
> $ python fake.py

### 自动生成 api 接口文档
[Swagger](https://swagger.io/) 是一个规范和完整的框架，用于生成、描述、调用和可视化 RESTful 风格的 Web 服务。

本项目使用[flasgger库](https://github.com/rochacbruno/flasgger)自动生成 Swagger风格[(Demo)](https://editor.swagger.io/?_ga=2.211085136.492521077.1539840591-1920768432.1536803925)的API文档。

1、[Swagger Editor](http://editor.swagger.io/) 在网页端直接编辑 API文档

查阅API文档(本项目)
> 启动服务(DEBUG模式下)
> 在浏览器端输入：http://localhost:8080/apidocs/#/
![]()

### pycharm的配置
http://www.it610.com/article/4325344.htm

### 服务器部署
[文章链接]()

#### Mysql的安装和数据导入
一、安装
```
> sudo apt-get install mysql-server
> sudo apt-get install mysql-client
> sudo apt-get install libmysqlclient-dev
```
安装过程中，会让你输入密码。<br>
请务必记住密码!<br>
务必记住密码！<br>
必记住密码！<br>

查看是否安装成功

`sudo netstat -tap | grep mysql`

二、运行

`> mysql -u root -p`

-u 表示选择登陆的用户名， -p 表示登陆的用户密码，上面命令输入之后会提示输入密码

接着输入密码(Enter password)

三、导入

下载 Mysql 数据  [SQL文件](https://github.com/bodanli159951/mini-shop-server/blob/master/zerd.sql)

mysql的每条执行以「分号」结尾
```
mysql> create database zerd; # 建立数据库(zerd)
mysql> use zerd; # 进入该数据库
mysql> source /home/ubuntu/zerd.sql; # 导入某目录下的sql文件
```
导入成功，可以直接查询
`mysql> select * from user;`

删除数据库
`mysql>  drop database zerd;`


#### 启动Server端
`python shema.py run -h 0.0.0.0 -p 8080`


