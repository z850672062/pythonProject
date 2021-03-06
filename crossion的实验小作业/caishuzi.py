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
最后将结果保存在文件中（保存在game_many_user.txt)中
Rev2021-7-12 14:32:56
新增内容：
txt文件是否存在，存在读取游戏
不存在，初始化游戏
Rev2021-7-13 15:56:46
新增内容：
增加多用户玩家，存在加载上次游戏数据，不存在增加新的游戏数据。

"""
import random
import pathlib


def guess_number():
    # 猜数字数据字典
    guess_dict = {}
    player = input('请输入你的名字：')
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
        average1 = all_count/times
        # 最快猜出轮数
        fast_count =  min(fast_count_list)
        print('%s，你已经玩了%d次，最少%d轮猜出答案,平均%.2f轮猜出答案' % (player,times,fast_count,average1))
        judge = input('是否继续游戏？(输入y继续，其他退出)')
        if judge != 'y':
            print('退出游戏，欢迎下次再来！')
            break
    # 添加key和value的数据
    guess_dict[player] = str(str(times) + ' ' + str(fast_count) + ' ' + str(all_count))
    return guess_dict

def init_file(guess_dict):
    # print(guess_dict)
    with open('game_many_user.txt', 'w', encoding='utf-8') as p:
        # 循环遍历字典中的key和value值写入到txt文本
        for k in guess_dict:
            str2 = str(k + ' ' + str(guess_dict[k]) + '\n')
            p.writelines(str2)

def history_file():

    with open('game_many_user.txt', 'r', encoding='utf-8') as p:
        data_list = p.readlines()

    guess_dict = {}
    # 循环遍历data_list2并进行split字符串分离 ，分离出的结果 加入字典
    for i in data_list:
        data_list2 = i.split()
        guess_dict[data_list2[0]] = data_list2[1:]
    # print(guess_dict)

    # 添加玩家名
    player = input('请输入玩家名')


    # 判断果然玩家不在字典中的keys就初始化数据，如果存在就继续游玩
    if player not in guess_dict.keys():
        times = 0
        fast_count = 0
        all_count =0
        average1 = 0
        print('%s，你已经玩了%d次，最少%d轮猜出答案,平均%.2f轮猜出答案' % (player, times, fast_count, average1))
    else:
        # 记录次数
        times = int(guess_dict[player][0])
        # 记录最快猜中轮数列表
        fast_count = int(guess_dict[player][1])
        # 记录总游戏轮数
        all_count = int(guess_dict[player][2])
        # 平均数
        average1 = all_count / times

        print('%s，你已经玩了%d次，最少%d轮猜出答案,平均%.2f轮猜出答案' % (player, times, fast_count, average1))

    while True:
        # 生成随机数1-100
        random_num = random.randint(1, 100)
        # print(random_num)

        print('废话不多说，咋们开始吧，请输入你想到的数字(1 - 100)：')
        count = 0  # 记录循环内的轮数

        while True:
            guess_number = int(input())
            count += 1
            if guess_number > random_num:
                print('哎呀，猜大了再试试')

            elif guess_number < random_num:
                print('哎呀，猜小了再试试')
            else:
                print('恭喜你猜对了，你真是神机妙算呀！，你只花了%d轮就猜出来了' % count)

                break
        # 如果游戏次数=0 或者 游戏轮数小于最小轮数就更新最小轮数= count
        if times == 0 or count < fast_count:
            fast_count = count
        # 游戏总次数加1
        times += 1
        # 总轮数增加
        all_count += count

        # 一次游戏平均几轮猜中 =总游戏轮数/总游戏次数
        average1 = all_count/times
        print('%s，你已经玩了%d次，最少%d轮猜出答案,平均%.2f轮猜出答案' % (player,times,fast_count,average1))
        judge = input('是否继续游戏？(输入y继续，其他退出)')
        if judge != 'y':
            print('退出游戏，欢迎下次再来！')
            break



    # 增加新数据
    guess_dict[player] = str(str(times) + ' ' + str(fast_count) + ' ' + str(all_count)).split()

    # print(guess_dict)

    # 写入数据
    with open('game_many_user.txt', 'w', encoding='utf-8') as p:
        # 循环遍历字典中的key和value值做join处理成string字符串 写入到txt文本
        for k in guess_dict:
            str2 = str(k + ' ' + str(" ".join(guess_dict[k])) + '\n')
            p.writelines(str2)

if __name__ == '__main__':
    judge = pathlib.Path('game_many_user.txt').exists()
    # 判断文件是否存在，不存在生成，存在读档写入

    if judge != True:
        print('生成游戏数据文件中...')

        guess_dict = guess_number()
        init_file(guess_dict)
    else:
        history_file()












