#!/usr/bin/env python 
# encoding: utf-8

import os
import re
import pathlib
from time import sleep
from wmi import WMI
from configobj import ConfigObj

#创建更新IP类
class UpdateIp(object):
    #初始化函数定义
    def __init__(self):
        self.wmiservice = WMI()
        # 获取到本地所有有网卡信息,list
        #IPEnabled=True为获取 IP不为空的网卡信息
        self.configs = self.wmiservice.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    # #返回带有IP的网卡
    # def get_inter(self):
    #     flag = 0
    #     # 遍历所有网卡，找到要修改的那个
    #     for con in self.configs:
    #         #con.IPAddress[0]为调用Win32_NetworkAdapterConfiguration方法里的IPAddress的值
    #         ip = re.findall("\d+.\d+.\d+.\d+", con.IPAddress[0])
    #
    #         if len(ip) > 0:
    #             #结束循环返回第一张网卡
    #             return 1
    #         else:
    #             flag = flag+1
    #
    def runset(self, ip, subnetmask, interway, dns):
        #调用第一张网卡信息
        adapter = self.configs[self.get_inter()]
        # 开始执行修改ip、子网掩码、网关
        #EnableStatic方法可以修改里面的值
        ipres = adapter.EnableStatic(IPAddress=ip, SubnetMask=subnetmask)
        #成功的话ipres将会返回元组(0,)
        if ipres[0] == 0:
            print('设置IP成功')
        else:
            if ipres[0] == 1:
                print('设置IP成功，需要重启计算机！')
            else:
                print('修改IP失败')
                return False
        #修改网关
        wayres = adapter.SetGateways(DefaultIPGateway=interway, GatewayCostMetric=[1])
        if wayres[0] == 0:
            print('设置网关成功')
        else:
            print('修改网关失败')
            return False
        #修改dns
        dnsres = adapter.SetDNSServerSearchOrder(DNSServerSearchOrder=dns)
        if dnsres[0] == 0:
            print('设置DNS成功,等待3秒刷新缓存')
            sleep(3)
            # 刷新DNS缓存使DNS生效
            os.system('ipconfig /flushdns')
        else:
            print('修改DNS失败')
            return False

def config_handle():
    config['NIC0'] = {}
    # config['NIC1'] = {}
    config['NIC0']['IP'] = '192.168.10.2'
    config['NIC0']['SubnetMask'] = '255.255.255.0'
    config['NIC0']['Gateway'] = '192.168.10.1'
    config['NIC0']['DNS'] = '192.168.10.1'
    config.write()



def config_read():
    config = ConfigObj(config_path,encoding='UTF-8')
    temp_dict = {}
    temp_dict['IP'] = config['NIC0']['IP']
    temp_dict['SubnetMask'] = config['NIC0']['SubnetMask']
    temp_dict['Gateway'] = config['NIC0']['Gateway']
    temp_dict['DNS'] = config['NIC0']['DNS']

    return temp_dict

def CHG_NIC(config_dict):
    config_dict
    update = UpdateIp()
    update.runset([config_dict['IP']], [config_dict['SubnetMask']],
                  [config_dict['Gateway']], [config_dict['DNS']])

def nic_namelist():
    c = WMI()
    temp_nicname = []
    for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        temp_nicname.append(nic.Description)
    return temp_nicname

if __name__ == '__main__':
    # 实例化一个ConfigObj对象
    config = ConfigObj()
    #当前路径
    path_0 = pathlib.Path.cwd()
    #配置名称
    config_name = 'NICIP_info.ini'
    #配置路径
    config_path = str(path_0) + '\\' + config_name
    print('按0自动获取IP地址DNS地址')
    print('按1运行配置文件修改IP地址、网关等信息')
    temp_num = str(input('请输入"0"或"1"：'))
    if temp_num == '1':
        # 生成配置文件/修改网卡信息
        while True:
            # 判断目录下是否存在该表格
            config_judge = os.path.isfile(str(config_path))
            if config_judge == True:
                print('修改数据中...')
                # 实例化配置读取方法
                config_dict = config_read()
                # 调用chg_nic改变网卡ip等信息
                CHG_NIC(config_dict)
                break;
            else:
                print('文件不存在,生成中...')
                config.filename = str(config_path)
                config_handle()
                print('生成完毕！')
                print('请打开NICIP_info.ini文件修改你的数据保存之后再次打开该程序。')
                break;
    else:
        print('自动获取ip')
    #实例化nic_namelist
    nic_name = nic_namelist()
    #获取nic_name的长度
    nic_namelen = len(nic_name)
    print('总共有%s张网卡' % nic_namelen)
    #循环显示nic_name 列表
    for i in nic_name:
        print(i)

    nic_num = input('请输入你想修改的网卡前面的数字：')
    my_ip = UpdateIp
    if nic_num == nic_num:
        my_ip.runset(nic_num)










