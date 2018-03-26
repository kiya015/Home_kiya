# -*- coding:utf-8 -*-

__author__ = 'kiya3-26'

# 用类实现烤地瓜应用

class SweetPotato:

	def __int__(self):
		self.cookedstring = '生的'
		self.cook_time = 0

	def __str__(self):
		return "地瓜状态：%s(%d)"%(self.cookedstring,self.cook_time)

	def cook(self, time):

		self.cook_time += time

		if 0< self.cook_time and self.cook_time<= 3:
			self.cookedstring = '还是生的呢'

		elif  3<self.cook_time  and self.cook_time <= 5:
			self.cookedstring = '还需要加油再烤烤哟'

		elif  5< self.cook_time and self.cook_time < 8:
			self.cookedstring = '刚刚好，可以开吃啦。。'

		elif  self.cook_time >= 8:
			self.cookedstring = '烤焦啦。。。'



# 创建对象(实例化)
gua = SweetPotato()
print(gua)


gua.cook(1)
# print(gua)