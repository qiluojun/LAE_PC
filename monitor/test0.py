import pygetwindow
import pyautogui
import time
import tkinter as tk

def get_clipboard():
    root = tk.Tk()
    root.withdraw()
    return root.clipboard_get()

while True:
    # 检查Edge浏览器是否正在运行
    edge_windows = [w for w in pygetwindow.getAllWindows() if 'Edge' in w.title and w.visible]
    if edge_windows:
        # 如果Edge浏览器正在运行，检查当前网址是否为指定网址
        edge_window = edge_windows[0]
        edge_window.activate()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'l')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        url = get_clipboard()
        if 'www.zhihu.com' in url:
            # 如果当前网址为指定网址，弹出提醒窗口
            pyautogui.alert('小心哦！')
    time.sleep(5)
