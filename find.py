import cv2

import time

import pyautogui
import pygetwindow as gw
import sys
import win32api
import win32com.client
from ctypes import *
from PIL import ImageGrab
import numpy as np

import win32gui

from pynput import keyboard

# def on_press(key):
#     try:
#         if key == keyboard.Key.f10:
#             print("按下 F10 键，执行相应操作")
#             # 在这里添加你想要执行的代码
#     except AttributeError:
#         pass
#
# def on_release(key):
#     if key == keyboard.Key.esc:
#         # 按下 ESC 键退出程序
#         return False
#
# # 监听键盘事件
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
x_offset = 0
y_offset = 0

match_rate=0.8

def isJx003():
    # 获取当前活动窗口句柄
    hwnd = win32gui.GetForegroundWindow()

    if hwnd != 0:
        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        return "剑网3" in window_title
    else:
        return False


def findIcon(path):
    if (isJx003() == False):
        return -1, -1
    # screenshot("tmp.png")
    # img = cv2.imread('tmp.png')
    img = memoryScreen()
    template = cv2.imread(path)
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f'Match value {max_val}')
    print(f'Match value {min_val}')
    time.sleep(1)
    if max_val > match_rate:
        x, y = max_loc
        print(f"Found {path} at:", x, y)
        return x, y
    else:
        print("Not found")
        return -1, -1


def screenshot(path):
    hwnd = win32gui.GetForegroundWindow()
    # 获取窗口位置和大小
    rect = win32gui.GetWindowRect(hwnd)
    x, y, width, height = rect

    # 截图并保存
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(path)
    print(f"截图已保存至 '{path}'.")


def capture_screen_to_memory():
    # 使用ImageGrab模块截取屏幕
    screenshot = ImageGrab.grab()
    return screenshot


def pil_to_cv2(image_pil):
    # 将PIL图像转换为OpenCV格式
    image_cv2 = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    return image_cv2


def memoryScreen():
    return pil_to_cv2(capture_screen_to_memory())


def registerKeybord():
    # 进程内注册插件,模块所在的路径按照实际位置修改
    hkmdll = windll.LoadLibrary("E:\\Code\\dnf-rich\\keybords\\wyhkm64.dll")
    hkmdll.DllInstall.argtypes = (c_long, c_longlong)
    if hkmdll.DllInstall(1, 2) < 0:
        print("注册失败!")
        sys.exit(0)

    # 创建对象
    try:
        wyhkm = win32com.client.Dispatch("wyp.hkm")
    except:
        print("创建对象失败!")
        sys.exit(0)

    # 获得模块版本号
    version = wyhkm.GetVersion()
    print("无涯键鼠盒子模块版本：" + hex(version))
    DevId = wyhkm.SearchDevice(0x2612, 0x1701, 0)
    if DevId == -1:
        print("未找到无涯键鼠盒子")
        sys.exit(0)
    # 打开设备,DPI模式取每个显示器DPI感知
    if not wyhkm.Open(DevId, 0):
        print("打开无涯键鼠盒子失败")
        sys.exit(0)
    wyhkm.SetKeyInterval(10, 10)
    return wyhkm


def clickIcon(iconPath):
    x, y = findIcon(iconPath)
    if (x > 0):
        x=x+x_offset
        y=y+y_offset
        wyhkm.MoveTo(x, y)
        print(f'move to {x}, {y}')
        wyhkm.LeftClick()
        return
    else:
        print(f"Not found {iconPath}")
    time.sleep(1)
    return x >= 0

def clickIconRetry(iconPath, retry):
    if(retry <= 0):
        return False

    x, y = findIcon(iconPath)
    if (x > 0):
        x = x + x_offset
        y = y + y_offset
        wyhkm.MoveTo(x, y)
        print(f'move to {x}, {y}')
        wyhkm.LeftClick()
        return True
    else:
        print(f"Not found {iconPath}")
        time.sleep(0.5)

        clickIconRetry(iconPath,retry - 1)

def init_login():
    global x_offset, y_offset, match_rate
    x_offset = 5
    y_offset = 5
    match_rate = 0.3

def init_normal():
    global x_offset, y_offset, match_rate
    x_offset = 3
    y_offset = 3
    match_rate = 0.7

def existIcon(path):
    x,y=findIcon(path)
    time.sleep(0.5)
    return x > -1

