import pywinauto
import win32gui
import time
from pynput import keyboard, mouse



# 初始化操作状态
operation_status = "无操作"

# 定义键盘监听事件
def on_keyboard_activity(key):
    global operation_status
    operation_status = "有操作"

# 定义鼠标监听事件
def on_mouse_activity(x, y, button, pressed):
    global operation_status
    operation_status = "有操作"

# 定义鼠标移动监听事件
def on_mouse_move(x, y):
    global operation_status
    operation_status = "有操作"

# 定义鼠标滚轮监听事件
def on_mouse_scroll(x, y, dx, dy):
    global operation_status
    operation_status = "有操作"



# 启动键盘监听
keyboard_listener = keyboard.Listener(on_press=on_keyboard_activity)
keyboard_listener.start()

# 启动鼠标监听
mouse_listener = mouse.Listener(on_click=on_mouse_activity,on_move=on_mouse_move, on_scroll=on_mouse_scroll)
mouse_listener.start()




i=0

while i<10:
    
    # 获取当前活动窗口的句柄
    handle = win32gui.GetForegroundWindow()

    # 连接到这个窗口
    app = pywinauto.Application().connect(handle=handle)




    # 打印窗口的标题和操作状态
    print(app.top_window().window_text(), operation_status)
    # 重置操作状态
    operation_status = "无操作"

    i+=1
    time.sleep(2) 