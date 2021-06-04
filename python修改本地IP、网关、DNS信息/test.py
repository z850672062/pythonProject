#!/usr/bin/env python 
# encoding: utf-8
from wmi import WMI
import re
import os
import re
import pathlib
from time import sleep
from wmi import WMI
from configobj import ConfigObj
# class Pepple:
#
#     def __init__(self,name,text):
#         self.name = '2'
#         self.text = '真帅'
#     # def __str__(self):
#     #     return self.name
#     def write(self):
#         print(self.name + self.text)
#
# if __name__ == '__main__':
#     person = Pepple('3','真丑')
#     print(person)
class UpdateIp(object):
    #初始化函数定义
    def __init__(self):
        self.wmiservice = WMI()
        # 获取到本地所有有网卡信息,list
        #IPEnabled=True为获取 IP不为空的网卡信息
        self.configs = self.wmiservice.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    # #用ip判断网卡是否存在 返回第一张网卡
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
    def runset(self, nic_num,ip, subnetmask, interway, dns):
        #调用第一张网卡信息
        adapter = self.configs[nic_num]
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

def CHG_NIC(config_dict):
    config_dict
    update = UpdateIp()
    update.runset([config_dict['IP']], [config_dict['SubnetMask']],
                  [config_dict['Gateway']], [config_dict['DNS']])
#
def nic_namelist():
    c = WMI()
    temp_nicname = []
    for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        temp_nicname.append(nic.Description)
    return temp_nicname

    # print(temp)


        # if nic_name
    # print((c.Win32_NetworkAdapterConfiguration(IPEnabled=True))[0])
    # print((c.Win32_NetworkAdapterConfiguration(IPEnabled=True))[1])
    # adapter = (c.Win32_NetworkAdapterConfiguration(IPEnabled=True))
    # print(adapter)
    # ipres = adapter.EnableStatic(IPAddress=['192.168.10.2'], SubnetMask=['255.255.255.0'])
    # # 修改网关 gatewayCostMetric为 网关接口跃点数列表
    # wayres = adapter.SetGateways(DefaultIPGateway=['192.168.10.1'], GatewayCostMetric=[1])
    # print(ipres)

if __name__ == '__main__':
    nic_name = nic_namelist()
    nic_namelen = len(nic_name)
    print('总共有%s张网卡' % nic_namelen)
    for i in nic_name:
        print(i)

    nic_num = input('请输入你想修改的网卡前面的数字：')
    my_ip = UpdateIp
    if nic_num == nic_num:
        my_ip.runset(nic_num)




# test2 = {'是' : '手势'}
# print(test2['是'])


# class test:
#     b = {"192.168.2.103", "fe80::29c1:83cf:bebc:22c0"}
#
#     def IP(self):
#         a = {"192.168.2.103", "fe80::29c1:83cf:bebc:22c0"}
#     def dict1(self):
#         self.IP

#
#
#
#
#
# t2 = test()
# t2.dict1()
# b = list(t2.b)
# print(b)
    # tmpmsg = {}
    # tmpmsg['硬盘名称'] = disk.Caption
    # tmpmsg['服务编码'] = disk.SerialNumber.strip()
    # tmpmsg['容量'] = int(int(disk.Size) / 1024 / 1024 / 1024)
    # disks.append(tmpmsg)
#
# class GameMach:
#
#     def __init__(self):
#         self.screen = '三星显示器'
#         self.youxika = '游戏卡'
#         self.shoubing = '手柄'
#
#
#
#
#     def start(self):
#         print('开机中。。')
#
#     def play(self):
#         print(self.youxika + '插入')
#         print(self.screen + '显示出游戏画面')
#
# Switch = GameMach()
# Switch.start()
# Switch.play()
# print(Switch.screen)
