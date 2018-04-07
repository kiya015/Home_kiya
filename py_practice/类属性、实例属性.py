# -*- coding:utf-8 -*-

__author__ = 'kiya04-7'

# 理解类对象  实际类也是一个对象，对象名是Tools
class Tools(object):
    # 属性
    num = 0  # 类属性
    # 方法
    def __init__(self, new_name):
        self.name = new_name  # 实例属性
        Tools.num += 1   # 调用类属性

# 实例化对象，实际有实例属性及方法
tool_1 = Tools('铁锹')
tool_2 = Tools('铁锹')
tool_3 = Tools('铁锹')
print(Tools.num)