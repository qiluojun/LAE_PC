import sys
import re
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QTextEdit,QPushButton,QLabel,QLineEdit
from PySide6.QtCore import QRect,Qt
'''


'''

# 锁屏时呈现的内容：
## 从md中读取相应内容



'''
for i in range(1, 9):
    reminder = {}
    content_pattern = re.compile(r'{}4【(.*?)】'.format(i))
    content_match = content_pattern.search(text)

    if content_match:
        reminder['content'] = content_match.group(1)
    
    reminder['time_period']=i
    
    reminders['reminder{}'.format(i)] = reminder
'''



class LockScreenWindow(QtWidgets.QWidget):
    def __init__(self,locking_time,period_index1):
        super().__init__()
        self.nahh = 1
        self.timer = QtCore.QTimer(self)
        self.setWindowTitle("Lock Screen Timer")
        self.setFixedSize(800, 600)
        # 在这里加个 text broswer~ ！！！！
        self.plan_text = QTextEdit(self)
        self.plan_text.clear()
        self.reminders={}
        reminder0={'content':"空",'time_period':0}
        self.reminders['reminder0']=reminder0
        self.read_remineder(period_index1) 
        reminder=self.reminders['reminder{}'.format(period_index1)]
        self.plan_text.insertPlainText(reminder['content'])
        self.plan_text.setGeometry(QRect(600, 300, 400, 300))
        #更改提示语—-通过输入时段+点击按钮
        self.entry_label = QLabel("输入新的时段",self)
        self.entry_label.setGeometry(QRect(720, 650, 141, 16))
        self.new_period_entry = QLineEdit(self)
        self.new_period_entry.setGeometry(QRect(900, 650, 113, 20))
        self.change_reminder_button = QPushButton("更改提示语", self)
        self.change_reminder_button.setGeometry(QRect(720,700, 150, 50))
        self.change_reminder_button.clicked.connect(self.change_reminder)
        
        self.start_button = QPushButton("解锁！！", self)
        self.start_button.setGeometry(QRect(720, 600, 150, 50))
        self.start_button.clicked.connect(self.unlock_screen)
        self.start_button.setEnabled(False)
        
        self.setWindowFlag(Qt.WindowStaysOnTopHint,True)
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setStyleSheet("background-color: white;")
 
        
        
        
        
        # Install event filter
        QtWidgets.QApplication.instance().installEventFilter(self)
        
        # Create a new timer
        self.check_timer = QtCore.QTimer(self)
        # Connect timer to the check_window_state method
        self.check_timer.timeout.connect(self.check_window_state)

                       
        # time_minutes = float(time_str)
        self.timer.singleShot(int(locking_time * 60 * 1000),self.allow_unlock_screen) 
        #self.timer.singleShot(10*1000,self.unlock_screen)  # 10s后解锁
        #self.timer.timeout.connect(self.unlock_screen)
    
    def read_remineder(self,index):
        self.reminders={}
        with open(r'D:\学习and学校\obsidian\qiluo\00-MOC\reminders_base_on_timeline.md','r',encoding='utf-8') as f:
            lines = f.readlines()
            reminder_whole = []
            record = False
            i=0
            for line in lines:
                    reminder=''
                    title = '### ' + str(index)    
                    if line.startswith(title):
                        record = True
                        i=1
                    elif line.startswith('###'):
                        record = False
                        i=0
                    elif i==1:
                        if "+{" in line:
                            record = False
                        elif "}+" in line:
                            record = True
                        elif record:
                            reminder_whole.append(line)
                    reminder_whole1 = ''.join(reminder_whole)
                    reminder_lines= reminder_whole1.splitlines()
                    for reminder_line in reminder_lines:
                        reminder+=reminder_line+'\n'
                    the_reminder={}
                    the_reminder['time_period']= index
                    the_reminder['content']=reminder

                    self.reminders['reminder{}'.format(index)] = the_reminder

        reminder0={'content':"你在干什么！？？？你现在贼有可能正处于狗剩之后：\n现在不是用电脑的时间！!小心！",'time_period':0}
        self.reminders['reminder0']=reminder0
        
    
             

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.WindowDeactivate and self.isFullScreen() and self.nahh:
            # Start the check timer when the lock screen window loses focus
            self.check_timer.start(1000)
        elif event.type() == QtCore.QEvent.WindowActivate and self.isFullScreen():
            # Stop the check timer when the lock screen window regains focus
            self.check_timer.stop()
        return super().eventFilter(source, event)

    def check_window_state(self):
    # Bring the lock screen window back to the front
        if not self.isActiveWindow():
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("警告")
            msgBox.setText("你在干啥！？(╬▔皿▔)╯")
            msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            msgBox.exec()

    def allow_unlock_screen(self):
        self.start_button.setEnabled(True)    

    def unlock_screen(self):
        # Stop the check timer
        self.check_timer.stop()
        self.nahh = 0
        #self.setWindowState(QtCore.Qt.WindowNoState) 原来是取消窗口全屏状态
        self.close()
        self.setStyleSheet("")
    def change_reminder(self):
        try:
            new_index=int(self.new_period_entry.text())
            self.plan_text.clear()
            self.read_remineder(new_index)
            reminder=self.reminders['reminder{}'.format(new_index)]
            self.plan_text.insertPlainText(reminder['content'])
        except ValueError:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setWindowTitle("输入错误")
            msgBox.setText("请输入有效值")
            msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            msgBox.exec()


