# -*- coding:utf-8 -*-

__author__ = 'kiya04-8'

# 未实现,部分原理未理解

# 新增一种车库类型如宝马
class Store(object):
    def select_car(self):
        pass

    def order(self, car_type):
        return self.select_car(car_type)




class Bmwcar(Store):
    def select_car(self, car_type):
		return Bmw_car().factory(car_type)


class Bmw_car(object):
	def factory(self, car_type):
		if car_type == "mini":
			return Xd_car()
		elif car_type == "x6":
			return Bk_car()

bmw = Bmwcar()
bmw2 = bmw.order('mini')

class CarStore(object):

	def __init__(self):
		self.factorys = Factory() #  类似于再将Factory这个类实例化

	def order(self, car_type):
		return self.factorys.factory(car_type)  # 此处self未理解代表谁

class Factory(object):
	def factory(self, car_type):
		if car_type == "现代":
			return Xd_car()
		elif car_type == "别克":
			return Bk_car()

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
car = car_store.order("现代")
car.move()
car.stop()

