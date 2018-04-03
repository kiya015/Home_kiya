# -*- coding:utf-8 -*-


__author__ = 'kiya4-3'


class Dog:
	# 私有方法
	def __send_msg(self):
		print('----发送短信')

	# 公有方法
	def send_msg(self, money):
		# print('------请重试')
		if money>1000:
			self.__send_msg()

		else:
			print('余额不足')

dog = Dog()
dog.send_msg(20000)
# dog.__send_msg()   # 私有方法，会报错




#
# class Dog:
# 	def __init__(self, new_name):
# 	# def __init__(self):
# 		self.name = new_name
# 		self.__age = 0 # 定义了一个私有属性
#
# 	def set_age(self, new_age):
# 		if new_age>0 and new_age<100:
# 			self.__age = new_age
# 		else:
# 			self.__age = 0
#
# 	def get_age(self):
# 		return self.__age,self.name
#
# # 实例化
# dog = Dog('test')
# dog.set_age(20)
# age = dog.get_age()
#
# print(age)



# class Dog:
# 	# def __init__(self, new_name):
# 	def __init__(self):
# 		# self.name = new_name
# 		self.__age = 0 # 定义了一个私有属性
#
# 	def set_age(self, new_age):
# 		if new_age>0 and new_age<100:
# 			self.__age = new_age
# 		else:
# 			self.__age = 0
#
# 	def get_age(self):
# 		return self.__age
#
# # 实例化
# dog = Dog()
# dog.set_age(20)
# age = dog.get_age()
#
# print(age)