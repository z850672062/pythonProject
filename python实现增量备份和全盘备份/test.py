#!/usr/bin/env python 
# encoding: utf-8
# #1、通过传入的路径，获取改路径下面的所有目录和文件
#
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

# 2、计算文件的md5值

import hashlib
import sys,os
def md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    print(md5('infotest.vbs'))
