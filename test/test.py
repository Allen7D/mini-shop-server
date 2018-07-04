# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/7/3.
"""
__author__ = 'Alimazing'


class Student():
	sum = 0
	name = 'Student'
	age = 0
	school = '学军中学'

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.__score = 0
		Student.sum += 1
		print('__init__')


	def palce(self, school):
		self.school = school

	def marking(self, score):
		self._score = score

	def show(self):
		print('分数：', self.__score)

	def __pri(self):
		print('private method')

	@classmethod
	def cm(cls):
		print('类方法:', cls.name)


s1 = Student('s1_haha', 11)
print(s1.name, s1.age)

# 如果没有「自定义的实例变量」，self直接使用类变量
s2 = Student('s2_hehe', 12)
print(s2.name, s2.age, s2.school)

# self的变量，是动态增加的
s3 = Student('s3_hihi', 13)
s3.palce('s3_中学')
s3.lover = '小红'
s3.__score = 13
s3.show()
print(s3.name, s3.age, s3.school, s3.lover)
print(s3.__dict__)
print('****'*10)

print(Student.name, Student.age, Student.school)
#Output: Student 0 学军中学

print('****'*10)

print(s1.__dict__)
print(Student.__dict__)

s1.cm()
print('学生总数:', Student.sum)

print('****'*10)
