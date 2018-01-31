# -*- coding:utf-8 -*-

__author__ = 'kiya'

#实例一：打印矩形
# symbol = input('请输入您要打印的符号：')
# i = 0
# while i < 5:
# 	j = 0
# 	while j < 10:
# 		print(symbol, end='	')
# 		j += 1
# 	print('')
# 	i += 1

# 实例二：打印三角形
# symbol = input('请输入您要打印的符号：')
# i = 0
# while i <= 5:
# 	j = 1
# 	while j <= i:  #循环
# 		print(symbol, end='')
# 		j += 1
# 	print('')
# 	i += 1

# 实例三：九九乘法表

row = 1
while row <= 9:
	column = 1
	while column <= row:
		print('%d*%d=%d,\t' % (column, row, (row * column)),end = '')
		column += 1
	print('')
	row += 1