#!/usr/bin/env python 
# encoding: utf-8

"""
随机生成个数字，用户输入数字去猜，大了就输出猜猜了，小了输出猜小了,等于输出猜对了，并统计回合数
Rev2021-7-3 08:36:31
增加用户可以选择继续和退出功能（用户猜中一次后可选择“继续”还是“退出”）
总游戏轮数（玩家每猜一个数字算玩了一轮游戏）
Rev2021-7-8 09:30:01
新增内容：
统计数据：玩家姓名、总游戏次数（玩家每猜中答案算玩了一次游戏）、总游戏轮数（玩家每猜一个数字算玩了一轮游戏）、
最快猜中轮数，
最后将结果保存在文件中（保存在game_one_user.txt)中
"""
import random


def guess_number():
    # 猜数字数据字典
    guess_dict = {}
    player = input('请输入你的名字：')
    # 添加玩家名
    guess_dict['玩家'] = player
    # 记录次数
    times = 0
    # 记录最快猜中轮数列表
    fast_count_list = []
    # 记录总游戏轮数
    all_count = 0
    #
    while True:
        # 生成随机数1-100
        random_num = random.randint(1, 100)
        # print(random_num)

        print('你好，欢迎来到猜数字小游戏！！！')
        print('废话不多说，咋们开始吧，请输入你想到的数字(1 - 100)：')
        count = 0  # 记录循环内的轮数
        # 猜中总次数加1
        times += 1
        while True:
            guess_number = int(input())
            count += 1
            if guess_number > random_num:
                print('哎呀，猜大了再试试')

            elif guess_number < random_num:
                print('哎呀，猜小了再试试')
            else:
                print('恭喜你猜对了，你真是神机妙算呀！，你只花了%d轮就猜出来了' % count)
                all_count += count
                # 当前花的轮数记录在list中
                fast_count_list.append(count)
                break

        # 一次游戏平均几轮猜中 =总游戏轮数/总游戏次数
        average1 =('%.2f'%(all_count/times))
        # 最快猜出轮数
        fast_count =  min(fast_count_list)
        print('%s，你已经玩了%d次，最少%d轮猜出答案,平均%s轮猜出答案' % (player,times,fast_count,str(average1)))
        judge = input('是否继续游戏？(输入y继续，其他退出)')
        if judge != 'y':
            print('退出游戏，欢迎下次再来！')
            break

    # 添加总游戏次数
    guess_dict['总游戏次数'] = times
    # 添加总游戏轮数
    guess_dict['总游戏轮数'] = all_count
    # 添加最快猜中轮数
    guess_dict['最快猜中轮数'] = fast_count

    return guess_dict

def game_file(guess_dict):
    # print(guess_dict)
    with open('game_one_user.txt' , 'w+' ,encoding='utf-8' ) as p:
        # 循环遍历字典中的key和value值写入到txt文本
        for k in guess_dict:
            str2 = str(k + ':' + str(guess_dict[k])+ '\n')
            # print(str2)
            p.writelines(str2)

if __name__ == '__main__':
    guess_dict = guess_number()
    game_file(guess_dict)







