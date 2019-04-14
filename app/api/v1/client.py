# _*_ coding: utf-8 _*_
"""
  Created by Allen7D on 2018/5/31.
"""

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import ClientValidator, UserEmailValidator
from app.api_docs import client as api_doc

__author__ = 'Allen7D'

api = RedPrint(name='client', description='客户端', api_doc=api_doc)


@api.route('/register', methods=['POST'])
def create_client():
	form = ClientValidator().validate_for_api()  # 参数校验，直接在此抛出异常，并中指代码
	promise = {
		ClientTypeEnum.USER_EMAIL: __register_user_by_email
	}
	promise[form.type.data]()
	return Success(error_code=1)


def __register_user_by_email():
	form = UserEmailValidator().validate_for_api()
	User.register_by_email(form.nickname.data, form.account.data, form.secret.data)


'''
	问题: def update_user应该放在client.py 或 user.py的哪一个？
	对于权限而言, update涉及的业务逻辑会很广，包括
		1、更好用户名、密码、各种绑定（QQ、微信、手机、邮箱）
		2、修改权限

	当然普通用户也有这个权限，包括
		1、绑定或结绑QQ、微信、手机、邮箱、账号等(一旦有了账号，则账号不可更改)
'''
