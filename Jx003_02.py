import ctypes
import time
from ctypes import wintypes

# 定义鼠标消息常量
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202

# 加载 User32.dll
# user32 = ctypes.WinDLL('user32', use_last_error=True)
user32 = ctypes.windll.user32

# 定义函数原型
user32.FindWindowW.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
user32.FindWindowW.restype = wintypes.HWND

user32.SendMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.SendMessageW.restype = wintypes.LPARAM

# 查找窗口句柄
hWnd = user32.FindWindowW(None, '剑网3 - 唯我独尊 @ 电信区(点月卡区)')

while (hWnd):
    time.sleep(1)
    if hWnd:
        print('33333')
        # 设置鼠标点击位置 (x, y)，这里假设点击位置为 (100, 100)
        x = 1178
        y = 958
        lParam = (y << 16) | x

        # 向窗口发送鼠标左键按下消息
        result_down = user32.PostMessageW(hWnd, WM_LBUTTONDOWN, 0, lParam)
        if result_down == 0:
            print(f'WM_LBUTTONDOWN failed with error: {ctypes.get_last_error()}')

        # 向窗口发送鼠标左键松开消息
        result_up = user32.PostMessageW(hWnd, WM_LBUTTONUP, 0, lParam)
        if result_up == 0:
            print(f'WM_LBUTTONUP failed with error: {ctypes.get_last_error()}')

        if result_down != 0 and result_up != 0:
            print('Mouse click message sent successfully')
    else:
        print('Window not found')
