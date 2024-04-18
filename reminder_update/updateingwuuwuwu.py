import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget
from PySide6.QtCore import QTimer, Qt
from PySide6 import QtGui


# define a class RestWindow, inherit from QMainWindow, to show the reminder window
class RestWindow(QMainWindow):
    def __init__(self, remind, selected_message):
        super().__init__()
        # set window title, size, position, font, etc.
        self.setWindowTitle("Rest Time!")
        self.resize(800, 500)
        self.move(250, 150)
        self.setFont(QtGui.QFont("font-size: 40px;font-weight: bold"))
        # set window topmost flag
        self.setWindowFlag(Qt.WindowStaysOnTopHint,True)
        # create a label rest_label, to show the user input reminder and selected message
        self.rest_label = QLabel(self)
        self.rest_label.setText(f"{remind}\n{selected_message}\n如果需要 请打开判断程序")
        self.rest_label.setAlignment(Qt.AlignCenter)
        self.rest_label.setStyleSheet("color: blue")

# define a class MainWindow, inherit from QMainWindow, to show the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window title, size, position, font, etc.
        self.setWindowTitle("reminder")
        self.resize(800, 500)
        self.move(250, 150)
        self.setFont(QtGui.QFont("font-size: 20px;font-weight: bold"))
        # create label and entry for inputting time
        self.time_label = QLabel(self)
        self.time_label.setText("Enter time in minutes:")
        self.time_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.entry = QLineEdit(self)
        self.entry.setStyleSheet("font-size: 20px;")
        # create label and entry for inputting remind
        self.remind_label = QLabel(self)
        self.remind_label.setText("Enter reminder:")
        self.remind_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.remind_entry = QLineEdit(self)
        self.remind_entry.setStyleSheet("font-size: 20px;")
        # create listbox
        self.message_choices = ["站起来稍微休息一下", "热身时间结束~ 请根据效果调整策略与目标~", "峰尾效应！！！以及减少狗剩！！！", " "]
        self.list_box = QListWidget(self)
        self.list_box.setStyleSheet("font-size: 20px;")
        for message in self.message_choices:
            self.list_box.addItem(message)
        # create button to start timer
        self.start_button = QPushButton(self)
        self.start_button.setText("Start Timer")
        self.start_button.setStyleSheet("font-size: 20px;")
        self.start_button.clicked.connect(self.start_timer)
        # create a layout layout, to arrange the widgets in the main window
        self.layout = QVBoxLayout()
        # add the widgets to the layout
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.remind_label)
        self.layout.addWidget(self.remind_entry)
        self.layout.addWidget(self.list_box)
        self.layout.addWidget(self.start_button)
    
        # create central widget and set layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        # set central widget for main window only once
        self.setCentralWidget(self.central_widget)


    def start_timer(self):
         # get the user input time, reminder and selected message
         selected_index = self.list_box.currentRow()
         selected_message = self.message_choices[selected_index]
         t_value = int(float(self.entry.text()) * 60) # convert minutes to seconds
         remind = self.remind_entry.text()
         
        # call threading.Timer function to execute show_rest_window function after the set time
         QTimer.singleShot(t_value * 1000, lambda: self.show_rest_window(remind, selected_message))
    # define a function show_rest_window, to create and show an instance of RestWindow class
    def show_rest_window(self,remind, selected_message):
        self.rest_window = RestWindow(remind, selected_message)
        self.rest_window.show()



# create an instance of QApplication class and pass sys.argv as argument
app = QApplication(sys.argv)

# create an instance of MainWindow class and show it
main_window = MainWindow()
main_window.show()

# enter the main loop and wait for user operation
sys.exit(app.exec())
