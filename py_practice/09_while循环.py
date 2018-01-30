# -*- conding:utf-8 -*-
__author__ = 'kiya'
#实例一
# num = 0
# while num <= 100:
    # print(num)
    # num += 1  # 在前时，无法打印出0
    # print(num)
    # if num % 2 == 0:  #仅打印双数
    #     print(num)
    # num += 1  #此位置时才能打印出0


#实例二
# i = 0
# number = 0
# while i <= 100:
#     if i % 2 == 0:  #仅打印偶数
#         print(i)
#         number += 1  #定义一个number记录打印i的次数
#     if number == 5: #打印次数超过5次后，结束打印
#         break
#     i += 1


#实例三
ticket = 1 #1表示有车票，0表示无车票
knifeLenght = 8 #cm

# if ticket == 1:  #先检查是否有票
#     print('有票进站，下一步请接受安全检查！')
#     if knifeLenght <= 10:  #携带的行李是否合规
#         print('合规，请上车')
#     else:
#         print('您的knife太长，不能上车')
# else:
#     print('请您买票上车')


# 实例四

gender = input('请输入你的性别:')
colour = '白'
money  = 10000
height = '美'
if gender == 'woman':
    if colour == '白' and money >=8000 and height == '美':
        print('我是白富美')
else:
    print('我是高帅富')
