import os
import time
import win32gui

import key
from find import locate
from join import main_join
from running import main_run
from end import main_end
from utils import logger_log as log, click, selectrun, selet_c, active
from autologin import autologin,steamlogin,choosemode
from presskey import press


def autostart(): #运行
    hwnd = win32gui.FindWindow('DagorWClass', None)
    hwnd1 = win32gui.FindWindow('WarThunderLauncher', None)
    if hwnd == 0 and hwnd1 == 0:
        r = selectrun()
        if r == 2:
            f = autologin()
            if f is None:
                log('ERROR''未成功选择目录')
                log('未成功选择目录')
                return None
            if f is False:
                log('ERROR''选择的目录中没有战雷')
                log('选择的目录中没有战雷')
                return False
        elif r == 1:
            f = steamlogin()
            if f is None:
                log('ERROR''未成功选择目录')
                log('未成功选择目录')
                return None
            if f is False:
                log('ERROR''选择的目录中没有战雷')
                log('选择的目录中没有战雷')
                return False
        else:
            log('未检测到运行配置')
            return False
        log('成功进入游戏')
        time.sleep(2)
        se1 = selet_c()
        if se1 is False:
            log('无需国家或未配置国家')
            return True
        time.sleep(2)
        return True
    elif hwnd != 0 and hwnd1 == 0:
        log('游戏已经开始')
        se = os.path.exists('pic/config/country.txt')
        print('1',se)
        if se is True:
            return True
        else:
            se1 = selet_c()
            print('2',se1)
            if se1 is False:
                log('无需国家或未配置国家')
                return True

def main():
    h = autostart()
    print(h)
    if h is None or h is False:
        return False
    # print(1)
    choosemode()
    log("运行中")
    while True:
        time.sleep(0.5)
        active()
        step1 = main_join()
        if step1 is True:
            log("进入游戏")
        elif step1 is False:
            log("进入游戏失败")
            j0 = locate('pic/0.png', 0.8)
            if j0 is True:
                log("已经在游戏中")
            elif j0 is None or False:
                log("未在游戏中")
                continue
        elif step1 is None:
            log("未知错误")
            press(key.key_Esc)
            continue
        log("第一步运行结束，开始下一步")
        step2 = main_run()
        if step2 is True:
            log("运行正常")
        else:
            log("运行异常")
        log('第二步运行结束，开始下一步')
        step3 = main_end()
        if step3 is True:
            log("战局结束")
        else:
            log("战局结束异常")
        log('最后一步运行结束')

