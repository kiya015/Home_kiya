# -*- coding:utf-8 -*-

__author__ = 'kiya3-27'


class Home:
	def __init__(self, narea, ninfo, naddr):
		self.area = narea
		self.info = ninfo
		self.addr = naddr
		self.nnarea = narea
		self.contain_item = []

	def __str__(self):
		return  '房子的总面积是：%d,地址：%s,户型：%s,放入%s后的面积是:%d' % (self.area, self.info, self.addr, self.contain_item, self.nnarea)

	def add_item(self, item):
		# self.nnarea -= item.area
		# self.contain_item.append(item.info)
		self.nnarea -= item.get_area()
		self.contain_item.append(item.get_info())

class Bed:
	def __init__(self, ninfo, narea):
		self.area = narea
		self.info = ninfo

	def __str__(self):
		return '%s占用面积是：%d' % (self.info, self.area)

	def get_area(self):
		return  self.area

	def get_info(self):
		return self.info

# 创建个对象，Home实例化

jia = Home(150, '深圳南山', '三室两厅')

bed1 = Bed('席梦思', 5)

jia.add_item(bed1)

bed2 = Bed('大圆床', 102)
jia.add_item(bed2)

print(jia)
print(bed1)
print(bed2)