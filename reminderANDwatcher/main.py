import time
from datetime import datetime
import sys
from typing import Optional
from PySide6.QtCore import QTimer,Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QAction
import subprocess
import PySide6.QtWidgets

import schedule  
import action
import app_rc # 由pyside6-rcc生成的资源文件




from mainwindow_ui import Ui_MainWindow
from goal_allocation_expectation import write_goals_to_db,read_goals_from_file,write_expectations_to_db,read_expectations_from_file
import condition_checker_ui
import read_current_window




filepath = "C:\\Users\\qiluo\\Desktop\\LAE!!!.txt"  # Update this to the correct path
goals = read_goals_from_file(filepath)
write_goals_to_db(goals)
expectations = read_expectations_from_file(filepath)
write_expectations_to_db(expectations)

app = QApplication(sys.argv)

night_questionaire_check = None
activity='none'

waiting_minutes= 0
    





def get_current_status():
    global night_questionaire_check
    global activity
    
    # 简化为直接返回当前时间和示例活动
    current_time = datetime.now().strftime('%H:%M')
    activity = read_current_window.get_current_window()
    
    status = {'current_time': current_time, 'activity': activity}
    rules_violated = schedule.check_status(status)
    
    main_window.condition_checker_window.waiting_minutes
    
    #action.remind_judge(rules_violated)
    #print("??")
    if current_time >= '22:20'and not night_questionaire_check:
        subprocess.run(["cmd.exe", "/c", "D:\\学习and学校\\搞事情\\LAE\\GraduateProject\\ui_and_basic\\questionnaire_in_use.bat"], shell=True)
        night_questionaire_check = True


    if main_window.condition_checker_window.waiting_minutes:
        # 每次调用减去5秒（0.0833分钟）
        main_window.condition_checker_window.waiting_minutes -= 0.08
    
    #print("waiting_minutes:",main_window.condition_checker_window.waiting_minutes)
    
    
    # 如果waiting_minutes大于0，则不继续执行后续逻辑
    if main_window.condition_checker_window.waiting_minutes <= 0:
        main_window.condition_checker_window.waiting_minutes= 0
        if '02' in rules_violated  :
            main_window.stopTimer()
            
            main_window.condition_checker_window.show()
            
            
            
    
    
    
        










class MySysTrayWidget(QWidget):
    def __init__(self, ui=None, app=None, window=None):
        QWidget.__init__(self)  # 必须调用，否则信号系统无法启用

        # 私有变量
        self.__ui = ui
        self.__app = app
        self.__window = window
        #self.__ui.setupUi(self.__window)
        #self.__ui.setupUi(self)
        
        
        # 配置系统托盘
        self.__trayicon = QSystemTrayIcon(self)
        self.__trayicon.setIcon(QIcon(':/app_icon.png'))
        self.__trayicon.setToolTip('reminderANDwatcher')  #为啥这里显示不出来？

        # 创建托盘的右键菜单
        self.__traymenu = QMenu()
        self.__trayaction = []
        self.addTrayMenuAction('显示主界面', self.show_userinterface)
        self.addTrayMenuAction('退出', self.quit)

        # 配置菜单并显示托盘
        self.__trayicon.setContextMenu(self.__traymenu) #把tpMenu设定为托盘的右键菜单
        self.__trayicon.show()  #显示托盘   

        # 连接信号
        #self.__ui.pushButton.clicked.connect(self.hide_userinterface)

        # 默认隐藏界面
        #self.hide_userinterface()

    def __del__(self):
        pass

    def addTrayMenuAction(self, text='empty', callback=None):
        a = QAction(text, self)
        a.triggered.connect(callback)
        self.__traymenu.addAction(a)
        self.__trayaction.append(a)

    def quit(self):
        # 真正的退出
        self.__app.exit()

    def show_userinterface(self):
        self.__window.show()

    def hide_userinterface(self):
        self.__window.hide()








class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi()
        self.setupTimer()
    
    def setupTimer(self):
        ''' 创建一个计时器'''
        self.timer = QTimer(self)
        # 设置计时器超时回调函数
        self.timer.timeout.connect(get_current_status)
        # 设置计时器间隔时间（毫秒）
        self.timer.start(5000)  # 60秒
    
    def startTimer(self):
        '''重新启动计时器'''
        if not self.timer.isActive():
            self.timer.start(5000)
    
    def stopTimer(self):
        '''停止计时器'''
        if self.timer.isActive():
            self.timer.stop()
    
    
    def closeEvent(self, event):
        # 忽略退出事件，而是隐藏到托盘
        event.ignore()
        self.hide()

        
main_window = MyWindow()
tray = MySysTrayWidget(app=app, window=main_window, ui=main_window.ui)




main_window.condition_checker_window=condition_checker_ui.Conditioner(main_window)

    






main_window.show()
sys.exit(app.exec())
















