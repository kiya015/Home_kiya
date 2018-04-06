# -*- coding:utf-8 -*-

__author__ = 'kiya4-3'

class Dog:

    def __del__(self):
        print("----英雄over-------")




dog1 = Dog()
dog2 = dog1
del dog1   # 不会调用__del__方法，因为这个对象还有其它变量指向它
del dog2   # 此时会调用__del__方法，因为没有变量指向它了
print('=========')


# 如果在程序结束时，有些对象还存在，那个python解释器会自动调用它们的__del__方法来完成清理工作

# del dog2