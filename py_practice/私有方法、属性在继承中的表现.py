# -*- coding:utf-8 -*-

__author__ = 'kiya04-6'


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print('-----公有方法----')

    def __test2(self):
        print('---私有方法----')
    # 同一个类中调用私有方法及属性
    def test3(self):
        self.__test2()
        print(self.__num2)


class B(A):
    pass


# a = A()
b = B()
b.test3()   # 可以调用父类中公有方法中调用的私有方法及属性

# b.__test2()  私有方法并不会被继承
# b.test1()

# print(b.__num2)  私有属性并不会被继承
# print(b.num1)

# 以上内容验证继承不会继承私有的方法及属性