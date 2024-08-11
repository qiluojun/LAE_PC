import pywinauto
import win32gui

# 在程序开始时初始化Application对象
app = pywinauto.Application()

def get_current_window(app_monitor):
    # 获取当前活动窗口的句柄

    try:
        # 连接到这个窗口
        handle = win32gui.GetForegroundWindow()
        app=app_monitor
        # 连接到这个窗口
        app.connect(handle=handle)

        window_name=app.top_window().window_text()
        return window_name

    except pywinauto.findwindows.ElementNotFoundError:
        return "无权限的系统应用", None