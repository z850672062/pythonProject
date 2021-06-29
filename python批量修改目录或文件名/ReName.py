#!/usr/bin/env python 
# encoding: utf-8

"""
该程序可以批量修改文件名或目录
生成配置文件
path
Pointer
path为list类型，可以添加多个路径
Pointer为指针，Pointer为1将会修改文件名前缀 ，Pointer为2将会取消所有目录和文件 前面的数字加、
完成：2021-6-29 23:24:47
Pointer为2需要修改 有BUG


加入日志系统，生成ReNameLog.log
记录修改过的文件

"""
import os
import pathlib
import  sys
from configobj import ConfigObj
#初始化配置文件写入

def config_handle():
    config['ReName'] = {}
    config['ReName']['Path'] = 'path,path,...'  #返回的是列表list格式
    config['ReName']['Pointer'] = 'number'
    config.write()

#配置文件读取
def config_read(config_path):
    config = ConfigObj(config_path,encoding='UTF-8')
    temp_dict = {}
    temp_dict['Path'] = config['ReName']['Path']
    temp_dict['Pointer'] = config['ReName']['Pointer']
    return temp_dict

def create_cfg():

    # 当前路径
    path_0 = pathlib.Path.cwd()
    # 获取程序本身名称
    base_name = os.path.basename(sys.argv[0]).split('.')[0]
    # 配置名称
    config_name = '%sCfg.ini' % base_name
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
    return config_path

# 修改目录或文件或目录和文件
def rename(config_dict):
    Path = config_dict['Path']
    Pointer = config_dict['Pointer']
    handle_filelist = []

    num = -1
    # Pointer为1将会修改文件名前缀   例如：test.txt → 1、test.txt
    if Pointer == '1':
        # 给file_name_list赋值 ,值为os返回路径全部名称
        file_name_list = os.listdir(str(Path))

        # 注释
        # enumerate函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中 start为设置索引下标
        for index, file_name in enumerate(file_name_list,start=1):
            handle_file = str(index) + '、' + file_name
            handle_filelist.append(handle_file)
        # handle_filelist为处理过的文件列表
        print(handle_filelist)
        # 循环遍历指定path中的目录和文件
        for path in pathlib.Path(Path).iterdir():
            # num参数让handle_filelist[num]循环遍历吃list中的数据
            num = num + 1
            # path.with_name更改路径名称, 更改最后一级路径名（文件名）
            path.rename(path.with_name(handle_filelist[num]))

    #  Pointer为2将会取消所有目录和文件前面的数字加、  例如：1、test.txt → test.txt
    if Pointer == '2':
        # 给file_name_list赋值 ,值为os返回路径全部名称
        file_name_list = os.listdir(str(Path))
        # 循环遍历参数中的文件名称 并进行名称处理和加入list
        for i in file_name_list:
            hand_file = max(i.split('、'))
            handle_filelist.append(hand_file)
        print(handle_filelist)
        # 循环遍历指定path中的目录和文件
        for path in pathlib.Path(Path).iterdir():
            # num参数让handle_filelist[num]循环遍历吃list中的数据
            num = num + 1
            # path.with_name更改路径名称, 更改最后一级路径名（文件名）
            path.rename(path.with_name(handle_filelist[num]))

if __name__ == '__main__':
    try:
        # 实例化一个ConfigObj对象
        config = ConfigObj()
        # 实例化 create_cfg返回的config_path
        config_path = create_cfg()
        # 实例化文件读取
        config_dict = config_read(config_path)

        # 运行rename方法
        rename(config_dict)
    except Exception as e:
        print('报错了！！！', e)