#!/usr/bin/env python
# encoding: utf-8
import os
import re
import sys
import time
import datetime
import logging
import shutil


# 记录日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)-1d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='DelApp.log',
                    filemode='a')


# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')
# 输出例子 Fri, 21 May 2021 18:51:20 del_file3.py [line:21] DEBUG This is debug message


# file_dir 为文件名称，file_re为过滤名称包含XXX的文件或文件夹，expire_time为最大保留时间
def find_file(file_dir, file_re='[^XXX$]+', expire_time=3):
    if file_re == '':
        logging.error('file_re is null,exit')
        return None

    logging.info('传入参数 :目录 [%s]，正则表达式[%s],过期天数 [%s]' % (file_dir, file_re, expire_time))
    # 目录下所有文件
    all_file = os.listdir(file_dir)
    # 匹配正则的文件
    reg_file_list = []
    reg_str = file_re
    for reg_file in all_file:
        if re.match(reg_str, reg_file):
            logging.info('正则匹配到文件：[%s]' % reg_file)

            # print(reg_file)
            reg_file_list.append(reg_file)
    # print(reg_file_list)

    # 满足过期时间的文件

    # 获取系统当前时间
    today = datetime.datetime.now()
    # print(today)
    # n天
    n_days = datetime.timedelta(days=int(expire_time))
    # n天前日期
    n_days_agos = today - n_days
    # n天前时间戳单位秒 时间戳（timestamp）的方式：时间戳表示是从1970年1月1号 00:00:00开始到现在按秒计算的偏移量。 北京就是1970年1月1号 08:00:00
    n_days_agos_timestamps = time.mktime(n_days_agos.timetuple())

    for date_file in reg_file_list:
        # 把目录和文件名合成一个路径
        abs_file = os.path.join(file_dir, date_file)
        # 获取文件的访问时间 以时间戳的形式
        file_timestamp = os.path.getatime(abs_file)
        # 如果文件夹的访问时间 时间戳 小于等于 n天前的时间戳 就并删除
        if float(file_timestamp) <= float(n_days_agos_timestamps):
            logging.info('过期匹配到文件：[%s]' % abs_file)
            # print "匹配到文件:" ,abs_file
            # 返回满足条件的文件
            if os.path.isfile(abs_file):
                os.remove(abs_file)
                logging.info('删除文件：[%s]成功' % abs_file)
            if os.path.isdir(abs_file):
                shutil.rmtree(abs_file)
                logging.info('删除目录：[%s]成功' % abs_file)

# 读取配置文件并传入对应的参数给find_file   根据，分割如果参数格式不正确则记录日志
def read_conf(file_path):
    with open(file_path,'r',encoding = 'utf-8') as f:
        # print(f.read())
        for line in f:
            line_list = line.strip().split(',')
            if len(line_list) != 3:
                logging.warning('%s 行配置不正确' % line.strip())
                continue
            file_dir = line_list[0]
            file_re = line_list[1]
            expire_time = line_list[2]
            find_file(file_dir, file_re, expire_time)


if __name__ == "__main__":
    # print(sys.argv[1])
    read_conf(sys.argv[1])
