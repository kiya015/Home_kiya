# -*- coding:utf-8 -*-

__author__ = 'kiya04-11'

class Dog(object):
    def __init__(self):
        print('--init方法--')

    def __del__(self):
        print('--del方法--')

    def __str__(self):
        return "--str方法--"

    def __new__(cls):
        return object.__new__(cls)
