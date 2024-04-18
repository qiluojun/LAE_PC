from PySide6.QtWidgets import (
    QApplication, QDialog, QPushButton, QHBoxLayout, QMessageBox
)
import sys
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
 
    window = QDialog()
    window.resize(400, 300)
    #弹出窗口
    def show_msg():
        QMessageBox.information(window, "信息提示", "你点击了我")
 
    hbox = QHBoxLayout()
    button = QPushButton("点击我")
    button.clicked.connect(show_msg)
 
    hbox.addWidget(button)
    window.setLayout(hbox)
#展示窗口
    window.show()
 
    sys.exit(app.exec())
