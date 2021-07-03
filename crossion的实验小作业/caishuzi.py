#!/usr/bin/env python 
# encoding: utf-8

"""
随机生成个数字，用户输入数字去猜，大了就输出猜猜了，小了输出猜小了,等于输出猜对了，并统计回合数
Rev2021-7-3 08:36:31
增加用户可以选择继续和退出功能（用户猜中一次后可选择“继续”还是“退出”）

"""
import random


def guess_number():
    # 生成随机数1-100
    random_num = random.randint(1, 100)
    # print(random_num)
    times = 0 # 记录轮数
    while True:
        print('你好，欢迎来到猜数字小游戏！！！')
        print('废话不多说，咋们开始吧，请输入你想到的数字(1 - 100)：')
        count = 0  # 记录回合数
        times += 1
        while True:
            guess_number = int(input())
            count += 1
            if guess_number > random_num:
                print('哎呀，猜大了再试试')

            elif guess_number < random_num:
                print('哎呀，猜小了再试试')
            else:
                print('恭喜你猜对了，你真是神机妙算呀！，你只花了%s回合就猜出来了' % count)
                break

        judge = input('是否继续游戏？(输入y继续，其他退出)')
        if judge == 'y':
            continue;
        else:
            print('退出游戏，您共玩了%s回合，欢迎下次再来！' % times)
            break;





if __name__ == '__main__':
    guess_number()






