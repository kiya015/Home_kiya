# -*- condig:utf-8 -*-

__author__ = 'kiya04-7'

# 多态学习

class Dog(object):
    def print_test(self):
        print('-----test')

class A(Dog):
    def print_test(self):
        print('---------test_one')

def introduce(temp):  # temp 在此为一个对象：temp.print_test()  调用对象temp中的方法print_test()
    temp.print_test()


dog = Dog()
a = A()
introduce(a)
introduce(dog)
