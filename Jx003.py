import pyautogui
import win32api
import win32gui


# 获取目标窗口的句柄
def get_window_handle(window_title):
    return win32gui.FindWindow(None, window_title)


# 在指定窗口上执行鼠标点击
def click_in_window(window_handle, x, y):
    # 获取窗口的设备上下文句柄
    hwndDC = win32gui.GetWindowDC(window_handle)

    # 将鼠标位置转换为屏幕坐标
    screen_pos = win32gui.ClientToScreen(window_handle, (x, y))

    # 模拟鼠标点击
    win32api.SetCursorPos(screen_pos)
    pyautogui.click()

    # 释放设备上下文句柄
    win32gui.ReleaseDC(window_handle, hwndDC)

# 回调函数，用于每个窗口
def enum_windows_callback(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        window_title = win32gui.GetWindowText(hwnd)
        if window_title:
            results.append(window_title)

# 获取所有窗口标题
def get_all_window_titles():
    results = []
    win32gui.EnumWindows(enum_windows_callback, results)
    return results

# 打印所有窗口标题
# window_titles = get_all_window_titles()
# for title in window_titles:
#     print(title)

# 示例用法
window_title = "剑网3 - 唯我独尊 @ 电信区(点月卡区)"
x, y = 100, 100  # 窗口内的点击位置
window_handle = get_window_handle(window_title)
if window_handle:
    click_in_window(window_handle, x, y)
else:
    print("找不到指定的窗口")
