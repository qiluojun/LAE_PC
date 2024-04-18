'''
此处存放mainwindow的ui 

进度：
好耶！可以用了！就是大小啥的有点丑 后续调一下~

'''
from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

class Ui_MainWindow(object):  # from reminder_finalversion.py
    '''def __init__(self):  bug2 如果有 init 函数 timeline那边就无法正常运行 不知道为啥呜呜
        # 主界面初始化-- 左右分半
        self.centralwidget = QWidget(MainWindow)
        self.layout=QHBoxLayout(self.centralwidget)
        # Create a layout for the frame
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout,1)
        self.layout.addLayout(self.right_layout,2)
    

		# 界面布局---太丑了 建议更改！
'''
    def setupUi(self, MainWindow):
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
        #MainWindow.resize(1440, 773)
        MainWindow.resize(1400, 800)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
		
		
		# 设置左半边：
        # 创建控件 
        self.current_period_name_label = QLabel()
        self.plan_text = QTextEdit()
        self.show_plan_button = QPushButton("show/refresh plan")
        self.basic_state_record_button = QPushButton("记录基本状态")
        self.start_new_period_button = QPushButton("开启新时段")
        self.end_current_period_button = QPushButton("结束当前时段")
        self.close_button = QPushButton("close")
        self.lock_button = QPushButton("lock now")
        # 安排位置
        plan_state_layout= QHBoxLayout()
        plan_state_layout.addWidget(self.show_plan_button,1)
        plan_state_layout.addWidget(self.basic_state_record_button,2)
        period_layout=QHBoxLayout()
        period_layout.addWidget(self.start_new_period_button,1)
        period_layout.addWidget(self.end_current_period_button,2)
        close_lock_layout=QHBoxLayout()
        close_lock_layout.addWidget(self.close_button,1)
        close_lock_layout.addWidget(self.lock_button,2)
        # 塞控件进layout  并且排列控件和layout
        self.left_layout.addWidget(self.current_period_name_label)
        self.left_layout.addWidget(self.plan_text)
        self.left_layout.addLayout(plan_state_layout)
        self.left_layout.addLayout(period_layout)
        self.left_layout.addLayout(close_lock_layout)
        
        # 设置右半边
        # 创建控件 
        self.search_bar = QLineEdit()
        self.view_activity = QTableView()
        self.select_activity_button = QPushButton("选择活动")
        self.current_activity_name_label = QLabel()
        self.activity_lenth = QLabel()
        self.start_activity_button = QPushButton("开始活动")
        self.pause_activty = QPushButton("暂停活动")
        self.end_activty = QPushButton("结束活动")
        # 安排位置
        search_select_layout=QHBoxLayout()
        search_select_layout.addWidget(self.search_bar,1)
        search_select_layout.addWidget(self.select_activity_button,2)
        start_pause_end_layout=QHBoxLayout()
        start_pause_end_layout.addWidget(self.start_activity_button,1)
        start_pause_end_layout.addWidget(self.pause_activty,2)
        start_pause_end_layout.addWidget(self.end_activty,3)
        # 塞控件进layout 并且排列控件和layout
        self.right_layout.addLayout(search_select_layout)
        self.right_layout.addWidget(self.view_activity)
        self.right_layout.addWidget(self.current_activity_name_label)
        self.right_layout.addWidget(self.activity_lenth)
        self.right_layout.addLayout(start_pause_end_layout)
        
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.search_activity() # 调用搜索活动板块的功能
        

    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        # 窗口名称
        MainWindow.setWindowTitle(_translate("MainWindow", "TimeLineV2"))


    def search_activity(self):  #搜索活动板块
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('D:\\学习and学校\\搞事情\\LAE\\TimeLine2\\file_paths.db')
        self.db.open()
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable('Files')
        if self.model.select():
            self.view_activity.setModel(self.model)
            self.view_activity.setColumnHidden(2,True)  #啊啊啊为啥隐藏不了555
        else:
            print("Error: ", self.model.lastError().text())
        self.view_activity.clicked.connect(self.on_view_activity_clicked)
        self.select_activity_button.clicked.connect(self.on_select_activity_button_clicked)
        self.search_bar.textChanged.connect(self.on_search_bar_text_changed)

    def on_view_activity_clicked(self, index):
        # 此处获得选中的内容
        self.selected_name = self.model.record(index.row()).value("name")   
    def on_select_activity_button_clicked(self):
        print(self.selected_name)
    def on_search_bar_text_changed(self, text):
        # Filter the model based on the search bar's text
        self.model.setFilter(f"name LIKE '%{text}%'")
        self.model.select()
    def just_test(self):
        print("asdasfa")
            
'''
运行测试用 测完删掉！
'''
'''
import sys
#create mainwindow：
class MyWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.lock_window = None  # Initialize lock_window
        self.ui = Ui_MainWindow()
 # 初始化界面
        self.ui.setupUi(self)


# 启动窗口
app = QApplication(sys.argv)


MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
'''