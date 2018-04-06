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

