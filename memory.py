import time

import cv2
import win32gui
from PIL import ImageGrab
import numpy as np


def capture_screen_to_memory():
    # 使用ImageGrab模块截取屏幕
    screenshot = ImageGrab.grab()
    return screenshot


def isJx003():
    # 获取当前活动窗口句柄
    hwnd = win32gui.GetForegroundWindow()

    if hwnd != 0:
        # 获取窗口标题
        window_title = win32gui.GetWindowText(hwnd)
        return "剑网3" in window_title
    else:
        return False


def pil_to_cv2(image_pil):
    # 将PIL图像转换为OpenCV格式
    image_cv2 = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    return image_cv2


while (isJx003() == False):
    time.sleep(1)

# 例子：截取屏幕并通过cv2读取到内存中
screenshot_image = capture_screen_to_memory()

# 将PIL图像转换为OpenCV格式
screenshot_cv2 = pil_to_cv2(screenshot_image)
img = screenshot_cv2
template = cv2.imread('icon/group.png')
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
if max_val > 0.8:
    x, y = max_loc
    print(f"Found  at:", x, y)
else:
    print("Not found")

print('Show')
# 例子：显示使用cv2读取的图像
cv2.imshow('Screenshot', screenshot_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

exit(0)
