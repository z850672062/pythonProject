#!/usr/bin/env python 
# encoding: utf-8
from wmi import WMI
import re
# class Pepple:
#
#     def __init__(self,name,text):
#         self.name = name
#         self.text = text
#
#     def write(self):
#         print(self.name + self.text)
#
# if __name__ == '__main__':
#     person = Pepple('3','真丑')
#     person.write()


#
def test():
    c = WMI()
    disks = []
    flag = 0
    # for disk in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
    #     print(type(disk.Index))
    #     print(disk)
    #     ip = re.findall("\d+.\d+.\d+.\d+", disk.IPAddress[0])
    #     print(ip)
    # print((c.Win32_NetworkAdapterConfiguration(IPEnabled=True))[0])
    # print((c.Win32_NetworkAdapterConfiguration(IPEnabled=True))[1])
    adapter = (c.Win32_NetworkAdapterConfiguration(IPEnabled=True))[1]
    print(adapter)
    ipres = adapter.EnableStatic(IPAddress=['192.168.10.2'], SubnetMask=['255.255.255.0'])
    # 修改网关 gatewayCostMetric为 网关接口跃点数列表
    wayres = adapter.SetGateways(DefaultIPGateway=['192.168.10.1'], GatewayCostMetric=[1])
    print(ipres)
test()

test2 = {'是' : '手势'}
print(test2['是'])


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