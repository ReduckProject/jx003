import win32gui
import win32con
import pyautogui
import time

def find_window_by_title_substring(substring):
    def callback(hwnd, substring):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if substring.lower() in window_title.lower():
                windows.append((hwnd, window_title))

    windows = []
    win32gui.EnumWindows(callback, substring)
    return windows

def capture_window_screenshot(hwnd, output_filename):
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

# 例子：模糊查找包含 "记事本" 的窗口并截图
result = find_window_by_title_substring("剑网")

if result:
    for hwnd, title in result:
        output_filename = f"{title.replace(' ', '_')}_screenshot.png"
        capture_window_screenshot(hwnd, output_filename)
else:
    print("未找到匹配的窗口。")