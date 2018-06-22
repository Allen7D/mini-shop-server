# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/14.
"""
from flask import g

from app.libs.error_code import RenewSuccess, DuplicateGift
from app.libs.redprint import RedPrint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.book import Book
from app.models.gift import Gift

__author__ = 'Alimazing'

api = RedPrint('gift')


@api.route('/<isbn>', methods=['POST'])
@auth.login_required
def create(isbn):
	uid = g.user.uid
	with db.auto_commit():
		Book.query.filter_by(isbn=isbn).first_or_404()
		gift = Gift.query.filter_by(isbn=isbn, uid=uid).first()  # 是否重复
		if gift:
			raise DuplicateGift()
		gift = Gift()
		gift.isbn = isbn
		gift.uid = uid
		db.session.add(gift)
	return RenewSuccess()
