#!/usr/bin/env python 
# encoding: utf-8
import sys
import webbrowser
import time,datetime

# now = datetime.datetime.now()
# now2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# print(now)
# print(now2)

# while True:
#     while True:
#         try:
#             if 2 > 1:
#                 print("大于")
#                 break
#         except:
#             print("出现错误！！！")

class TestClass:
    # def __init__(self):
    #     self.name = '小明'
    name = 'xx'
    # return self.name
    def __str__(self):
        # self.name = '小密'
        return self.name

t = TestClass() #实例化对象
print(t)
# 结果显示：小明