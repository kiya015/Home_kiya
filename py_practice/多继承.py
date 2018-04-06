# -*- coding:utf-8 -*-

__author__ = 'kiya04-6'

class Base(object):
    def test(self):
        print('----base')

class A(Base):
    def test1(self):
        print("-----test1")

class B(Base):
    def test2(self):
        print('----test2')
# 同时继承A,B的方法及属性
class C(A,B):
    pass

c = C()

c.test1()
c.test()
c.test2()

print(C.__mro__)  # 此处为类调用__mro__ 故是大写的Ｃ，可功能可以得知Ｃ的执行顺序（Ｃ3算法）

