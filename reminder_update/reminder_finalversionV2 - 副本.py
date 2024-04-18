import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer, Qt,QRect,QMetaObject,QDateTime
from PySide6.QtGui import *





# define a class RestWindow, inherit from QMainWindow, to show the reminder window
class RestWindow(QMainWindow):
    def __init__(self, remind, selected_message):
        super().__init__()
        # set window title, size, position, font, etc.
        self.setWindowTitle("Rest Time!")
        self.resize(800, 500)
        self.move(250, 150)
        self.setFont(QFont("font-size: 60px;font-weight: bold"))
        # set window topmost flag
        self.setWindowFlag(Qt.WindowStaysOnTopHint,True)
        #layout = QVBoxLayout(self)
        
        # create a central widget and set it as the main widget for the window
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # create a vertical layout
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignCenter)
        
        # create a label rest_label, to show the user input reminder and selected message
        self.rest_label = QLabel(self)
        self.rest_label.setText(f"{remind}\n{selected_message}")
        self.rest_label.setAlignment(Qt.AlignCenter)
        self.rest_label.setStyleSheet("color: black")
        self.rest_label.setStyleSheet("font-size: 30px")
        #self.rest_label.setFont(QFont("font-size: 60px"))  # Set the font size to 24
        
        layout.addWidget(self.rest_label)
    # Add a timer to delay the close button
        self.close_enabled = False
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.enable_close)
        self.timer.start(8000)  # 5 seconds
        
    def enable_close(self):
        self.close_enabled = True

    def closeEvent(self, event):
        if self.close_enabled:
            event.accept()
        else:
            event.ignore()
       

       
	

class Ui_MainWindow(object):
	def __init__(self):
		# 主界面初始化
		self.centralwidget = QWidget(MainWindow)
		# 添加监控开关
		self.monitor_button = QPushButton("Monitor: OFF")
		self.monitor_button.setCheckable(True)
		self.monitor_button.clicked.connect(self.toggle_monitor)
		
		# 添加监控定时器
		self.monitor_timer = QTimer()
		self.monitor_timer.setInterval(60000)  # 1 minute
		self.monitor_timer.timeout.connect(self.check_reminder)

	def setupUi(self, MainWindow):
		# 创建界面
		MainWindow.setObjectName("MainWindow")
		#MainWindow.resize(1440, 773)
		MainWindow.resize(700, 600)
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)
		
		
		# 设置主界面面板：
		
		self.layout = QVBoxLayout(self.centralwidget)
		self.time_label = QLabel()
		self.time_label.setText("请输入时间：(单位为分钟)")
		self.time_label.setStyleSheet("font-size: 20px; font-weight: bold;")
		self.entry = QLineEdit()
		self.entry.setStyleSheet("font-size: 20px;")
		# create label and entry for inputting remind
		self.remind_label = QLabel()
		self.remind_label.setText("Enter reminder:")
		self.remind_label.setStyleSheet("font-size: 20px; font-weight: bold;")
		self.remind_entry = QLineEdit()
		self.remind_entry.setStyleSheet("font-size: 20px;")
		
		self.reminders_list = QTextEdit()
		self.reminders_list.insertPlainText(" ")
		self.reminders_list.setStyleSheet("font-size: 20px;")
		self.reminders_list.setReadOnly(True)
  
  
  
  		# create listbox
		
		# 这里待功能优化！
		self.message_choices=[""]
		with open(r"D:\学习and学校\搞事情\LAE\reminder_update\reminder_content.txt", "r",encoding='utf-8') as file:
			for line in file:
				self.message_choices.append(line.strip())
    
		self.list_box = QListWidget()
		self.list_box.setStyleSheet("font-size: 20px;")
		window_size = self.layout.sizeHint() # get the recommended size of the window
		self.list_box.setMaximumHeight(window_size.height() * 10) # set the maximum width to one third of the window width

		for message in self.message_choices:
			self.list_box.addItem(message)
		# create button to start timer
		self.start_button = QPushButton()
		self.start_button.setText("Start Timer")
		self.start_button.setStyleSheet("font-size: 20px;")
		self.start_button.clicked.connect(self.start_timer)
		# create a layout layout, to arrange the widgets in the main window
		time_layout= QHBoxLayout()
		time_layout.addWidget(self.time_label,1)
		time_layout.addWidget(self.entry,2)
		remind_layout = QHBoxLayout()
		remind_layout.addWidget(self.remind_label, 1)
		remind_layout.addWidget(self.remind_entry, 2)
		self.layout.addLayout(time_layout)
		self.layout.addLayout(remind_layout)
		self.layout.addWidget(self.list_box)
		self.layout.addWidget(self.reminders_list)
		self.layout.addWidget(self.start_button)
  
  
		self.layout.addWidget(self.monitor_button)
  		
		self.retranslateUi(MainWindow)
		QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QApplication.translate
		# 窗口名称
		MainWindow.setWindowTitle(_translate("MainWindow", "定时休息提醒"))
		
		

	
  
	def start_timer(self):
		# get the user input time, reminder and selected message
		selected_index = self.list_box.currentRow()
		selected_message = self.message_choices[selected_index]
		if self.entry.text():
			t_value = int(float(self.entry.text()) * 60) # convert minutes to seconds
			remind = self.remind_entry.text()

			# call threading.Timer function to execute show_rest_window function after the set time
			QTimer.singleShot(t_value * 1000, lambda: self.show_rest_window(remind, selected_message))

			global reminders,reminders_num
			reminders_num +=1
			# Calculate the time when QTimer will be triggered
			current_time = QDateTime.currentDateTime()
			trigger_time = current_time.addSecs(t_value)

			reminders[reminders_num] = trigger_time.toString("hh:mm:ss")
			self.show_reminders()
		else:
			QMessageBox.warning(self.centralwidget,"错误", "请按格式输入正确的时间")
			
  		#print(reminders)
	def show_reminders(self):
		self.reminders_list.clear()
		for key,value in reminders.items():
			if key<= reminders_num:
				line = f"第{key}个提醒将于{value}弹出\n"	
				self.reminders_list.insertPlainText(line)
            
    # define a function show_rest_window, to create and show an instance of RestWindow class
	def show_rest_window(self,remind, selected_message):
		self.rest_window = RestWindow(remind, selected_message)
		self.rest_window.show()
		global reminders_num,reminders
		for i in range(1,reminders_num):
			reminders[i]=reminders[i+1]
		reminders_num -=1
		self.show_reminders()
  

	def toggle_monitor(self, checked):
		if checked:
			self.monitor_button.setText("Monitor: ON")
			self.monitor_timer.start()
		else:
			self.monitor_button.setText("Monitor: OFF")
			self.monitor_timer.stop()

	def check_reminder(self):
		global reminders
		if not reminders:
			self.show_rest_window("请设定reminder", "")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyleSheet("QPushButton { background-color: #4d90fe; border-radius: 10px; }")
	reminders={}
	reminders_num=0
	MainWindow = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec())
