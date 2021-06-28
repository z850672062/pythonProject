#!/usr/bin/env python 
# encoding: utf-8

"""
该程序可以批量修改文件名或目录
生成配置文件
path
Pointer
path为list类型，可以添加多个路径
Pointer为指针，1 为 目录，2为文件，3为目录和文件，
加入日志系统，生成ReNameLog.log（算了）
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

    if Pointer == '3':
        # 遍历Pathlist参数中的文件路径
        for path_cfg in Pathlist:
            # 1、给file_name_list赋值 ,值为os返回路径全部名称
            file_name_list = os.listdir(path_cfg)
            # 遍历配置文件中的路径下的所有目录和文件信息
            # for path in pathlib.Path(path_cfg).iterdir():
                # 遍历enumerate并用path.with.name更改路径名称, 更改最后一级路径名
            for path, index, file_name in enumerate(file_name_list),pathlib.Path(path_cfg).iterdir():
                name = path.with_name(str(index + 1) + '、' + file_name)

                # path.rename(name)
                print(name)






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