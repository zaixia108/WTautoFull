import random
import time
from concurrent.futures import ThreadPoolExecutor

import pyautogui
import win32gui

import key
from find import find, locate, find_lit_mat
from presskey import hold, wtpress, key_down, key_up, press
from utils import active, logger_log as log, click

flag = False
run_flag = False


def run():  # 转向，定速
    global flag
    global run_flag
    while True:
        print(flag)
        print('转向')
        if flag:
            return
        if run_flag is True:
            time.sleep(1)
            continue
        active()
        a = random.randint(8, 20)
        b = random.randint(5, 10)
        c = random.randint(1, 100)
        time.sleep(a)
        if c > 50:
            hold(k=key.key_D, t=b)
            speed()
        else:
            hold(k=key.key_A, t=b)
            speed()


def press_times(k, i):#按某一个按键多少次
    for a in range(i):
        wtpress(k)


def select_ship02():#选择船加入战斗
    global flag
    while True:
        if flag:
            return
        active()
        time.sleep(5)
        ship = find('pic/join.png')
        findtime = find('pic/time.png')
        time.sleep(1)
        if ship is not None and findtime is not None:
            time.sleep(1)
            click(ship)
            time.sleep(1)
            prepare()


def autorep():#检测自动维修
    a01 = locate('pic/6b.png', 0.8)  # 492, 731, 539, 780)
    if a01 is not None:
        log('press6')
        wtpress(k=key.key_6)
    a02 = locate('pic/7b.png', 0.8)  # 542, 731, 586, 780)
    if a02 is not None:
        log('press7')
        wtpress(k=key.key_7)
    a03 = locate('pic/8b.png', 0.8)  # 592, 731, 637, 780)
    if a03 is not None:
        log('press8')
        wtpress(k=key.key_8)


def speed():#改变速度
    f5 = locate('pic/53f.png', 0.8)
    f4 = locate('pic/43f.png', 0.8)
    f3 = locate('pic/33f.png', 0.8)
    f2 = locate('pic/23f.png', 0.8)
    f1 = locate('pic/13f.png', 0.8)
    s0 = locate('pic/stop.png', 0.8)
    b1 = locate('pic/13b.png', 0.8)
    b2 = locate('pic/23b.png', 0.8)
    b3 = locate('pic/43b.png', 0.8)
    print(f5, f4, f3, f2, f1, s0, b1, b2, b3)
    if f5 is not None:
        press_times(key.key_S, 3)
    elif f4 is not None:
        press_times(key.key_S, 2)
    elif f3 is not None:
        press_times(key.key_S, 1)
    elif f1 is not None and f2 is not None:
        f03 = locate('pic/13t.png', 0.8)
        f04 = locate('pic/23t.png', 0.8)
        print(f03,f04)
        if f03 is not None:
            press_times(key.key_W, 1)
        if f04 is not None:
            press_times(key.key_S, 0)
    elif s0 is not None:
        press_times(key.key_W, 2)
    elif b1 is not None and b2 is not None:
        b01 = locate('pic/13t.png', 0.8)
        b02 = locate('pic/23t.png', 0.8)
        print(b01, b02)
        if b01 is not None:
            press_times(key.key_W, 3)
        if b02 is not None:
            press_times(key.key_W, 4)
    elif b3 is not None:
        press_times(key.key_W, 5)


def prepare():#准备工作，包括换武器，定速，维修检测
    while True:
        p = locate('pic/0.png', 0.8)
        if p is not None:
            changeweapon()
            autorep()
            speed()
            time.sleep(1)
            speed()
            break


