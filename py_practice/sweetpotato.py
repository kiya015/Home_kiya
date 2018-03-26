# -*- coding:utf-8 -*-

__author__ = 'kiya3-26'

# 用类实现烤地瓜应用

class potato:

	def __init__(self):   # 此处因为init写为int导致错误一直未发现并修正
		self.cookeda = '生的'
		self.cooklevel = 0
		self.condiments = []  # 多个属性

	def __str__(self):
		return '地瓜状态：%s(%d)，添加佐料有：%s'%(self.cookeda, self.cooklevel, str(self.condiments))

	def cook(self, time):

		self.cooklevel += time
		if self.cooklevel>0  and  self.cooklevel<= 3:
			self.cookeda = '还是生的呢'

		elif self.cooklevel>3  and self.cooklevel <=5:

			self.cookeda = '还需要加油再烤烤哟'

		elif self.cooklevel>5 and self.cooklevel <8:
			self.cookeda = '刚刚好，可以开吃啦。。'

		elif self.cooklevel >= 8:
			self.cookeda = '烤焦啦。。。'

	def addCondinments(self,item):
		self.condiments.append(item)




# 创建对象(实例化)

gua = potato()

# print(gua)


gua.cook(5)
gua.addCondinments('辣椒')
print(gua)