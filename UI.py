import argparse
import os
import dearpygui.dearpygui as dpg
from autologin import endoff
from concurrent.futures import ThreadPoolExecutor
import utils
import main
executor = ThreadPoolExecutor(max_workers=50)


def runsteam():#运行steam版本
    st = os.path.exists('pic/config/gaijin.d')
    if st is True:
        os.remove('pic/config/gaijin.d')
    open('pic/config/steam.d','w+')
    with dpg.window(label="切换成功",pos=(60,80),modal=True,tag='steam',no_title_bar=True,no_resize=True,no_move=True):
        dpg.add_text("已成功切换至启动steam客户端\n请点击开始以开始挂机",)
        dpg.add_button(label='确定',pos=(90,70),callback=lambda :dpg.delete_item(item='steam'))
    log('已经切换到steam版')
    return


def runGaijin():#运行gaijin版本
    gj = os.path.exists('pic/config/steam.d')
    if gj is True:
        os.remove('pic/config/steam.d')
    open('pic/config/gaijin.d','w+')
    with dpg.window(label="切换成功",pos=(60,80),modal=True,tag='Gaijin',no_title_bar=True,no_resize=True,no_move=True):
        dpg.add_text("已成功切换至启动Gaijin客户端\n请点击开始以开始挂机")
        dpg.add_button(label='确定',pos=(90,70),callback=lambda :dpg.delete_item(item='Gaijin'))
    log('已经切换到Gaijin版')
    return


def choosecountry():
    with dpg.window(label='选择国家', modal=True, tag="modal_id",pos=(40, 40),no_resize=True,no_move=True,no_scrollbar=True,no_title_bar=True):
        dpg.add_text('请选择国家')
        dpg.add_button(label='美国',callback=utils.us)
        dpg.add_button(label='德国', callback=utils.ger)
        dpg.add_button(label='苏联', callback=utils.ussr)
        dpg.add_button(label='英国', callback=utils.uk)
        dpg.add_button(label='日本', callback=utils.jp)
        dpg.add_button(label='意大利', callback=utils.it)
        # dpg.add_button(label='确定', pos=(120, 160), tag='确定',callback=lambda: dpg.delete_item(item='modal_id'))


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
        endoff()
        os._exit(0)
    except:
        os._exit(0)


parser = argparse.ArgumentParser()
parser.add_argument('-g', type=str, default=None)
args = parser.parse_args()


dpg.create_context()
dpg.create_viewport(width=350, height=529, min_width=10, min_height=10, x_pos=1300, y_pos=50,
                    small_icon='pic/icon.ico', large_icon='pic/icon.ico',resizable=False)
dpg.set_viewport_decorated(True)
dpg.setup_dearpygui()
width, height, channels, data = dpg.load_image("pic/bg.jpg")
with dpg.texture_registry(show=False):
    dpg.add_static_texture(width, height, data, tag="texture_tag")


with dpg.font_registry():
    with dpg.font("STXINWEI.TTF", 16) as CNF:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)

with dpg.window(label="RunMain", id="main_window", pos=[0, 0], no_background=True,no_scrollbar=True,no_title_bar=True,no_resize=True):
    dpg.bind_font(CNF)
    dpg.add_image("texture_tag")
    dpg.add_button(label="开始", callback=Run_WTAuto, pos=[25, 410], width=120, height=50)
    dpg.add_button(label="结束", callback=ShunDown_WTAuto, pos=[190, 410], width=120, height=50)
    # dpg.add_button(label="全自动配置", callback=autorunconfig, pos=[25, 340], width=120, height=25)
    dpg.add_button(label="国家", callback=choosecountry, pos=[25, 375], width=285, height=25)
    dpg.add_button(label="切换steam启动", callback=runsteam, pos=[25, 340], width=120, height=25)
    dpg.add_button(label="切换Gaijin启动", callback=runGaijin, pos=[190, 340], width=120, height=25)
    dpg.add_text("如果你是steam版请点击切换Steam启动\n如果你是Gaijin版请点击切换Gaijin启动\n也可以打开游戏后在点击开始\n ", pos=(45, 150),color=(0,0,0))
dpg.set_primary_window("main_window", True)
dpg.set_viewport_title("WTAuto")
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()