import sys
import time
from ctypes import *

import win32com.client

import WindowsUtils


class WyKeybord():
    def __init__(self):
        global wyhkm
        wyhkm= WindowsUtils.wyhkm
        # # 进程内注册插件,模块所在的路径按照实际位置修改
        # hkmdll = windll.LoadLibrary("E:\\Code\\dnf-rich\\keybords\\wyhkm64.dll")
        # hkmdll.DllInstall.argtypes = (c_long, c_longlong)
        # if hkmdll.DllInstall(1, 2) < 0:
        #     print("注册失败!")
        #     sys.exit(0)
        #
        # # 创建对象
        # try:
        #     wyhkm = win32com.client.Dispatch("wyp.hkm")
        # except:
        #     print("创建对象失败!")
        #     sys.exit(0)
        #
        # # 获得模块版本号
        # version = wyhkm.GetVersion()
        # print("无涯键鼠盒子模块版本：" + hex(version))
        # DevId = wyhkm.SearchDevice(0x2612, 0x1701, 0)
        # if DevId == -1:
        #     print("未找到无涯键鼠盒子")
        #     sys.exit(0)
        # # 打开设备,DPI模式取每个显示器DPI感知
        # if not wyhkm.Open(DevId, 0):
        #     print("打开无涯键鼠盒子失败")
        #     sys.exit(0)
        # wyhkm.SetKeyInterval(10, 10)

    def press(self, key):
        print('pression key', key)
        wyhkm.KeyPress(key)
        time.sleep(0.2)

    def leftClick(self):
        wyhkm.LeftClick()

    def leftDoubleClick(self):
        wyhkm.LeftDoubleClick()

    def rightClick(self):
        wyhkm.RightClick()

    def rightDoubleClick(self):
        wyhkm.LeftDoubleClick()
