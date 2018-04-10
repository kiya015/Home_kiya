# -*- coding:utf-8 -*-

__author__ = 'kiya04-8'

class CarStore(object):
	# 以钱为区别选择提什么价格的车
	# def order(self, money):
	# 	if money > 50000:
	# 		return  Car()
	# def order(self, car_type):
	# 	if car_type == "现代":
	# 		return  Xd_car()
	def __init__(self):
		self.factorys = Factory() # 此处未完全理解

	def order(self, car_type):
		return self.factorys.factory(car_type)  # 此处未完全理解

	# def order(self, car_type):
	# 	return factory(car_type)

class Factory(object):
	def factory(self, car_type):
		if car_type == "现代":
			return Xd_car()
		elif car_type == "别克":
			return Bk_car()
		# else:
		# 	print('无此车型')



class Car(object):
	def move(self):
		print('移动---')

	def stop(self):
		print('停车---')

class Xd_car(Car):
	pass

class Bk_car(Car):
	pass


car_store = CarStore()
# car = Car()
# car = car_store.order(60000)
car = car_store.order("现代")
car.move()
car.stop()

