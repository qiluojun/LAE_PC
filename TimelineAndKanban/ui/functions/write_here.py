from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMessageBox
from PySide6.QtCore import Qt, QTimer
import pyperclip
import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.button = QPushButton('打印', self)
        self.button.clicked.connect(self.copy_text)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def copy_text(self):
        pyperclip.copy('哈哈哈哈')
        self.show_message()

    def show_message(self):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("已复制到剪切板")
        msgBox.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(500, msgBox.accept)  # 2 seconds
        msgBox.exec()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()