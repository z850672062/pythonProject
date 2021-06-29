#!/usr/bin/env python 
# encoding: utf-8

from pathlib import Path
import os
import sys
print(i for i in Path('C:\\').parents)
print(Path('C:\\').resolve())

a = os.listdir('C:\\test')
print(a)


print(os.path.basename(sys.argv[0]).split('.')[0])


testlist = ['1、0']

t2 = ['123', 'xyz', 'zara', 'abccc','是']
teststr = '6、33333333333、新建文本文档.txt'

print(max(t2))

for i in testlist:
    print(max(i.split('、')))