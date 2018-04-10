# -*- coding:utf-8 -*-

__author__ = 'kiya04-8'

class CarStore(object):
	def order(self, car_type):
		return order_car_type(car_type)  # 返回内容(谁调的order返回给谁)：将car_type传参给函数order_car_type

def order_car_type(car_type):   #
	if car_type == "现代":
		return Xd_car()
	elif car_type == "mini":
		return Mini()


class Car(object):
	def move(self):
		print('移动---')

	def stop(self):
		print('停车---')

class Xd_car(Car):
	pass

class Mini(Car):
	pass


car_store = CarStore()
# car = Car()
# car = car_store.order(60000)
car = car_store.order("现代")
car.move()
car.stop()

