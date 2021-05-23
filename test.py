#!/usr/bin/env python 
# encoding: utf-8
import sys
import webbrowser

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
webbrowser.open('https://map.baidu.com/?newmap=1&ie=utf-8&s=s%26wd%3D'+address)