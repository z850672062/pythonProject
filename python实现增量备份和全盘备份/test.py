#!/usr/bin/env python 
# encoding: utf-8
#1、通过传入的路径，获取改路径下面的所有目录和文件

# import os,sys
#
# # 环循变量出路径，文件夹和文件，
# # D:\pythonProject\python实现增量备份和全盘备份\templates\小工具
# # ['windows激活工具', 'geek.exe', 'Music-Downloader-UI.exe', 'windows激活工具.7z']
# def lsdir(folder):
#     contents = os.walk(folder)
#     for path,folder,file in contents:
#         print("%s\n%s\n" %(path,folder + file))
#
#
#
#
#
# if __name__ == '__main__':
#     print()
#     lsdir(os.path.join(str(os.getcwd()),'templates'))
#
# # 2、计算文件的md5值
#
# import hashlib
# import sys,os
# def md5(fname):
#     # 生成一个md5的hash对象
#     m = hashlib.md5()
#     # ‘rb’：表示以二进制方式读取文件。该文件必须已存在。
#     with open(fname,'rb') as fobj:
#         while True:
#             # 从打开的文件中读取数据
#             data = fobj.read(4096)
#             if not data:
#                 break
#             #     更新加密
#             m.update(data)
#     #         返回加密字符串
#     return m.hexdigest()
#
# if __name__ == '__main__':
#     print(md5('infotest.vbs'))
#
#
#
# import os
# fename = os.path.split('C://test/')
# print(
# fename)
#
# print('C://test/    2 /' .rstrip('/'))


dict2 = {'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\404.html': '0aac04d1d432437e1c41e3a01f981ddf',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\base.html': '75171613dac4c768f0fad8666c9d5ee8',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\commodity.html': '183ceb2f712d94bb942b44a232325be8',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\details.html': '2868defb5300644befd0918f8411c35a',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\index.html': '23c1fb244732b0e4351749219e2e519e',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\login.html': '0cf1b09d0604b77a2d431dbb596a4d62',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\shopcart.html': '6f4e1b656fecd83354a05854f0b31195',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\shopper.html': 'a01cd2dc72a1ad2b6b4601a9c3cc882d',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\test\\base.html': '75171613dac4c768f0fad8666c9d5ee8'}

dict3 = {'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\404.html': '0aac04d1d432437e1c41e3a01f981ddf',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\base.html': '75171613dac4c768f0fad8666c9d5ee8',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\commodity.html': '183ceb2f712d94bb942b44a232325be8',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\details.html': '2868defb5300644befd0918f8411c35a',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\index.html': '23c1fb244732b0e4351749219e2e519e',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\login.html': '0cf1b09d0604b77a2d431dbb596a4d62',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\shopcart.html': '6f4e1b656fecd83354a05854f0b31195',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\shopper.html': 'a01cd2dc72a1ad2b6b4601a9c3cc882d',
         'D:\\pythonProject\\python实现增量备份和全盘备份\\templates\\test\\base.html': '75171613dac4c768f0fad8666c9d5ee9'}

# if dict2.values() != dict3.values():
#     print()

# print(dict3.values() ^ dict2.values())
# for i in dict3:
#     print(dict3[i]) #获取到dict的values
#     print(i) #获取到dict的key
#     print(dict2[i]) #获取dict2的values
#     print(dict2.get(i))
#     # print(i.values())

# list2 = ['C:\\test','C:\\test - 副本']
# for i in list2:
#     print(i)
import zipfile

