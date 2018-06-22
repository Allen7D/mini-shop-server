# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/5/31.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
__author__ = 'Alimazing'

Base = declarative_base()

theme2product = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )
