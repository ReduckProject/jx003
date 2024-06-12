from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")

# 设置鼠标监听器
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
