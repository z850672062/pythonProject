#!/usr/bin/env python 
# encoding: utf-8
"""
模板文件

"""

import os
import pathlib
from configobj import ConfigObj
#初始化配置文件写入


def config_handle():
    config['ReName'] = {}
    config['ReName']['Path'] = 'path,path,...'  #返回的是列表list格式
    config['ReName']['Pointer'] = 'number'
    config.write()

#配置文件读取
def config_read():
    config = ConfigObj(config_path,encoding='UTF-8')
    temp_dict = {}
    temp_dict['Path'] = config['ReName']['Path']
    temp_dict['Pointer'] = config['ReName']['Pointer']
    return temp_dict

# 修改目录或文件或目录和文件
def rename(config_dict):
    Pathlist = config_dict['Path']
    Pointer = config_dict['Pointer']

    for path in Pathlist:


        print(path)


if __name__ == '__main__':
    try:
        # 实例化一个ConfigObj对象
        config = ConfigObj()
        # 当前路径
        path_0 = pathlib.Path.cwd()
        # 配置名称
        config_name = 'ReNameCfg.ini'
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
        rename(config_dict)

    except Exception as e:
        print('报错了！！！', e)