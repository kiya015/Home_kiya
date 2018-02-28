# -*- coding:utf-8 -*-

__author__ = "kiya"

# 实例：先计算三个值的和，再取三个值的平均值

# 方法一：使用第一个函数返回结果，第二个函数调用第一个函数的结果（传参方式）

# onea = int(input('输入值1：'))
# twoa = int(input('输入值2：'))
# threea = int(input('输入值3：'))
#
#
# def five_sum(one, two, three):
# 	sum = one + two + three
# 	# print('%d+%d+%d=%d '%(one,two,three,sum))
# 	return sum
#
#
# def average_three(suma):
# 	average_sum = suma / 3
# 	print('%d的平均值是：%d' %(suma,average_sum))
#
#
# result = five_sum(onea, twoa, threea)
# average_three(result)

# 方法二：函数里面调用函数


num1 = int(input('数值1：'))
num2 = int(input('数值2：'))
num3 = int(input('数值3：'))

def sum_three(a,b,c): # 函数1
	result = a + b + c
	# print("结果是：%d" %result)
	return result

def average_sum(a1,a2,a3):
	result1 = (sum_three(a1,a2,a3)) /3   # 函数sum_three(a1,a2,a3) 实际是去调前面的函数一并传参a1,a2,a3至对应的a,b,c,对应的结果用result1来接收
	print("三个和的平均值是：%d" %result1)

sum_three(num1,num2,num3)
average_sum(num1,num2,num3)