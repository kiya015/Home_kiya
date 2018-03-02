# -*- coding:utf-8 -*-

__author__ = 'kiya'

# 实现打卡计算

import requests
import time

# 步骤一：取出所有时间
# get请求获取所有的日期数据（以json串返回的Response）
payload = {'userId':2017402}
r = requests.get('http://jiecaob.szzbmy.com/sign/getRecord', params=payload)  # 将payload传递至URL上（http://jiecaob.szzbmy.com/sign/getRecord?userId=2017402）
dtime = r.json()  # 获取以json形式返回的response数据 返回结果为字典
# print(dtime)

time_value = dtime['data']  # 从dtime字典里取出data(为列表)
# print(time_value)

# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
date = '2018-02-28'
# date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print(date)
# 从time_value取出每个相同日期进行比较
datelt = []
# fmt = '%Y-%m-%d %H:%M:%S'  # 确定输出的时间格式带 .0是因为tday值带.0
for tday in time_value:
	# time_tuple = time.strptime(tday,fmt) # 将tday时间转换为fmt时间格式,输出结果为元组
	# print(time_tuple)
	# print(type(time_tuple))
	d_list = tday.split(' ') # split(' ')以空隔打断tday字符串内容
	# print(d_list[0])
	if d_list[0] == date:
		# print(tday)
		datelt.append(time.strptime(tday, '%Y-%m-%d %H:%M:%S.0'))  # 将转化后的时间加到datelt[]
		# print(tday,type(tday))


maxtime = max(datelt)  # 取出单个datelt[]中最大时间
mintime = min(datelt)  # 取出单个datelt[]中最小时间

# print(min(datelt))
# print(max(datelt))

mdtime = time.strptime('2018-02-28 09:30:00.0', '%Y-%m-%d %H:%M:%S.0')
mdtime_2 = time.strptime('2018-02-28 19:00:00.0', '%Y-%m-%d %H:%M:%S.0')
# print(mintime)
# print(maxtime)
# print(mdtime)
# print(mdtime_2)
# print(type(mdtime_2),type(mintime))

# 将同格式的时间进行比较
if mintime < mdtime and maxtime > mdtime_2:
	print('上班卡时间为：%s,下班卡为：%s' % (mintime,maxtime))
	# print('正常')


def mydata(date):
	pass













