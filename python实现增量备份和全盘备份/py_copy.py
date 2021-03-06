#!/usr/bin/env python 
# encoding: utf-8

"""
2021-6-29 16:55:19
新增功能：
加入日志系统，和路径排除功能：
报错日志和路径排除日志
2021-7-1 13:16:56
修改完全备份：
先完全备份然后删除上星期

"""

import time
import os
import datetime
import zipfile
import _pickle as p
import hashlib
import pathlib
import logging
from configobj import ConfigObj


# 记录日志
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)-1d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='BackupError.log',
                    filemode='a')

# md5校验
def md5check(fname):
    # 生成一个md5的hash对象
    m = hashlib.md5()
    # ‘rb’：表示以二进制方式读取文件。该文件必须已存在。
    with open(fname,'rb') as fobj:
        while True:
            # 从打开的文件中读取数据
            data = fobj.read(4096)
            if not data:
                break
            #     更新加密
            m.update(data)
    #         返回加密字符串
    return m.hexdigest()
# 全盘备份
def full_backup(config_dict):
    src_dirlist = config_dict['src_dir']

    dst_dir = config_dict['dst_dir']
    expath_list = config_dict['expath_list']
    # md5file = str(path_0) + '\\' + config_dict['md5file']
    # md5dict = {}
    # 定义par_dir, base_dir 两个参数，返回src_dir去掉尾部/字符串，并分离出目录路径和文件名给par_dir, base_dir 两个参数赋值
    # par_dir, base_dir = os.path.split(src_dir.rstrip('/'))
    back_name = 'full_%s.zip' % (time.strftime('%Y%m%d'))
    # full_name为目标路径的打包名称，将目标路径和back路径相加
    full_name = os.path.join(dst_dir, back_name)
    print(src_dirlist)
    print('完全备份中...')
    # 遍历src_dirlist中的路径并打包
    for src_dir in src_dirlist:
        # zipfile打包
        with zipfile.ZipFile(full_name, 'a') as myzip:
            for path, folder, files in os.walk(src_dir):
                for fname in files:
                    path2 = "%s\\%s" % (path, fname)
                    print(path2)
                    if path2 in expath_list:
                        logging.info('完全备份排除路径：' + path2)
                        pass;
                    else:
                        try:
                            myzip.write(path2, compress_type=zipfile.ZIP_DEFLATED)
                        except Exception as e:
                            logging.warning("zip打包跳过错误文件" + str(e))
                            continue;



# 增量备份 根据md5值对比来对个别文件进行增量备份
def incr_backup(config_dict,path_0):
    src_dirlist = config_dict['src_dir']
    dst_dir = config_dict['dst_dir']
    expath_list = list(config_dict['expath_list'])

    md5file = str(path_0) + '\\' + config_dict['md5file']
    md5dict = {}
    md5new = {}
    # 定义par_dir, base_dir 两个参数，返回src_dir去掉尾部/字符串，并分离出目录路径和文件名给par_dir, base_dir 两个参数赋值
    # par_dir, base_dir = os.path.split(src_dir.rstrip('/'))
    back_name = 'incr.zip'
    # full_name为目标路径的打包名称，将目标路径和back路径相加
    full_name = os.path.join(dst_dir, back_name)
    print(src_dirlist)

    # 判断目录下是否存在该文件
    config_judge = os.path.isfile(str(full_name))
    if config_judge == True:
        print('增量备份中...')
        for src_dir in src_dirlist:
            # 将path:md5写入md5new用于保存md5.data
            for path, folder, files in os.walk(src_dir):
                for fname in files:
                    path2 = "%s\\%s" % (path, fname)
                    if path2 in expath_list:
                        pass;
                    else:
                        try:
                            # 每遍历一次将src_dir的path 和 文件名相加
                            full_path = os.path.join(path, fname)
                            # 每次将full_path的md5校验码加入md5字典 ： path:md5
                            md5new[full_path] = md5check(full_path)
                        except Exception as e:
                            print("报错了！！！", e)
                            logging.warning("md5新字典数据生成跳过该错误文件" + str(e))
                            continue;


        # print(md5new)
        # 使用load加载之前的mdf5文件
        with open(md5file, 'rb') as fobj:
            md5old = p.load(fobj)
        # 使用pickle序列化并写入文件
        with open(md5file, 'wb') as fobj:
            p.dump(md5new, fobj, 0)
        # zipfile打包
        with zipfile.ZipFile(full_name, 'a') as myzip:
            for key in md5new:
                if md5old.get(key) != md5new[key]:
                    try:
                        myzip.write(key, compress_type=zipfile.ZIP_DEFLATED)
                    except Exception as e:
                        logging.warning("跳过该错误文件" + str(e))
                        continue;

    else:
        # 遍历src_dirlist中的路径并打包
        print('生成增量备份压缩包中...')
        for src_dir in src_dirlist:
            # zipfile打包
            with zipfile.ZipFile(full_name, 'a') as myzip:
                for path, folder, files in os.walk(src_dir):
                    for fname in files:
                        path2 = "%s\\%s" % (path, fname)
                        print(path2)
                        if path2 in expath_list:
                            logging.info('增量备份排除路径：' + path2)
                            pass;
                        else:
                            try:
                                myzip.write(path2, compress_type=zipfile.ZIP_DEFLATED)
                            except Exception as e:
                                logging.warning("zip打包跳过错误文件" + str(e))
                                continue;

            # 将path:md5写入md5dict用于保存md5.data
            for path, folder, files in os.walk(src_dir):
                for fname in files:
                    path2 = "%s\\%s" % (path, fname)
                    if path2 in expath_list:
                        pass;
                    else:
                        try:
                            # 每遍历一次contents将src_dir的path 和 文件名相加
                            full_path = os.path.join(path, fname)
                            # 每次将full_path的md5校验码加入md5字典 ： path:md5
                            md5dict[full_path] = md5check(full_path)
                        except Exception as e:
                            print("报错了！！！", e)
                            logging.warning("md5字典数据生成跳过该错误文件" + str(e))
                            continue;


            # print(md5dict)
            # 使用pickle序列化并写入文件
            with open(md5file, 'wb') as fobj:
                p.dump(md5dict, fobj, 0)
        incr_backup(config_dict,path_0)

