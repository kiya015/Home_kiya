# -*- coding:utf-8 -*-

__author__ = 'kiya4-1'

class Dog:
    def set_age(self, new_age):
        if new_age > 0 and new_age < 100:
            self.age = new_age
        else:
            self.age = 0
            # print('年龄错了')

    def get_age(self):
        return  self.age

# 实例化
dog = Dog()
# dog.name = '小白'
# dog.age = 10

dog.set_age(1000)
print(dog.get_age())

