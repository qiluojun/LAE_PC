import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QTextEdit,QPushButton,QLabel,QLineEdit
from PySide6.QtCore import QRect,Qt


'''
可以用了 但是老有一个不影响使用的bug……why？

'''

class States():
    def __init__(self):
        self.locking_time=0
        self.locking_content=''
        self.lock=0
    def check_state(self):
            self.lock=1
            self.locking_time= 0.1
            self.locking_content='知乎！'
            self.locking= LockScreenWindow(self.locking_time,self.locking_content)
            self.locking.show()
            


class LockScreenWindow(QtWidgets.QWidget):
            def __init__(self,locking_time,locking_content):
                super().__init__()
                self.nahh = 1
                self.timer = QtCore.QTimer(self)
                self.setWindowTitle("Lock Screen Timer")
                self.setFixedSize(800, 600)
                # 在这里加个 text broswer~ ！！！！
                self.plan_text = QTextEdit(self)
                self.plan_text.clear()
                self.plan_text.insertPlainText(locking_content)
                self.plan_text.setGeometry(QRect(600, 300, 400, 300))
                
                self.start_button = QPushButton("解锁！！", self)
                self.start_button.setGeometry(QRect(720, 600, 150, 50))
                self.start_button.clicked.connect(self.unlock_screen)
                self.start_button.setEnabled(False)
                
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
                #print("???")
                self.start_button.setEnabled(True)    

            def unlock_screen(self):
                # Stop the check timer
                self.check_timer.stop()
                self.nahh = 0
                #self.setWindowState(QtCore.Qt.WindowNoState) 原来是取消窗口全屏状态
                self.close()
                self.setStyleSheet("")
  
    



    