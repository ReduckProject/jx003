import os
from time import sleep

import pyautogui

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
    WindowsUtils.clickIcon('icon/map/maweiyi.png')
    WindowsUtils.clickIcon('icon/map/longmenhuangmo.png')

    # WindowsUtils.clickIcon('icon/maweiyi/changancheng2.png')
    # WindowsUtils.clickIcon('icon/maweiyi/maweiyi_shenxing2.png')
    # sleep(1)
    # print("find .. maweiyi_select")
    # WindowsUtils.clickIcon('icon/maweiyi/maweiyi_select.png')
    # sleep(1)
    # print("find .. maweiyi_shenxing_confirm")
    # WindowsUtils.clickIcon('icon/maweiyi/maweiyi_shenxing_confirm.png')
    # sleep(1)

