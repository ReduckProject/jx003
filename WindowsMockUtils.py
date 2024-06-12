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

def matchWindows(title):
    # 获取当前活动窗口句柄
    hwnd = win32gui.GetForegroundWindow()

    if hwnd != 0:
        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        return title in window_title
    else:
        return False

def printCurrenntWindowsTitle():
    # 获取当前活动窗口句柄
    hwnd = win32gui.GetForegroundWindow()

    if hwnd != 0:
        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        print('Current Window Title: ' + window_title)
    else:
        print('Not found current windows title')

def findIcon(path):
    if (isJx003() == False):
        return -1, -1
    # screenshot("tmp.png")
    # img = cv2.imread('tmp.png')
    img = memoryScreen()
    # template = cv2.imread(path)
    template = imread_unicode(path)
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

# 解决中文路径找不到的问题
def imread_unicode(path):
    # 使用 numpy 从文件中读取字节数据
    stream = open(path, "rb")
    bytes_data = bytearray(stream.read())
    numpy_array = np.asarray(bytes_data, dtype=np.uint8)
    # 使用 cv2.imdecode 读取 numpy 数组中的图像数据
    image = cv2.imdecode(numpy_array, cv2.IMREAD_COLOR)
    return image

def isJx003():
    # 获取当前活动窗口句柄
    hwnd = win32gui.GetForegroundWindow()

    if hwnd != 0:
        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        return "剑网3" in window_title
    else:
        return False

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

def clickIcon(iconPath):
    x, y = findIcon(iconPath)
    if (x > 0):
        x=x+x_offset
        y=y+y_offset
        pyautogui.moveTo(x, y)
        print(f'move to {x}, {y}')
        pyautogui.click()
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
        pyautogui.moveTo(x, y)
        print(f'move to {x}, {y}')
        pyautogui.click()
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
