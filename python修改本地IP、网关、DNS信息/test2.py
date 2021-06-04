#!/usr/bin/env python 
# encoding: utf-8
NIC = ['Intel(R) 82579LM Gigabit Network Connection',
'DW1501 Wireless-N WLAN Half-Mini 卡',
'VirtualBox Host-Only Ethernet Adapter',
'Microsoft Loopback Adapter']


for index in range(len(NIC)) :
    NIC[index] = str(index) + ' —— ' + NIC[index]
for i in NIC:
    print(i)