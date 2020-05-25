# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/12/2.
"""
__author__ = 'Allen7D'

upload_file = {
    "parameters": [
        {
          "name": "id",
          "in": "path",
          "type": "integer",
          "emun": [0, 1, 2, 3, 4, 5]
        },
        {
            "name": "file",
            "in": "formData",
            "type": "file",
            "required": 'false'
        }
    ],
    "security": [
        {
            "basicAuth": []
        }
    ],
    "responses": {
        "200": {
            "description": "上传文件成功",
            "examples": {
                "data": [
                    {
                        "id": 1,
                        "key": "file",
                        "name": "switch.png",
                        "path": "2020/04/10/93e1ffd0-7b07-11ea-b22f-acbc32924b6f.png",
                        "url": "http://127.0.0.1:5000/static/2020/04/10/93e1ffd0-7b07-11ea-b22f-acbc32924b6f.png"
                    }
                ],
                "error_code": 0,
                "msg": "成功"
            }
        }
    }
}

download_file = {
    "parameters": [
        {
            "file_name": "",
            "in": "path",
            "type": "string",
            "enum": ['Python面向对象编程指南.epub'],
            "default": 'Python面向对象编程指南.epub',
            "required": 'true'
        },
    ],
    "responses": {
        "200": {
            "description": "下载文件成功",
            "examples": {}
        }
    }
}
