# -*- coding:utf-8 -*-

__author__ = 'kiya04-6'

class animal:

    def eat(self):
        print('-----eat------')
    def dink(self):
        print('-----dink------')
    def run(self):
        print('-----run------')
# 继承父类
class Dog(animal):

    def dog(self):
        print('----汪汪叫-----')

class Cat(animal):

    def cat(self):
        print('-----喵喵叫-----')
# 继承子类
class Erha(Dog):

    def erha(self):
        print('----我是二哈-----')

    # 重写
    def dog(self):
        print('----重写汪汪叫----')
    # 调用被重写的方法
    # 方法一
    #     Dog.dog(self)
    # 方法二(super().dog() 调用super()结果中的dog())
        super().dog()


A = animal()
dog1 = Dog()
cat1 = Cat()
erha1 = Erha()

A.eat()
dog1.eat()
cat1.eat()
erha1.erha()
erha1.eat()
erha1.dog()
