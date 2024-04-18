from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import sys
from pynput import keyboard
import pyperclip

from functions.Class_activityAndRecord import Activity, ActivityRecord



class Ui_start_new_activity(object):  # from reminder_finalversion.py

    def __init__(self,StartNewActivityWindow):

        # 主界面初始化-- 左右分半
        self.current_activity= Activity(name="")
        self.centralwidget = QWidget(StartNewActivityWindow)
        self.layout=QHBoxLayout(self.centralwidget)
        # Create a layout for the frame
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout,2)
        self.layout.addLayout(self.right_layout,1)

        # 创建界面
        StartNewActivityWindow.setObjectName("StartNewActivityWindow")
        StartNewActivityWindow.resize(1000, 600)
        self.centralwidget.setObjectName("centralwidget")
        StartNewActivityWindow.setCentralWidget(self.centralwidget)
        

        # 设置左半边：
        # 创建控件 

        self.activity_search_bar = QLineEdit(self.centralwidget)
        self.activity_table_view = QTableView(self.centralwidget)

        # 安排位置
        activity_search_layout= QVBoxLayout()
        activity_search_layout.addWidget(self.activity_search_bar)
        activity_search_layout.addWidget(self.activity_table_view)
        # 塞控件进layout  并且排列控件和layout
        self.left_layout.addLayout(activity_search_layout)

        # 设置右半边
        # 创建控件 

        self.start_chosen_activity_button = QPushButton("开始选中活动", self.centralwidget)
        self.add_new_activity_button = QPushButton("添加新活动再开始", self.centralwidget)

        # 安排位置
        activity_buttons_layout= QVBoxLayout()
        activity_buttons_layout.addWidget(self.start_chosen_activity_button)
        activity_buttons_layout.addWidget(self.add_new_activity_button)
        self.right_layout.addLayout(activity_buttons_layout)

        self.retranslateUi(StartNewActivityWindow)
        QMetaObject.connectSlotsByName(StartNewActivityWindow)

   
    def setupUi(self,db):
            
        #连接 table view 和 数据表
        # 创建数据库连接
        self.db = db
        
        if not self.db.open():
            print("无法打开数据库")

        # 创建模型并链接到表
        self.model = QSqlTableModel()
        self.model.setTable('activity')
        self.model.setFilter("activity_status != '已完结'")
        self.model.select()

        # 将模型设置为QTableView的模型
        self.activity_table_view.setModel(self.model)
        self.activity_table_view.setSortingEnabled(True)
        
        self.activity_table_view.clicked.connect(self.on_activity_table_view_clicked)
        self.start_chosen_activity_button.clicked.connect(self.on_start_chosen_activity_button_clicked)
        self.activity_search_bar.textChanged.connect(self.on_activity_search_bar_text_changed)
        
        self.activity_table_view.doubleClicked.connect(self.on_start_chosen_activity_button_clicked)
       

    def on_activity_search_bar_text_changed(self, text):
        # Filter the model based on the search bar's text
        self.model.setFilter(f"name LIKE '%{text}%'")
        self.model.select()

    def on_activity_table_view_clicked(self, index):
        self.selected_index = index.row()
    
    def on_start_chosen_activity_button_clicked(self):
        # 获取选中行的记录
        record = self.model.record(self.selected_index)
        # 获取name列的值
        self.current_activity.timestamp = record.value("timestamp")
        self.show_message_and_copy_handle()
    
        

    def retranslateUi(self,  StartNewActivityWindow):
        _translate = QApplication.translate
        # 窗口名称
        StartNewActivityWindow.setWindowTitle(_translate("开启活动", "TimeLineV2"))

    
    def show_message_and_copy_handle(self):
        if self.current_activity.handle:
            pyperclip.copy(self.current_activity.handle)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("已成功将抓手复制至剪切板")
        msgBox.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(500, msgBox.accept)  # 0.5 seconds
        msgBox.exec()
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    StartNewActivityWindow = QMainWindow()
    ui = Ui_start_new_activity(StartNewActivityWindow)
    ui.setupUi()
    StartNewActivityWindow.show()
    sys.exit(app.exec())

