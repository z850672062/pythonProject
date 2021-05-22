#!/usr/bin/env python
# encoding: GBK
import os
import re
import sys
import time
import datetime
import logging
import shutil


# reload(sys)
# sys.setdefaultencoding('utf-8')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)-1d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a')


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
# ������� Fri, 21 May 2021 18:51:20 main.py [line:21] DEBUG This is debug message

#
#�������ư���XXX���ļ����ļ���
def find_file(file_dir, file_re='[^XXX$]+', expire_time=7):
    #     print sys.getdefaultencoding()
    if file_re == '':
        logging.error('file_re is null,exit')
        return None
    # �����������
    # file_dir = file_dir.decode("utf-8")
    # file_re = file_re.decode("utf-8")
    logging.info('������� :Ŀ¼ [%s]��������ʽ[%s],�������� [%s]' % (file_dir, file_re, expire_time))
    # Ŀ¼�������ļ�
    all_file = os.listdir(file_dir)
    # ƥ��������ļ�
    reg_file_list = []
    reg_str = file_re
    for reg_file in all_file:
        if re.match(reg_str, reg_file):
            logging.info('����ƥ�䵽�ļ���[%s]' % reg_file)

            # print(reg_file)
            reg_file_list.append(reg_file)
    print(reg_file_list)
    # �������ʱ����ļ�
find_file("D:/test")
#     # ��ǰʱ��
#     today = datetime.datetime.now()
#     # n��
#     n_days = datetime.timedelta(days=int(expire_time))
#     # n��ǰ����
#     n_days_agos = today - n_days
#     # n��ǰʱ���
#     n_days_agos_timestamps = time.mktime(n_days_agos.timetuple())
#
#     for date_file in reg_file_list:
#         abs_file = os.path.join(file_dir, date_file)
#         file_timestamp = os.path.getmtime(abs_file)
#         if float(file_timestamp) <= float(n_days_agos_timestamps):
#             logging.info('����ƥ�䵽�ļ���[%s]' % abs_file)
#             # print "ƥ�䵽�ļ�:" ,abs_file
#             # ���������������ļ�
#             if os.path.isfile(abs_file):
#                 os.remove(abs_file)
#                 logging.info('ɾ���ļ���[%s]�ɹ�' % abs_file)
#             if os.path.isdir(abs_file):
#                 shutil.rmtree(abs_file)
#                 logging.info('ɾ��Ŀ¼��[%s]�ɹ�' % abs_file)
#
#
# def read_conf(file_path):
#     with open(file_path, 'r') as f:
#         for line in f:
#             line_list = line.strip().split(',')
#             if len(line_list) != 3:
#                 logging.warning('%s �����ò���ȷ' % line.strip())
#                 continue
#             file_dir = line_list[0]
#             file_re = line_list[1]
#             expire_time = line_list[2]
#             find_file(file_dir, file_re, expire_time)
#
#
# if __name__ == "__main__":
#     read_conf(sys.argv[1])