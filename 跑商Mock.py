import os
from time import sleep

import pyautogui

import WindowsMockUtils
import WindowsUtils

# 移动鼠标到指定位置，例如 (100, 200)
# pyautogui.moveTo(100, 200)
#
# # 点击鼠标左键
# pyautogui.click()


def check_image_path(image_path):
    if not os.path.exists(image_path):
        print(f"文件路径不存在: {image_path}")
        return False
    else:
        print(f"文件路径存在: {image_path}")
        return True

while True:
    WindowsMockUtils.clickIcon('icon/map/maweiyi.png')
    WindowsMockUtils.clickIcon('icon/map/longmenhuangmo.png')
    sleep(2)

