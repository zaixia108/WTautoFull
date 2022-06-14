import argparse
import os
import dearpygui.dearpygui as dpg
from concurrent.futures import ThreadPoolExecutor
import utils
import main
executor = ThreadPoolExecutor(max_workers=50)


def log(param):
    utils.logger_log(param)


def _run():
    executor.submit(main.main)
    return


def Run_WTAuto(sender):
    global flag_check
    flag_check = False
    executor.submit(_run)


def ShunDown_WTAuto(sender):
    global flag_check
    try:
        with open('pic/check/check.ini','w+') as shut:
            shut.truncate(0)
            shut.write('#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#\n#')
            shut.close()
    except:
        print('没有检查文件')
    flag_check = True
    try:
        os._exit(0)
    except:
        os._exit(0)


parser = argparse.ArgumentParser()
parser.add_argument('-g', type=str, default=None)
args = parser.parse_args()


dpg.create_context()
dpg.create_viewport(width=350, height=350, min_width=10, min_height=10, x_pos=1300, y_pos=50,
                    small_icon='pic/icon.ico', large_icon='pic/icon.ico',resizable=False)
dpg.set_viewport_decorated(True)
dpg.setup_dearpygui()

with dpg.font_registry():
    with dpg.font("STXINWEI.TTF", 16) as CNF:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)

with dpg.window(label="RunMain", id="main_window", pos=[0, 0], no_background=True,no_scrollbar=True,no_title_bar=True,no_resize=True):
    dpg.bind_font(CNF)
    dpg.add_button(label="开始", callback=Run_WTAuto, pos=[25, 200], width=120, height=50)
    dpg.add_button(label="结束", callback=ShunDown_WTAuto, pos=[190, 200], width=120, height=50)
    dpg.add_text("本程序完全免费开源", pos=(45, 150),color=(255,255,255))
dpg.set_primary_window("main_window", True)
dpg.set_viewport_title("WTAuto")
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()