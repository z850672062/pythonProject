#!/usr/bin/env python
# encoding: utf-8


import os
import socket
import winreg
import pathlib

# -*- coding: UTF-8 -*-
from openpyxl import Workbook #不需要excel文件存在 可以生成一个
from openpyxl import load_workbook #需要传入一个excel文件不能传入

hostname = socket.gethostname()

rows = [
    ['Number', 'data1', 'data2'],
    [2, 40, 30],
    [3, 40, 25],
    [4, 50, 30],
    [5, 30, 10],
    [6, 25, 5],
    [7, 50, 10]]

print(list(zip(*rows)))




# 获取工作簿
wb = Workbook()
# 激活当前的sheet
ws = wb.active

# ws.append(softlist)

ws2 = wb.create_sheet('SoftwareList')
sheets = wb.sheetnames
ws1 = wb[sheets[0]]
ws2 = wb[sheets[1]]

ws.append(list(zip(*rows)))
# excel中单元格为B2开始，即第2列，第2行
# for i in range(len(softlist)):
#     ws2.cell(i + 2, 1).value = softlist[i]

# # 加载文件
# wb = openpyxl.load_workbook("test.xlsx")
# # 获得sheet名称
# sheetNames = wb.sheetnames
# print(sheetNames)
# # sheetName1 = sheetNames[0]
# # 根据名称获取第一个sheet
# # sheet1 = wb[sheetName1]
# # 根据索引获得第一个sheet
# sheet1 = wb.worksheets[0]



# # 保存数据，如果提示权限错误，需要关闭打开的excel
wb.save("test.xlsx")