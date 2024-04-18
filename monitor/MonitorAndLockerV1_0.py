'''
功能设想：
1. 2130 之后 用知乎 B站  直接强制锁屏 1min以上 
2. 平时检测到 弹窗提醒？（这个力度可以吗？）


'''
from pywinauto import Desktop
import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer,Qt


import time

from locker import States 

windows = Desktop(backend="uia").windows()
current_names = set(w.window_text() for w in windows if w.window_text().strip())





def check_app():
    windows = Desktop(backend="uia").windows()
    current_names = set(w.window_text() for w in windows if w.window_text().strip())
    print(type(current_names))
    current_time = time.strftime("%H%M")
    contains_zhihu = False
    for name in current_names:
        if "知乎" in name:
            contains_zhihu = True
            break


    if current_time >= '1500' :
        if contains_zhihu:
            app.state.check_state()
        
app = QApplication(sys.argv) 
       
check_app_timer = QTimer()
check_app_timer.timeout.connect(check_app)
check_app_timer.start(60 * 1000)  # QTimer uses milliseconds


app.state=States()


check_app()




app.exec()