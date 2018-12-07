<h1 align="center">
  mini-shop-server
</h1>

<h4 align="center">
	构建微信小程序(商城)后端
	<br>🤜基于 Flask框架🤛
</h4>

<div align="center">
  <img alt="Header" src="https://ws1.sinaimg.cn/large/006tNbRwly1fx19fcgb2pg308w099kjl.gif" width="40%">
</div>
<div align="center">
  <a href="http://api.ivinetrue.com/apidocs/#/">API 文档</a>
</div>


* 借鉴慕课网的[《Python Flask构建可扩展的RESTful API》](http://coding.imooc.com/class/220.html)的设计模式
* 重构慕课网的[《微信小程序商城构建全栈应用》](https://coding.imooc.com/learn/list/97.html)，源项目基于TP5 + MINA框架
* QQ 交流群 163801325（聊天，斗图，学习，交流。伸手党勿进）

## 亮点
- [自动激活](#auto_active)虚拟环境(autoenv)
- 基于原生的 Flask构建 RESTfull API
- 更灵活的 API文档生成方式(可带 Token)
- AOP(面向切面编程)设计，实现 **参数校验层** & **异常统一处理层**
- Ubuntu 16.04上 nginx + uwsgi + pipenv部署


## 目录
- [亮点](#亮点)
- [开发工具](#开发工具)
- [服务器部署](#服务器部署)
- [三端分离](#三端分离)


## 开发工具
* Python 3.6（虚拟环境：pipenv）
* MySQL
* PyCharm（开发工具）
* Navicat（数据库可视化管理工具）

## 开发环境搭建
### pipenv的安装
[《pipenv 的用法指南》](https://www.jianshu.com/p/00af447f0005)

如果还未安装pip3包管理工具，请先执行如下语句<br>
```$ sudo apt install python3-pip```

安装 pipenv<br>
```$ pip3 install pipenv```

### 本地启动
```
$ git clone https://github.com/Alimazing/mini-shop-server.git
$ cd mini-shop-server 
$ pipenv --python 3.6 # 指定某 Python版本创建环境
$ pipenv shell # 激活虚拟环境 or 如果没有虚拟环境，则构建新的(默认版本)
$ pipenv install # 安装包依赖
$ python shema.py run # 启动入口文件(默认5000端口)
$ python shema.py run -p 8080 # 启动入口文件(改为8080端口)
```

#### 其他 pipenv操作
```
$ pipenv install flask # 安装指定模块，并写入到 Pipfile中
$ pipenv install flask==1.0.2 # 安装指定版本的模块
$ pipenv uninstall flask # 卸载指定模块
$ pipenv update flask # 更新指定模块
$ pip list # 查看安装列表
$ pipenv graph # 查看安装列表，及其相应的以来
$ pipenv --venv # 虚拟环境信息
$ pipenv --py # Python解释器信息
$ pipenv –rm # 卸载当前虚拟环境
$ exit # 退出当前虚拟环境
```

#### 骚操作
1、<span id="auto_active">**`自动激活`**<span> <br>
进入项目目录时，自动激活项目所需的虚拟环境

1.1 全局安装

 ```$ pip3 install autoenv```
 
1.2 配置

项目根目录下创建.env文件<br>
写入```$ pipenv shell```

1.3 将autoenv的激活脚本写入 profile文件中

bash模式

```
$ echo "source `which activate.sh`" >> ~/.bashrc
$ source ~/.bashrc
```
zsh模式

```
$ echo "source `which activate.sh`" >> ~/.zshrc
$ source ~/.zshrc
```
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
```$ python fake.py```

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


#### Mysql的安装和数据导入
##### 一、安装
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

```$ sudo netstat -tap | grep mysql```

##### 二、运行
```$ mysql -u root -p```

-u 表示选择登陆的用户名， -p 表示登陆的用户密码，上面命令输入之后会提示输入密码

接着输入密码(Enter password)

##### 三、导入
下载 Mysql 数据  [SQL文件](https://github.com/bodanli159951/mini-shop-server/blob/master/zerd.sql)

mysql的每条执行以「分号」结尾
```
mysql> create database zerd; # 建立数据库(zerd)
mysql> use zerd; # 进入该数据库
mysql> source /home/ubuntu/zerd.sql; # 导入某目录下的sql文件
```
导入成功，可以直接查询
```mysql> select * from user;```

删除数据库
```mysql>  drop database zerd;```


#### 启动Server端
```$ python shema.py run -h 0.0.0.0 -p 8080```

## 三端分离
#### 1.客户端: mini-shop-wx
基于美团的 [mpvue框架](http://mpvue.com/)开发的微信小程序。（未开始，占坑）

#### 2.服务端: mini-shop-server
基于 Flask框架构建 RESTful API。（正在实现中）

点击查阅 [API文档](http://api.ivinetrue.com/apidocs/#/)(Swagger风格，可以带token)

#### 3.CMS: mini-shop-cms
基于 Flask框架。（未开始，占坑）



