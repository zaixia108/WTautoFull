import os
import shutil
import random
import subprocess
import win32print
import key
import time
import pyautogui
import win32con
import win32gui
from find import locate, find_lit_mat
import filedialogs



hDC = win32gui.GetDC(0)
wide = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
high = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)


def findwt():
    global pathway
    wtpath = os.path.exists('pic/config/way.txt')
    if wtpath is False:
        FolderPath = filedialogs.open_folder_dialog('选择文件夹路径', 'gbk')
        if FolderPath is None:
            return None
        pathway = FolderPath
        pathway2 = pathway + '/launcher.exe'
        wt = os.path.exists(pathway2)
        if wt is False:
            return False
        with open('pic/config/way.txt','w+') as w:
            w.write(pathway)
            return pathway
    else:
        with open('pic/config/way.txt','r+') as w:
            pathway = w.read()
            return pathway


def findstwt():
    global pathway
    wtpath = os.path.exists('pic/config/stway.txt')
    if wtpath is False:
        FolderPath = filedialogs.open_folder_dialog('选择文件夹路径', 'gbk')
        if FolderPath is None:
            return None
        pathway = FolderPath
        pathway2 = pathway + '/launcher.exe'
        wt = os.path.exists(pathway2)
        if wt is False:
            return False
        with open('pic/config/stway.txt','w+') as w:
            w.write(pathway)
            return pathway
    else:
        with open('pic/config/stway.txt','r+') as w:
            pathway = w.read()
            return pathway


def click(p):
    pyautogui.moveTo(p)
    pyautogui.mouseDown(p, button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(p, button='left')
    time.sleep(0.1)
    pyautogui.moveTo(5, 30)


def openwt():
    global pathway
    way = pathway + '/launcher.exe'
    subprocess.Popen(way)


def startgame():
    hwnd = win32gui.FindWindow('WarThunderLauncher', None)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
    win32gui.SetForegroundWindow(hwnd)
    print('找到窗口')
    while True:
        start = locate('pic/luncher/lunch.png',0.8)
        time.sleep(1)
        if start is not None:
            click(start)
            time.sleep(3)
            hvstart = find_lit_mat('pic/luncher/hvstart.png',0.8,0,0,wide,high)
            if hvstart is not None:
                print('成功打开游戏')
                return
            else:
                continue


def login():
    while True:
        account = find_lit_mat('pic/luncher/warthunder.png',0.8,0,0,wide,high)
        logo = find_lit_mat('pic/lost.png',0.8,0,0,wide,high)
        time.sleep(0.5)
        if account is not None:
            hwnd = win32gui.FindWindow('DagorWClass', None)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
            win32gui.SetForegroundWindow(hwnd)
            login = locate('pic/luncher/login.png',0.8)
            if login is not None:
                click(login)
                print('登录成功')
                time.sleep(1)
                while True:
                    loading = locate('pic/lost.png',0.8)
                    time.sleep(1)
                    if loading is not None:
                        print('已经在游戏界面')
                        return
        elif logo is not None:
            hwnd = win32gui.FindWindow('DagorWClass', None)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
            win32gui.SetForegroundWindow(hwnd)
            time.sleep(1)
            print('已经在游戏界面')
            return


def startcheckin():
    while True:
        checkin = locate('pic/checkin.png',0.8)
        menu = locate('pic/lost.png',0.8)
        time.sleep(2)
        if checkin is not None:
            click(checkin)
            print('点击签到')
            time.sleep(8)
            close = locate('pic/close.png',0.8)
            if close is not None:
                click(close)
                print('签到完毕')
                return
        elif menu is not None:
            print('无需签到')
            return



def startbak():
    global pathway
    shutil.copyfile(pathway + "\config.blk", "pic/config/config.blk.bk")
    shutil.copyfile("pic/config/config.blk", pathway + "\config.blk")


def endbak():
    global pathway
    shutil.copyfile("pic/config/config.blk.bk", pathway + "\config.blk")


def autologin():
    f = findwt()
    if f is None:
        return None
    elif f is False:
        return False
    startbak()
    openwt()
    time.sleep(2)
    startgame()
    login()
    time.sleep(5)
    startcheckin()
    return True


def endoff():
    endbak()
    os.remove('pic/config/config.blk.bk')
    return


def steamlogin():
    f = findstwt()
    if f is None:
        return None
    elif f is False:
        return False
    startbak()
    os.system("start steam://rungameid/236390")
    time.sleep(30)
    while True:
        f = find_lit_mat('pic/steam/run.png',0.8,0,0,wide,high)
        time.sleep(1)
        if f is not None:
            hwnd = win32gui.FindWindow('DagorWClass', None)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
            win32gui.SetForegroundWindow(hwnd)
            while True:
                login = locate('pic/steam/login.png',0.8)
                menu = locate('pic/lost.png',0.8)
                time.sleep(1)
                if login is not None:
                    click(login)
                    print('登录成功')
                    time.sleep(1)
                    while True:
                        loading = locate('pic/lost.png', 0.8)
                        time.sleep(1)
                        if loading is not None:
                            print('已经在游戏界面')
                            break
                    time.sleep(5)
                    startcheckin()
                    return True
                elif menu is not None:
                    print('已经在游戏界面')
                    time.sleep(15)
                    startcheckin()
                    return True


def choosemode():
    hwnd = win32gui.FindWindow('DagorWClass', None)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
    win32gui.SetForegroundWindow(hwnd)
    print(hwnd)
    while True:
        a = locate('pic/join.png',0.8)
        time.sleep(1)
        if a is not None:
            x = a[0]
            y = a[1]+50
            b = (x,y)
            click(b)
            navy = locate('pic/luncher/navyrb.png',0.8)
            if navy is not None:
                click(navy)
                return
        elif a is None:
            return False
