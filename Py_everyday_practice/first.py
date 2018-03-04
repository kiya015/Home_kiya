# -*- coding:utf-8 -*-

__author__ = 'kiya  2018-3-2'


# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

# d = []
# for i in range(1,5):
# 	for j in range(1,5):
# 		for a in range(1,5):
# 			if (i != j) and (i != a) and (j != a):
# 				# print(i, j, a)
# 				d.append(int(str(i) + str(j) + str(a)))
#
#
# print(d)
# print(len(d))

# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？


# if ...elif...else方法

# profit = float(input('请输入当月利润：'))
# if profit <= 100000:
# 	money = profit * 0.01
# 	print("低于或等于10万元时提成0.1为:%s" % (money))
# elif 100000 < profit <= 200000:
# 	money = (profit - 100000)*0.075 +  (100000 * 0.1)
# 	print("10~20W之间提成是:%s" % (money))
# elif 200000 < profit <= 400000:
# 	money = (profit - 200000) * 0.005 + (100000 * 0.1) + (100000 * 0.075)
# 	print(money)



# 输入三个整数x,y,z，请把这三个数由小到大输出。


# range()语法：range(start, stop[, step])
lit = []
for i in range(3):   # 循环3次，实际执行for循环中的操作3次
    num = int(input('输入数据：'))
    lit.append(num)   # append():append() 方法用于在列表末尾添加新的对象。
lit.sort()  # sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
print(lit)


