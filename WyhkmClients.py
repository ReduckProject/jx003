import sys
import time
from ctypes import *
import atexit

import win32com.client

import WindowsUtils


# 键盘鼠标程序
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


wyhkm = registerKeybord()

def cleanup():
    wyhkm.Close()
    print("程序即将关闭，执行清理操作")

atexit.register(cleanup)

def delayRnd(min, max):
    wyhkm.DelayRnd(min, max)

def press(key):
    print('pression key', key)
    wyhkm.KeyPress(key)
    time.sleep(0.2)

def backspace():
    press('Backspace')

def esc():
    press('Esc')


def tab():
    press('Tab')


def write(data):
    wyhkm.OutputString(data)
    time.sleep(0.2)


def leftClick():
    wyhkm.LeftClick()
    time.sleep(0.2)


def leftDoubleClick():
    wyhkm.LeftDoubleClick()
    time.sleep(0.2)


def rightClick():
    wyhkm.RightClick()
    time.sleep(0.2)


def rightDoubleClick():
    wyhkm.LeftDoubleClick()
    time.sleep(0.2)

def check():
    res = wyhkm.CheckPressedKeys(2)
    print('pressed', res)
