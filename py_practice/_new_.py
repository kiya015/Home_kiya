# -*- coding:utf-8 -*-

__author__ = 'kiya04-12'

class Dog(object):
    def __init__(self):
        print('我是init')

    def __str__(self):
        return  '我是str,打印对象会返回一个结果'

    def __del__(self):
        print('删除类')

    def __new__(cls):  #cls 此时是Dog指向的类对象
        # print('创建对象')
        return object.__new__(cls)  # 调用父类的__new__方法来创建对象


dog = Dog()
print(id(Dog))