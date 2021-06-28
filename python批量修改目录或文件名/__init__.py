#!/usr/bin/env python 
# encoding: utf-8

from pathlib import Path
import os
print(i for i in Path('C:\\').parents)
print(Path('C:\\').resolve())

a = os.listdir('C:\\test')
print(a)