def waitIcon(iconPath, retry):
    if(retry < 1):
        return False
    if(existIcon(iconPath)):
        return True
    else:
        waitIcon(iconPath, retry - 1)

while (isJx003() == False):
    print("Waiting...")
    time.sleep(1)

def press(key):
    print('pression key', key)
    wyhkm.KeyPress(key)
    time.sleep(0.2)

def login(username, password):
    init_login()
    time.sleep(2)
    clickIcon('icon/username_input_new.png')
    time.sleep(1.5)
    wyhkm.LeftDoubleClick()
    wyhkm.OutputString(username)
    time.sleep(1)
    wyhkm.KeyPress('Esc')

    time.sleep(1)
    clickIcon('icon/password_input_new.png')
    time.sleep(1)
    wyhkm.LeftDoubleClick()

    wyhkm.OutputString(password)
    time.sleep(1)
    init_normal()

    clickIconRetry('icon/login.png', 20)
    clickIconRetry('icon/enter_game.png', 100)
    wyhkm.KeyPress('Enter')

def logout():
    init_normal()
    while(existIcon('icon/return_login.png') == False):
        print('登出按钮不存在')
        press('Esc')

    while(existIcon('icon/confirm.png') == False):
        clickIcon('icon/return_login.png')
    clickIconRetry('icon/confirm.png', 10)

def imIn():
    init_normal()
    while (existIcon('icon/return_login.png') == False):
        press('Esc')
    press('Esc')
    clickIconRetry('icon/im_in_icon_new.png',10)
    clickIconRetry('icon/im_in_new.png', 20)

def autoRegister(username, password):
    time.sleep(2)
    login(username, password)
    time.sleep(5)
    imIn()
    time.sleep(2)
    logout()
    time.sleep(3)
wyhkm = registerKeybord()

# clickIcon('icon/locked_icon.png')
# time.sleep(1)
# clickIcon('icon/group.png')
# time.sleep(1)
# clickIcon('icon/locked_icon.png')
# time.sleep(1)
# clickIcon('icon/unlocked_icon.png')
# time.sleep(1)
# clickIcon('icon/unlock.png')
# time.sleep(1)
# clickIcon('icon/transmit.png')
# time.sleep(1)
# clickIcon('icon/group.png')
# time.sleep(1.2)
# clickIcon('icon/transmit_group.png')
# print('Esc')
# wyhkm.KeyPress('Esc')
# print('click')
# clickIcon('icon/return_login.png')
# time.sleep(1)
# clickIcon('icon/confirm.png')05n@123ä923
# time.sleep(1)
# init_login()
# clickIcon('icon/username_input.png')
# # time.sleep(5)
# # wyhkm.KeyPress('Tab')
# time.sleep(2)
# wyhkm.LeftDoubleClick()
#
# wyhkm.OutputString("cannogcc")
# time.sleep(2)
# wyhkm.KeyPress('Esc')
# time.sleep(2)
# clickIcon('icon/password_input_new.png')
# time.sleep(1)
# # wyhkm.KeyPress('Esc')
# # wyhkm.KeyPress('Tab')
# time.sleep(2)
# wyhkm.LeftDoubleClick()
#
# wyhkm.OutputString("Admin@123")
# time.sleep(2)
#
# init_normal()
# clickIcon('icon/login.png')
# time.sleep(5)
# # clickIcon('icon/enter_game.png')
# wyhkm.KeyPress('Enter')
# time.sleep(20)
# time.sleep(5)
# while(existIcon('icon/return_game.png') == False):
#     wyhkm.KeyPress('Esc')
#     time.sleep(2)
#     if(existIcon('icon/return_game.png')):
#         wyhkm.KeyPress('Esc')
#         break
# time.sleep(2)
# match_rate=0.4
# if(existIcon('icon/return_game.png')):
#     wyhkm.KeyPress('Esc')
# clickIcon('icon/im_in_icon_new.png')
# time.sleep(3)
# clickIcon('icon/im_in.png')
autoRegister('cannogcc', 'Admin@123')
autoRegister('ginsco', 'Admin@123')
autoRegister('ginsco03', 'Admin@123')
autoRegister('qianchenyuanwei', 'Admin@123')
autoRegister('lixuansu', 'Admin@123')
exit(0)

