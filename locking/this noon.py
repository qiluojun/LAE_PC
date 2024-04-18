import sys
from PySide6 import QtWidgets, QtCore 
from pynput.keyboard import Key, Controller, Listener
import threading
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
        self.setWindowTitle("Lock Screen Timer")
        self.keyboard = Controller()
        self.listener = None

        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.setStyleSheet("background-color: white;")

        self.start_button = QtWidgets.QPushButton("准备好迎接中午！", self)
        self.start_button.setStyleSheet("font-size: 30px;")  # Make the text in the button larger
        # Calculate the position of the button
        button_width = 300
        button_height = 90
        window_width = self.width()
        window_height = self.height()
        button_x = (window_width - button_width) // 2
        button_y = (window_height - button_height) // 2
        self.start_button.setGeometry(button_x, button_y, button_width, button_height)
        self.start_button.clicked.connect(self.unlock_screen)

        #self.time_input = QtWidgets.QLineEdit(self)
        #self.time_input.setGeometry(100, 100, 100, 30)
        #self.time_input.setPlaceholderText("Please enter time")

        
        

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
        # Start a new thread to listen to keyboard events
        self.listener = Listener(on_press=self.disable_keyboard)
        self.listener.start()

    def unlock_screen(self):
        self.setWindowState(QtCore.Qt.WindowNoState)
        self.setStyleSheet("")
        # Stop the keyboard listener when unlocking the screen
        if self.listener is not None:
            self.listener.stop()
    def disable_keyboard(self, key):
        # This function will be called whenever a key is pressed.
        # We will suppress all key presses by returning False.
        return False
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LockScreenWindow()
    window.show()
    try:
        sys.exit(app.exec())
    except Exception:
        # If an error occurs, make sure to stop the keyboard listener
        if window.listener is not None:
            window.listener.stop()
    finally:
        # Also stop the keyboard listener when the program is exiting
        if window.listener is not None:
            window.listener.stop()
