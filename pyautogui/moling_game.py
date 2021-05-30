#!/usr/bin/env python 
# encoding: utf-8
import pyautogui
import time
# 匹配图片需要匹配当前像素
#出现胜利后点两次鼠标
def run(Shengli_url,quereng_url,xiage_url):
    print('test')
    #判定目标截图在系统上的位置
    Shengli = True
    quereng = True
    xiage = True
    while True:

        if Shengli == True:
            Shengli = pyautogui.locateOnScreen(Shengli_url)
            print('匹配胜利完毕')


            if Shengli == None:
                print('匹配胜利失败')
                break

        #匹配到胜利图标进行中心校准并点击
        elif Shengli is not None:
            # 利用center()函数获取目标图像在系统中的中心坐标位置
            x,y = pyautogui.center(Shengli)
            print('胜利中心点:',x,y)
            #对识别出的图像进行点击,参数x,y代表坐标位置,clicks代表点击次数,button可以设置为左键或者右键,interval为间隔时间
            pyautogui.click(x=x,y=y,clicks=2,button='left',interval=1)

            time.sleep(0.1)
            # 检查确认按钮
            if quereng == True:
                quereng = pyautogui.locateOnScreen(quereng_url)
                print('匹配确认按钮完毕')
                if quereng == None:
                    print('匹配确认按钮失败')
                    break
                continue;
            elif quereng is not None:
                # 利用center()函数获取目标图像在系统中的中心坐标位置
                x, y = pyautogui.center(quereng)
                print('确认中心点:', x, y)
                # 对识别出的图像进行点击,参数x,y代表坐标位置,clicks代表点击次数,button可以设置为左键或者右键,interval为间隔时间
                pyautogui.click(x=x, y=y, clicks=1, button='left')

                time.sleep(0.1)

                #检查下个关卡
                if xiage == True:
                    xiage = pyautogui.locateOnScreen(xiage_url)
                    print('匹配下个关卡按钮完毕')
                    if xiage == None:
                        print('匹配下个关卡按钮失败')
                        break
                    continue;
                elif xiage is not None:
                    # 利用center()函数获取目标图像在系统中的中心坐标位置
                    x, y = pyautogui.center(xiage)
                    print('确认中心点:', x, y)
                    # 对识别出的图像进行点击,参数x,y代表坐标位置,clicks代表点击次数,button可以设置为左键或者右键,interval为间隔时间
                    pyautogui.click(x=x, y=y, clicks=1, button='left')

                    time.sleep(0.1)
                    break


            # 丢弃
            # if Baoxiang == True:
            #     Baoxiang = pyautogui.locateOnScreen('moling/baoxiang.png')
            #     print('匹配宝箱完毕')
            #     if Baoxiang == None:
            #         print('匹配宝箱失败')
            #         break
            # else:
            #     print(Baoxiang)
            #     break





            break;
        else:
            pass;







    # print(loaction)
    # print('test')





if __name__ == '__main__':
    Shengli_url = 'moling/shengli.png'
    quereng_url = 'moling/quereng2.png'
    xiage_url = 'moling/xiage.png'
    run(Shengli_url,quereng_url,xiage_url)