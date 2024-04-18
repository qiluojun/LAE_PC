from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import sys



class Ui_MainWindow(object):  # from reminder_finalversion.py

    def __init__(self,MainWindow):
        # 主界面初始化-- 左右分半
        
        
        self.centralwidget = QWidget(MainWindow)
        self.layout=QHBoxLayout(self.centralwidget)
        # Create a layout for the frame
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout,1)
        self.layout.addLayout(self.right_layout,2)
           
        # 创建界面
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1440, 773)
        MainWindow.resize(1000, 600)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
		
	
		# 设置左半边： 没想好干啥 先占个空
        # 创建控件 
        

        self.ZhanKong_table_view = QTableView(self.centralwidget)
 
        # 安排位置

        self.left_layout.addWidget(self.ZhanKong_table_view)

        
        # 设置右半边
        # 创建控件 
        
        # 创建控件
        self.current_time_period_label = QLabel("当前时段为", self.centralwidget)
        self.start_new_period_button = QPushButton("开启新时段", self.centralwidget)
        self.end_period_button = QPushButton("结束时段", self.centralwidget)

        self.current_activity_label = QLabel("当前进行的活动为：", self.centralwidget)
        self.timer_label = QLabel("00:00:00", self.centralwidget)
        self.continuous_timer_label = QLabel("00:00:00", self.centralwidget)

        self.start_restart_button = QPushButton("start/restart", self.centralwidget)
        self.pause_button = QPushButton("pause", self.centralwidget)

        self.start_activity_button = QPushButton("开启活动", self.centralwidget)
        self.end_activity_button = QPushButton("结束活动", self.centralwidget)

        self.state_record_button = QPushButton("state record", self.centralwidget)
        self.close_window_button = QPushButton("close window", self.centralwidget)
        self.activity_record_record_button =QPushButton("record record", self.centralwidget)
        # 安排位置
        first_layout = QHBoxLayout()
        second_layout = QHBoxLayout()
        third_layout = QHBoxLayout()
        fourth_layout = QHBoxLayout()
        fifth_layout = QHBoxLayout()

        first_layout.addWidget(self.current_time_period_label)
        first_layout.addWidget(self.start_new_period_button)
        first_layout.addWidget(self.end_period_button)

        second_layout.addWidget(self.current_activity_label)
        second_layout.addWidget(self.timer_label)
        second_layout.addWidget(self.continuous_timer_label)

        third_layout.addWidget(self.start_restart_button)
        third_layout.addWidget(self.pause_button)

        fourth_layout.addWidget(self.start_activity_button)
        fourth_layout.addWidget(self.end_activity_button)

        fifth_layout.addWidget(self.state_record_button)
        fifth_layout.addWidget(self.activity_record_record_button)
        fifth_layout.addWidget(self.close_window_button)

        self.right_layout.addLayout(first_layout)
        self.right_layout.addLayout(second_layout)
        self.right_layout.addLayout(third_layout)
        self.right_layout.addLayout(fourth_layout)
        self.right_layout.addLayout(fifth_layout)
        
       
        self.retranslateUi( MainWindow)
        QMetaObject.connectSlotsByName( MainWindow)

    
    def setupUi(self):
            
        pass
    
    
    

    def retranslateUi(self,  MainWindow):
        _translate = QApplication.translate
        # 窗口名称
        MainWindow.setWindowTitle(_translate("TimeLine主窗口", "TimeLineV2"))


 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec())


# 进度 左半边窗口 功能搞定~
