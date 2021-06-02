#!/usr/bin/env python 
# encoding: utf-8

#需要的工具 python pycharm chromedriver.exe（91.0.4472.77） selenium


#下例是自定义时间和商品自动抢购。
from selenium import webdriver
import datetime
import time

def login():
    # 打开淘宝登录页并访问
    browser.get("https://www.taobao.com")
    # 程序睡眠2秒，等待页面代码加载
    time.sleep(2)
    # 如果找到一个元素,就点击他    找到。元素。通过。局部，链接_文本
    if browser.find_element_by_partial_link_text("亲，请登录"):
        browser.find_element_by_partial_link_text("亲，请登录").click()

    # 跳转到登陆页面后，提示用户扫码登陆
    print('请在6秒内扫码登陆！')
    time.sleep(12)
    # 之后跳转到购物车
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(2)

#设置秒杀时间 对比系统时间 时间一到就执行结算
#bug_time 为设定秒杀的时间 比如 2021-5-12 21:00:00 choose设置手动和自动勾选商品 1就自动，2就手动
def bug(buy_time,choose):
    # 获取当前时间
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print(now)

        #对比是否达到抢购时间 现在时间大于等于设置的时间
        if now >= buy_time:

            #如果 值为1 自动
            if choose == 1:
                #开始全选商品
                while True:
                    try:
                        # 如果发现 id 为J_SelectAll2就选中全部商品
                        if browser.find_element_by_id("J_SelectAll2"):
                            browser.find_element_by_id("J_SelectAll2").click()
                            # 打印当前时间
                            now_time = datetime.datetime.now()
                            print('选中的商品时间为:%s' % now_time)
                            break
                    except:
                        print("找不到全选按钮")
            # 开始进行结算
            try:
                if browser.find_element_by_partial_link_text('结 算'):
                    browser.find_element_by_partial_link_text('结 算').click()
                    print("结算成功")
            except:
                pass
            #开始提交订单
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print("抢购成功时间:%s" % now)
                        break
                except:
                    pass


    #循环打印当前时间
    print(now)
    #循环睡眠0.1s 循环对比是否达到抢购时间
    time.sleep(0.005)

if __name__=='__main__':
    #设置抢购时间
    buy_time = input('请输入抢购时间，格式如（2021-05-27 23:09:00.000000） ')
    #设置手动还是自动 选择商品
    choose = input('到时间自动勾选购物车请输入“1”，手动选择商品输入“2” ')
    #打开浏览器
    browser = webdriver.Chrome()
    # 全屏化页面
    browser.maximize_window()


    #调用登陆函数
    login()
    #调用购买函数
    bug(buy_time,choose)











