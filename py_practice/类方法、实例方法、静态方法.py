# -*- coding:utf-8 -*-

__author__ = 'kiya04-7'

class Game(object):
    # 类属性
    num = 0
    # 实例方法
    def __init__(self):
        # 实例属性
        self.name = 'kiya'

    # 类方法
    @classmethod   # 固定写法，表示定义类方法
    def add_num(cls):  # cls 不一定要叫cls,原理同self
        cls.num = 100

    # 静态方法
    @staticmethod
    def print_menu():
        print('----------------')
        print('--穿越火线V1.1--')
        print('1、开始游戏----')
        print('2、选择人物----')
        print('-----------------')


game = Game()
Game.add_num()  # 可以通过类名调用类方法
game.add_num()  # 还可以用类创建的对象，调用类方法

print(Game.num)

# game.print_menu() # 实例对象调用静态方法
Game.print_menu() # 类对象调用静态方法
