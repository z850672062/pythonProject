#!/usr/bin/env python 
# encoding: utf-8
import pyautogui
import time
import pyperclip

# print('确认中心点:', x, y)
# 对识别出的图像进行点击,参数x,y代表坐标位置,clicks代表点击次数,button可以设置为左键或者右键,interval为间隔时间



def auto_choujiang(Str2):
    while True:
        pyautogui.click(x=1367, y=1028, clicks=1, button='left')
        time.sleep(0.5)
        pyperclip.copy(Str2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(1)

if __name__ == '__main__':
    print("ctrl + f2 :暂停")
    Str2 = input('输入想发的字符:')
    auto_choujiang(Str2)