# 删除完全备份（指定星期备份完成后删除上次备份的完全备份）
def del_fullback(config_dict):
    dst_dir = config_dict['dst_dir']
    # 获取系统当前时间
    today = datetime.datetime.now()
    # 7天
    n_days = datetime.timedelta(days=int(7))
    # 7天前日期
    n_days_agos = (today - n_days).strftime('%Y%m%d')

    # print(n_days_agos)
    n_days_fullbackup_file = 'full_%s.zip' % n_days_agos
    # print(n_days_fullbackup_file)
    # 遍历指定路径的所有文件，加入if判断文件是否存在 ，存在就删除
    for path in pathlib.Path(dst_dir).iterdir():
        if n_days_fullbackup_file in str(path):
            # unlink方法可以删除文件和取消链接
            pathlib.Path(str(path)).unlink()
            logging.info('删除7天前的完全备份文件:%s' % n_days_fullbackup_file)



#初始化配置文件写入
def config_handle():
    config['copy'] = {}
    config['copy']['src_dir'] = 'path,path,...'  #返回的是列表list格式
    config['copy']['dst_dir'] = 'path'
    config['copy']['expath_list'] = 'path,..'
    config['copy']['md5file'] = 'md5.data'
    config['copy']['f_backup_week'] = 'Mon'
    config.write()

#配置文件读取
def config_read():
    config = ConfigObj(config_path,encoding='UTF-8')
    temp_dict = {}
    temp_dict['src_dir'] = config['copy']['src_dir']
    temp_dict['dst_dir'] = config['copy']['dst_dir']
    temp_dict['expath_list'] = config['copy']['expath_list']
    temp_dict['md5file'] = config['copy']['md5file']
    temp_dict['f_backup_week'] = config['copy']['f_backup_week']
    return temp_dict

if __name__ == '__main__':

    try:
        # 实例化一个ConfigObj对象
        config = ConfigObj()
        # 当前路径
        path_0 = pathlib.Path.cwd()
        # 配置名称
        config_name = 'Backup.ini'
        # 配置路径
        config_path = str(path_0) + '\\' + config_name
        # 判断目录下是否存在配置文件，不存在就生成
        config_judge = os.path.isfile(str(config_path))
        if config_judge == True:
            print('配置文件检查存在，将开始运行主函数')
        else:
            print('配置文件不存在,生成中...')
            config.filename = str(config_path)
            config_handle()
            print('生成完毕！')
            print('请打开%s文件修改你的数据保存之后再次打开该程序。' % config_name)
            input()
        # 实例化文件读取
        config_dict = config_read()
        # 获取配置文件中的完全备份日期
        f_backup_week = config_dict['f_backup_week']
        if config_judge == True:
            if time.strftime('%a') == f_backup_week:
                # 对完全备份进行传参
                full_backup(config_dict)
                logging.info('完全备份完毕')
                # 删除
                del_fullback(config_dict)

            else:
                # 对增量备份进行传参
                incr_backup(config_dict, path_0)
                logging.info('增量备份完毕')



    except Exception as e:
        logging.warning(e)

