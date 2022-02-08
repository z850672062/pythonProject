#!/usr/bin/env python
# encoding: utf-8

"""
2022-2-8 20:04:12
修改采购执行表并修改名称上传服务器，最删除自身表格。
自身名称:
盛罗采购订单执行表.xls
克来采购订单执行表.xls
奥可威采购订单执行表.xls
三罗采购订单执行表.xls
名称格式：
盛罗采购订单执行表20220211.xls
克来采购订单执行表20220211.xls
奥可威采购订单执行表20220211.xls
三罗采购订单执行表20220211.xls
服务器地址：
\\192.168.16.17\文件服务器\05.部门管理平台\05.05.采购部平台\05.05.00.资料共享区\采购订单执行表\
"""

import xlrd
import xlwt

def read():
    # user = str(input("输入你的域账户,例子yijun.zeng\n"))
    # data = xlrd.open_workbook("C:\\Users\\" + user + "\\Desktop\\VB测试文件\\我的.xls")
    data = xlrd.open_workbook(r"C:\Users\lenovo\Desktop\VB测试文件\我的.xls")
    table = data.sheets()[0]
    # print(table.cell(1,1))
    # print(table.cell_value(1,1))
    print(data.sheet_by_index(1))

def write():
    new_workbook = xlwt.Workbook()
    worksheet = new_workbook.add_sheet('new_sheet')
    worksheet.write(0,0,'你好')
    new_workbook.save(r"C:\Users\lenovo\Desktop\VB测试文件\天啊.xls")






if __name__ == '__main__':
    read()
    write()