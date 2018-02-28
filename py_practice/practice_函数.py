# -*- coding : utf-8 -*-

__author__ = 'kiya'

# 函数实现名片管理系统
# '''打印提示'''


def p_fun():
	print('='*50)
	print('功能项：1、增加;2、删除;3、修改;4、查询;5、退出')
	print('='*50)

# 调用打印提示
p_fun()


fun = int(input('选择功能：'))
card_n = []

# 添加增加的函数
def add_card():
	'''增加名片函数'''
	global card_n
	name = input('增加的姓名:')
	card_n.append(name)
	print(card_n)


if fun == 1:
	add_card()

# help(add_card)




