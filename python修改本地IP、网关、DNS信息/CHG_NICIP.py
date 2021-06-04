#!/usr/bin/env python 
# encoding: utf-8

import os
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
    #定义自动获取方法
    def auto_set(self,nic_num):
        # 调用用户输入的索引网卡信息
        adapter = self.configs[nic_num]
        # 修改dhcp为自动获取
        dhcp = adapter.EnableDHCP()
        # 成功的话ipres将会返回元组(0,)
        if dhcp[0] == 0:
            print('设置DHCP自动获取成功')
        else:
            if dhcp[0] == 1:
                print('设置DHCP自动获取成功，需要重启计算机！')
            else:
                print('设置DHCP自动获取失败')
                return False
        # dns自动获取
        dnsres = adapter.SetDNSServerSearchOrder(DNSServerSearchOrder=[])
        if dnsres[0] == 0:
            print('设置DNS成功,等待3秒刷新缓存')
            sleep(3)
            # 刷新DNS缓存使DNS生效
            os.system('ipconfig /flushdns')
        else:
            print('修改DNS失败')
            return False

    #修改IP配置
    def runset(self,nic_num,ip, subnetmask, interway, dns):
        #调用用户输入的索引网卡信息
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
#初始化配置文件写入
def config_handle():
    config['NIC0'] = {}
    config['NIC0']['IP'] = '192.168.10.2'
    config['NIC0']['SubnetMask'] = '255.255.255.0'
    config['NIC0']['Gateway'] = '192.168.10.1'
    config['NIC0']['DNS'] = '192.168.10.1'
    config.write()


#配置文件读取
def config_read():
    config = ConfigObj(config_path,encoding='UTF-8')
    temp_dict = {}
    temp_dict['IP'] = config['NIC0']['IP']
    temp_dict['SubnetMask'] = config['NIC0']['SubnetMask']
    temp_dict['Gateway'] = config['NIC0']['Gateway']
    temp_dict['DNS'] = config['NIC0']['DNS']

    return temp_dict

#修改NIC卡信息 ip、等
def CHG_NIC(config_dict,nic_num):
    config_dict
    #实例化 UpdateIp类
    update = UpdateIp()
    #调用runset方法
    update.runset(nic_num,[config_dict['IP']], [config_dict['SubnetMask']],
                  [config_dict['Gateway']], [config_dict['DNS']])
#返回NIC名称列表
def nic_namelist():
    c = WMI()
    temp_nicname = []
    for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        temp_nicname.append(nic.Description)
    return temp_nicname

if __name__ == '__main__':
    #实例化UpdateIp类
    CHG_NIC_auto = UpdateIp()
    # 实例化一个ConfigObj对象
    config = ConfigObj()
    # 实例化nic_namelist
    nic_name = nic_namelist()
    # 获取nic_name的长度
    nic_namelen = len(nic_name)
    #当前路径
    path_0 = pathlib.Path.cwd()
    #配置名称
    config_name = 'NICIP_info.ini'
    #配置路径
    config_path = str(path_0) + '\\' + config_name
    print('按0自动获取IP地址DNS地址')
    print('按1运行配置文件修改IP地址、网关等信息')
    temp_num = str(input('请输入"0"或"1"：'))
    try:
        if temp_num == '1':
            # 生成配置文件/修改网卡信息
            while True:
                # 判断目录下是否存在该表格
                config_judge = os.path.isfile(str(config_path))
                if config_judge == True:
                    print('总共有%s张网卡' % nic_namelen)
                    #处理nic_name 在每个索引下增加 数字
                    for index in range(len(nic_name)):
                        nic_name[index] = str(index) + ' —— ' + nic_name[index]
                    # 循环显示nic_name 列表
                    for i in nic_name:
                        print(i)
                    nic_num = int(input('请输入你想修改的网卡前面的数字：'))

                    if nic_num == nic_num:
                        print('修改数据中...')
                        # 实例化配置读取方法 返回 ip等配置数据
                        config_dict = config_read()
                        # 调用chg_nic改变网卡ip等信息,（传参：配置文件的信息，网卡索引数值）
                        CHG_NIC(config_dict,nic_num)

                    # print('修改数据中...')
                    # # 实例化配置读取方法
                    # config_dict = config_read()
                    # # 调用chg_nic改变网卡ip等信息
                    # CHG_NIC(config_dict)
                    break;
                else:
                    print('文件不存在,生成中...')
                    config.filename = str(config_path)
                    config_handle()
                    print('生成完毕！')
                    print('请打开NICIP_info.ini文件修改你的数据保存之后再次打开该程序。')
                    input()
                    break;
        else:

            print('总共有%s张网卡' % nic_namelen)
            # 处理nic_name 在每个索引下增加 数字
            for index in range(len(nic_name)):
                nic_name[index] = str(index) + ' —— ' + nic_name[index]
            # 循环显示nic_name 列表
            for i in nic_name:
                print(i)
            nic_num = int(input('请输入你想修改的网卡前面的数字：'))
            if nic_num == nic_num:
                print('设置自动获取ip中...')
                CHG_NIC_auto.auto_set(nic_num)


    except Exception as e:
        print("报错了！!！",e)















