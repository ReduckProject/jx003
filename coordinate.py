import pyautogui
import time
import win32gui
import win32con


def capture_window_screenshot(window_title, output_filename):
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(None, window_title)

    if hwnd == 0:
        print(f"窗口 '{window_title}' 未找到。")
        return

    # 将窗口激活到前台
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)  # 等待窗口响应

    # 获取窗口位置和大小
    rect = win32gui.GetWindowRect(hwnd)
    x, y, width, height = rect

    # 截图并保存
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(output_filename)
    print(f"截图已保存至 '{output_filename}'.")


def find_window_by_title_substring(substring):
    def callback(hwnd, substring):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if substring.lower() in window_title.lower():
                windows.append((hwnd, window_title))

    windows = []
    win32gui.EnumWindows(callback, substring)
    return windows


# 例子：模糊查找包含 "记事本" 的窗口
result = find_window_by_title_substring("剑网3")

if result:
    for hwnd, title in result:
        print(f"窗口标题: {title}, 句柄: {hwnd}")
else:
    print("未找到匹配的窗口。")



# 例子：获取记事本窗口并保存截图
capture_window_screenshot("无标题 - 记事本", "notepad_screenshot.png")
exit(0)