def near_danger():#危险检测
    # print(x1, y1, x2, y2)
    global run_flag
    global flag
    i = 0
    while True:
        if flag:
            return
        i = i+1
        print('这是第{}次撞山检测'.format(i))
        hwnd = win32gui.FindWindow('DagorWClass', None)
        rect = win32gui.GetWindowRect(hwnd)
        # print(rect)
        x = rect[0]
        y = rect[1]
        # 302 302+27 712 480+27
        x1 = x + 302
        y1 = y + 302
        x2 = 410
        y2 = 178
        run_flag = False
        if flag:
            return
        active()
        gp = find_lit_mat('pic/giveup.png',0.7,x1,y1,x2,y2)
        danger = find('pic/danger.png')
        time.sleep(3)
        if danger is not None or gp is not None:
            run_flag = True
            log('危险靠近，开始避险')
            avoid_danger()
            time.sleep(1)
            run_flag = False


def avoid_danger():#避险操作
    global flag
    active()
    num = random.randint(1, 100)
    key_down(k=key.key_S)
    if num > 50:
        hold(k=key.key_D, t=15)
    else:
        hold(k=key.key_A, t=15)
    key_up(k=key.key_S)
    time.sleep(30)
    speed()
    time.sleep(1)
    speed()


def changeweapon():#换武器
    key_down(k=key.key_LeftAlt)
    time.sleep(0.5)
    wtpress(k=key.key_2)
    wtpress(k=key.key_3)
    key_up(k=key.key_LeftAlt)
    log('切换武器')


def repaire():#维修保险措施
    global flag
    while True:
        if flag:
            return
        press6 = locate('pic/fire.png',0.85)
        if press6 is not None:
            press(key.key_6)
            time.sleep(1)
        press7 = locate('pic/repaire.png', 0.85)
        if press7 is not None:
            press(key.key_7)
            time.sleep(1)
        press8 = locate('pic/waterdanger.png', 0.85)
        if press8 is not None:
            press(key.key_8)
            time.sleep(1)


def back_to_base():#返回基地检测
    global flag
    i = 0
    while True:
        if flag:
            return
        i = i+1
        log('正在检测运行情况，这是第{}次'.format(i))
        print('正在检测运行情况，这是第{}次'.format(i))
        active()
        backtobase1 = locate('pic/backtobase1.png', 0.8)
        backtobase2 = locate('pic/backtobase2.png', 0.8)
        okk = locate('pic/missioncomplete.png', 0.8)
        backtobase3 = locate('pic/ok02.png', 0.8)
        backtobase4 = locate('pic/end.png', 0.8)
        ulost = locate('pic/lost.png', 0.8)
        complete = locate('pic/ok03.png',0.8)
        if backtobase1 is not None:
            pyautogui.moveTo(backtobase1)
            click(backtobase1)
            time.sleep(6)
            while True:
                check_backtobase1 = locate('pic/backtobase1.png', 0.8)
                time.sleep(0.5)
                if check_backtobase1 is not None:
                    click(check_backtobase1)
                    log('返回基地失败，重新返回基地')
                    continue
                else:
                    log('返回基地成功')
                    break
            BB01 = '船舰摧毁，正在返回基地'
            flag = True
        elif backtobase2 is not None:
            pyautogui.moveTo(backtobase2)
            flag = True
            log('任务结束，正在返回基地')
        elif okk is not None:
            pyautogui.moveTo(okk)
            flag = True
            log('任务结束，返回基地')
        elif backtobase3 is not None:
            pyautogui.moveTo(backtobase3)
            flag = True
            log('发生意外，已经返回基地')
        elif backtobase4 is not None:
            flag = True
            log('任务完成，圆满返回基地')
        elif ulost is not None:
            flag = True
            log('你丢失了链接')
        elif complete is not None:
            flag = True
            log('成功完成任务')
        time.sleep(6)


def main_run():
    global flag
    flag = False
    executor = ThreadPoolExecutor(max_workers=20)
    prepare()
    Run = executor.submit(run)
    Danger = executor.submit(near_danger)
    ship = executor.submit(select_ship02)
    backtobase = executor.submit(back_to_base)
    re = executor.submit(repaire)
    while True:
        time.sleep(1)
        if flag:
            time.sleep(3)
            log('任务结束')
            return True