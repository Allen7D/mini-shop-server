# Flask 升级指南

本文档提供了将 mini-shop-server 项目从 Flask 1.1.2 升级到 Flask 2.0.3 的详细说明。

## 主要变更

1. 升级 Flask 从 1.1.2 到 2.0.3
2. 移除 flask-script 依赖，改用 Flask 内置的 CLI 功能
3. 更新 werkzeug 相关导入和使用方式
4. 更新 itsdangerous 库的使用方式
5. 替换已弃用的配置项和功能
6. 更新自定义异常类以适配新版API

## 依赖版本更新

主要更新包括：

- flask: 1.1.2 -> 2.0.3
- flask-sqlalchemy: 2.3.2 -> 2.5.1
- sqlalchemy(固定其版本用以兼容 flask-sqlalchemy的版本): 未指定 -> 1.4.46
- flask-httpauth: 3.3.0 -> 4.7.0
- flask-wtf: 0.14.2 -> 1.1.1
- flask-cors: 3.0.6 -> 3.0.10
- itsdangerous: 未指定 -> 2.0.1
- werkzeug: 未指定 -> 2.0.3
- jinja2: 未指定 -> 3.0.3
- 新增 cachelib 替代 werkzeug.contrib.cache: 未指定 --> 0.10.2

## 代码变更详情

### 1. 移除 flask-script 依赖

`server.py` 文件已更新，移除了 flask-script 的使用，改为使用 Flask 内置的 CLI 功能：

```python
# 旧代码
from flask_script import Manager, Server
app = create_app()
manager = Manager(app)
manager.add_command("run", Server())
if __name__ == '__main__':
    manager.run()

# 新代码
import click
app = create_app()
@app.cli.command("run")
@click.option('--host', default='127.0.0.1', help='The host to bind to.')
@click.option('--port', default=5000, help='The port to bind to.')
@click.option('--debug', is_flag=True, help='Enable debug mode.')
def run_command(host, port, debug):
    """Run the Flask development server."""
    app.run(host=host, port=port, debug=debug)
if __name__ == '__main__':
    app.run()
```

### 2. 更新 werkzeug 相关导入

- `werkzeug.contrib.fixers` 已移至 `werkzeug.middleware.proxy_fix`
- `werkzeug.contrib.cache` 已移至独立的 `cachelib` 包

### 3. 更新 JSON 相关配置

在 `app/core/utils.py` 中更新了 `jsonify` 函数，移除了对已弃用配置的依赖：

```python
# 旧代码
if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] or current_app.debug:
    indent = 2
    separators = (', ', ': ')
# ...
mimetype=current_app.config['JSONIFY_MIMETYPE']

# 新代码
if current_app.debug:
    indent = 2
    separators = (', ', ': ')
# ...
mimetype='application/json'
```

### 4. 更新 itsdangerous 库的使用

在 `app/core/token_auth.py` 中，更新了 token 生成和验证的代码：

```python
# 旧代码
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# ...
s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
token = s.dumps({...})
return {'token': token.decode('ascii')}

# 新代码
from itsdangerous import URLSafeTimedSerializer as Serializer
# ...
s = Serializer(current_app.config['SECRET_KEY'])
data = s.loads(token, max_age=7200)  # 使用 max_age 参数
token = s.dumps({...})
return {'token': token}  # 不再需要 decode('ascii')
```

### 5. 错误处理更新

在 `app/__init__.py` 中，更新了错误处理代码，确保与 Flask 2.0 兼容：

```python
# 旧代码
return APIException(code=e.code, error_code=1007, msg=e.description)

# 新代码
return APIException(code=e.code, error_code=1007, msg=str(e.description))
```

### 6. 更新自定义异常类

在 `app/core/error.py` 中，更新了 `APIException` 和 `Success` 类以适配 Flask 2.0.3 的接口变化：

```python
# 更新 APIException.get_body 方法添加 scope 参数
def get_body(self, environ=None, scope=None):
    body = dict(
        msg=self.msg,
        error_code=self.error_code,
        request_url=request.method + ' ' + self.get_url_no_param()
    )
    text = json.dumps(body)
    return text

# 更新 APIException.get_headers 方法添加 scope 参数
def get_headers(self, environ=None, scope=None):
    return [('Content-type', 'application/json; charset=utf-8')]

# 更新子类 Success.get_body 方法添加 scope 参数
def get_body(self, environ=None, scope=None):
    body = dict(
        error_code=self.error_code,
        msg=self.msg,
        data=self.data
    )
    text = json.dumps(body)
    return text

# 添加 __call__ 方法确保异常类可以作为WSGI应用被调用
def __call__(self, environ, start_response):
    return super(APIException, self).__call__(environ, start_response)
```

### 7. 修复 flask-admin 蓝图命名冲突

在 Flask 2.0+ 版本中，蓝图名称不能包含点(.)字符，需要修改相关代码：

```python
# 旧代码
self.admin.add_view(model_view(model, db.session,
                           endpoint='admin.{}'.format(lower_model_name),
                           url='/admin/{}'.format(lower_model_name)))

# 新代码
self.admin.add_view(model_view(model, db.session,
                           endpoint='admin-{}'.format(lower_model_name),
                           url='/admin/{}'.format(lower_model_name)))
```

## 运行项目

1. 安装新的依赖：
   ```
   # 使用pipenv
   pipenv install
   
   # 或使用pip
   pip install -r requirements.txt
   ```

2. 使用新的命令启动服务器：
   ```
   # 开发模式
   flask run
   
   # 或者使用自定义命令
   flask run --host=0.0.0.0 --port=8000 --debug
   ```

## 注意事项

1. 如果项目中有其他使用已弃用 Flask 功能的地方，可能需要进一步调整
2. 建议在升级后全面测试项目功能，确保所有功能正常工作
3. 对于使用 `flask-script` 的自定义命令，需要使用 Flask CLI 重新实现
4. 确保所有视图函数返回的是 Flask 期望的响应类型，特别是使用了自定义异常类的地方