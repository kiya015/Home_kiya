# -*- coding:utf-8 -*-

__author__ = 'kiya'

#实现打卡计算

import requests


# get请求获取所有的日期数据（以json串返回的Response）
payload = {'userId':2017402}
r = requests.get('http://jiecaob.szzbmy.com/sign/getRecord',params= payload)
print(r.json())  # 获取以json形式返回的response数据


