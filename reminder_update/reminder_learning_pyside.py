import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit, QListWidget
from PySide6.QtCore import QTimer

def show_rest_window(remind, selected_message):
    rest_window = QMainWindow()
    rest_window.setWindowTitle("Rest Time!")
    rest_label = QLabel(f"{remind}\n{selected_message}\n如果需要 请打开判断程序")
    rest_label.setStyleSheet("font-size: 40px; font-weight: bold; color: blue;")
    rest_window.setCentralWidget(rest_label)
    rest_window.show()

def start_timer():
    selected_index = list_box.currentRow()
    selected_message = message_choices[selected_index]
    t_value = int(float(entry.text()) * 60) # convert minutes to seconds
    remind = remind_entry.text()
    QTimer.singleShot(t_value * 1000, lambda: show_rest_window(remind, selected_message))

app = QApplication(sys.argv)

# create main window
main_window = QMainWindow()
main_window.setWindowTitle("reminder")
main_window.setGeometry(250, 150, 800, 500)

# create label and entry for inputting time
time_label = QLabel("Enter time in minutes:")
time_label.setStyleSheet("font-size: 20px; font-weight: bold;")
entry = QLineEdit()
entry.setStyleSheet("font-size: 20px;")
time_layout = QVBoxLayout()
time_layout.addWidget(time_label)
time_layout.addWidget(entry)
time_widget = QWidget()
time_widget.setLayout(time_layout)
main_window.setCentralWidget(time_widget)

# create label and entry for inputting remind
remind_label = QLabel("Enter reminder:")
remind_label.setStyleSheet("font-size: 20px; font-weight: bold;")
remind_entry = QLineEdit()
remind_entry.setStyleSheet("font-size: 20px;")
remind_layout = QVBoxLayout()
remind_layout.addWidget(remind_label)
remind_layout.addWidget(remind_entry)
remind_widget = QWidget()
remind_widget.setLayout(remind_layout)
main_window.setCentralWidget(remind_widget)

# create listbox
message_choices = ["站起来稍微休息一下", "热身时间结束~ 请根据效果调整策略与目标~", "峰尾效应！！！以及减少狗剩！！！"," "]
list_box = QListWidget()
list_box.setStyleSheet("font-size: 20px;")
for message in message_choices:
    list_box.addItem(message)
list_box.setFixedHeight(200)

# create button to start timer
start_button = QPushButton("Start Timer")
start_button.setStyleSheet("font-size: 20px;")
start_button.clicked.connect(start_timer)

# create layout for main window
layout = QVBoxLayout()
layout.addWidget(time_widget)
layout.addWidget(remind_widget)
layout.addWidget(list_box)
layout.addWidget(start_button)

# create central widget and set layout
central_widget = QWidget()
central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)

main_window.show()
sys.exit(app.exec())