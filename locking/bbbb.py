import sys
from PySide6 import QtWidgets, QtCore 

'''
抓手：
1. 搞清楚 unlock_screen是怎么搞的 
2. singleshot 这一语句 多长时间检查一次？ 能不能改久一点？
未来：   锁屏 改为 必须要在规定区域做规定的事情 并且禁止其他区域的输入  
如果不以时间 而是以其他为条件解锁……就不用那么麻烦了哈哈哈哈


'''


class LockScreenWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer(self)
        self.setWindowTitle("Lock Screen Timer")
        self.setFixedSize(300, 200)

        self.start_button = QtWidgets.QPushButton("Start", self)
        self.start_button.setGeometry(100, 50, 100, 30)
        self.start_button.clicked.connect(self.lock_screen)

        self.time_input = QtWidgets.QLineEdit(self)
        self.time_input.setGeometry(100, 100, 100, 30)
        self.time_input.setPlaceholderText("Please enter time")
        # Install event filter
        QtWidgets.QApplication.instance().installEventFilter(self)
        
        # Create a new timer
        self.check_timer = QtCore.QTimer(self)
        # Connect timer to the check_window_state method
        self.check_timer.timeout.connect(self.check_window_state)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.WindowDeactivate and self.isFullScreen():
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
            msgBox.setText("你在干什么！？")
            msgBox.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
            msgBox.exec()

    '''def start_timer(self):
        time_str = self.time_input.text()
        try:
            time_minutes = float(time_str)
            self.timer.singleShot(int(time_minutes * 60 * 1000), self.lock_screen)  # Lock screen for the specified time
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid time.")
    '''
    def lock_screen(self):
        time_str = self.time_input.text() 
        try:               
            time_minutes = float(time_str)
            self.timer.singleShot(int(time_minutes * 60 * 1000),self.unlock_screen)  
            #self.timer.timeout.connect(self.unlock_screen)
            self.setWindowState(QtCore.Qt.WindowFullScreen)
            self.setStyleSheet("background-color: white;")
            
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid time.")


    def unlock_screen(self):
        # Stop the check timer
        self.check_timer.stop()
        
        self.setWindowState(QtCore.Qt.WindowNoState)
        self.setStyleSheet("")
        return super().unlock_screen()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LockScreenWindow()
    window.show()
    sys.exit(app.exec())