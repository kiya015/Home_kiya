# -*- coding:utf-8 -*-

__author__ = 'kiya3-12'

# class 学习实例


class Cat:
    # 属性

    # 方法
    def eat(self):
        print('猫在吃鱼====')

    def drink(self):
        print('猫在喝水。。')

    def introduce(self):
        print('%s的年纪是%s!' % (self.name, self.age))

# 创建一个对象
tom = Cat()

# 调用tom指向对象中的方法
tom.eat()
tom.drink()

# 给tom指向的对象添加属性
tom.name = '汤姆'
tom.age = 30
# 第一种实现属性的方法
# print('%s的年纪是%d!'%(tom.name, tom.age))

tom.introduce()

blue = Cat()
blue.eat()
blue.drink()
blue.name = '蓝猫'
blue.age = '28'

blue.introduce()
