import os
import time
import win32gui

import key
from find import locate
from join import main_join
from running import main_run
from end import main_end
from utils import logger_log as log, active, click
from presskey import press



def main():
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
            forcejoin = locate('pic/join.png', 0.8)
            if forcejoin is not None:
                click(forcejoin)
                time.sleep(0.1)
                log("强制加入")
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

