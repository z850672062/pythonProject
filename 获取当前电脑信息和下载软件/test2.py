#!/usr/bin/env python
# encoding: utf-8


import os
import socket
import winreg
import pathlib

# -*- coding: UTF-8 -*-
from openpyxl import Workbook #不需要excel文件存在 可以生成一个
from openpyxl import load_workbook #需要传入一个excel文件不能传入

L2 = '1'
L3 = '2'
blist = []
for m,n in zip(L2,L3):
  blist.append(m)
  blist.append(n)
print(blist)