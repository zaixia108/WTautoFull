import hashlib
import os
import time

import requests
#检测windows程序后台运行
from loguru._logger import start_time


def check_process(name):
    #检测是否有进程在运行
    #返回值为进程名
    process_list = []
    for i in os.popen('tasklist'):
        process_list.append(i.strip())
    for i in process_list:
        if i.find(name) != -1:
            print(name + '正在运行')
            return True
        else:
            print(name + '未运行')
            return False


def report(message):#qq群发消息提示卡死
    with open('qq.ini') as q:
        qq = q.readline()
    url = 'http://47.96.160.181:7766/hqzp'
    data = {
        'qq': qq,
        'ts': '',
        'sign': '',
        'message': message
    }
    m = hashlib.md5()
    ts = int(time.time() * 1000)
    m.update((qq + str(ts) + "wi@@onzzzjwi1#@!").encode())
    sign = m.hexdigest()
    data['ts'] = ts
    data['sign'] = sign
    resp = requests.post(url, data=data).text


def checkini():
#读取pic/check/check.ini最后10行并且不显示\n
    with open('pic/check/check.ini') as f:
        check = f.readlines()
        check10 = check[-10:]
        print(check10)
#排除check10里的换行符
    check10 = [i.strip() for i in check10]
    return check10


def checkrunning():
# 每60秒检查一次check10是否一致
    while True:
        c1 = checkini()
        l1 = c1[-1]
        time.sleep(60)
        c2 = checkini()
        l2 = c2[-1]
        if l1 == l2 and l1 != '正在加入，请稍后':
            print('程序卡住了')
            report('脚本卡住了')
        elif l1 == l2 and l1 == '正在加入，请稍后':
            print('程序正常运行')
        elif l1 != l2:
            print('程序正常运行')


