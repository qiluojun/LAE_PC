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
from pynput import keyboard
import pyperclip




class Ui_new_activity(object):  # from reminder_finalversion.py

    def __init__(self,NewActivityWindow):
        # 主界面初始化-- 左右分半
        self.current_activity= Activity(name="")
        self.centralwidget = QWidget(NewActivityWindow)
        self.layout=QHBoxLayout(self.centralwidget)
        # Create a layout for the frame
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout,1)
        self.layout.addLayout(self.right_layout,2)
           
        # 创建界面
        NewActivityWindow.setObjectName(" NewActivityWindow")
        # NewActivityWindow.resize(1440, 773)
        NewActivityWindow.resize(1000, 600)
        self.centralwidget.setObjectName("centralwidget")
        NewActivityWindow.setCentralWidget(self.centralwidget)
		# 设置窗口始终在顶部
        NewActivityWindow.setWindowFlags(NewActivityWindow.windowFlags() | Qt.WindowStaysOnTopHint)
		
		# 设置左半边：
        # 创建控件 
        
        self.content_search_bar = QLineEdit(self.centralwidget)
        self.content_yes_button = QPushButton("内容确定", self.centralwidget)
        self.content_table_view = QTableView(self.centralwidget)
        
        self.type_search_bar = QLineEdit(self.centralwidget)
        self.type_yes_button = QPushButton("类型确定", self.centralwidget)
        self.type_table_view = QTableView(self.centralwidget)
        
        
        

        
        
        
        
        
        # 安排位置
        content_search_layout= QHBoxLayout()
        content_search_layout.addWidget(self.content_search_bar,1)
        content_search_layout.addWidget(self.content_yes_button,2)
        type_search_layout=QHBoxLayout()
        type_search_layout.addWidget(self.type_search_bar,1)
        type_search_layout.addWidget(self.type_yes_button,2)
        # 塞控件进layout  并且排列控件和layout
        self.left_layout.addLayout(content_search_layout)
        self.left_layout.addWidget(self.content_table_view)
        self.left_layout.addLayout(type_search_layout)
        self.left_layout.addWidget(self.type_table_view)
        
        # 设置右半边
        # 创建控件 
        
        self.activity_alreadyModify_list = QListWidget(self.centralwidget)
        self.delete_chosen_button = QPushButton("删除选中", self.centralwidget)
        self.start_now_button = QPushButton("立即开始活动", self.centralwidget)
        self.add_activity_button = QPushButton("添加活动", self.centralwidget)
        
        self.md_chosen_text_show = QTextEdit()
        self.activity_attribute_list = QListWidget(self.centralwidget)
        self.add_into_activity_button = QPushButton("添加", self.centralwidget)
        

        
        
        

        # 安排位置
        three_buttons_layout=QHBoxLayout()
        add_attribute_layout=QHBoxLayout()
        att_list_and_add_button_layout=QVBoxLayout()
        
        three_buttons_layout.addWidget(self.delete_chosen_button)
        three_buttons_layout.addWidget(self.start_now_button)
        three_buttons_layout.addWidget(self.add_activity_button)
        att_list_and_add_button_layout.addWidget(self.activity_attribute_list)
        att_list_and_add_button_layout.addWidget(self.add_into_activity_button)
        add_attribute_layout.addWidget(self.md_chosen_text_show)
        add_attribute_layout.addLayout(att_list_and_add_button_layout)
        self.right_layout.addWidget(self.activity_alreadyModify_list)
        self.right_layout.addLayout(three_buttons_layout)
        self.right_layout.addLayout(add_attribute_layout)
        
 
        
        self.retranslateUi( NewActivityWindow)
        QMetaObject.connectSlotsByName( NewActivityWindow)

    def on_text_copied(self, text):
        self.md_chosen_text_show.setText(text)
    def setupUi(self,db):
           
        #连接 table view 和 数据表
        # 创建数据库连接
        
        self.db = db
        self.db.open()

        # 创建模型并链接到表
        self.model_content = QSqlTableModel()
        self.model_content.setTable('活动内容_简')
        self.model_content.select()

        self.model_type = QSqlTableModel()
        self.model_type.setTable('活动类型')
        self.model_type.select()

        # 将模型设置为QTableView的模型
        self.content_table_view.setModel(self.model_content)
        self.type_table_view.setModel(self.model_type)
        self.content_table_view.setSortingEnabled(True)
        self.type_table_view.setSortingEnabled(True)
        
        self.content_table_view.clicked.connect(self.on_content_table_view_clicked)
        self.content_yes_button.clicked.connect(self.on_content_yes_button_clicked)
        self.content_search_bar.textChanged.connect(self.on_content_search_bar_text_changed)

        self.type_table_view.clicked.connect(self.on_type_table_view_clicked)
        self.type_yes_button.clicked.connect(self.on_type_yes_button_clicked)
        self.type_search_bar.textChanged.connect(self.on_type_search_bar_text_changed)

        self.content_table_view.doubleClicked.connect(self.on_content_yes_button_clicked)
        self.type_table_view.doubleClicked.connect(self.on_type_yes_button_clicked)


        # 处理 list（右下的活动属性列表）
        self.activity_attributes = ["活动名称", "目标完成日",  "目标时长", "进度描述", "抓手"]
        # 将属性列表的内容添加到activity_attribute_list中
        self.activity_attribute_list.addItems(self.activity_attributes)
        self.activity_attribute_list.itemDoubleClicked.connect(self.on_add_into_activity_button_clicked)
        # 连接add_into_activity_button的点击事件
        self.add_into_activity_button.clicked.connect(self.on_add_into_activity_button_clicked)
        
        # 处理 md中选中内容显示到text_show中
        # 创建MyListener实例
        self.listener = MyListener()
        self.listener.text_copied.connect(self.on_text_copied)
        # 在新的线程中启动监听器
        self.listener.start()
        
        # 连接删除按钮
        self.delete_chosen_button.clicked.connect(self.on_delete_chosen_button_clicked) 
        # list双击同样可删除~
        self.activity_alreadyModify_list.itemDoubleClicked.connect(self.on_delete_chosen_button_clicked)
        # 连接 添加活动 按钮 
        self.add_activity_button.clicked.connect(self.activity_generate)
        self.add_activity_button.clicked.connect(lambda: write_activity_in_md(self.current_activity))
        
        self.add_activity_button.clicked.connect(lambda: write_activity_in_db(self.current_activity))
        

    def activity_generate(self):
        self.current_activity.timestamp=self.current_activity.generate_timestamp()
        
    def on_content_table_view_clicked(self, index):
        self.selected_index = index.row()
    def on_content_yes_button_clicked(self):
        # 获取选中行的记录
        record = self.model_content.record(self.selected_index)
        # 获取name列的值
        name = record.value("name")
        # 将name列的值赋给self.current_activity.name
        self.current_activity.content_location = name
        # 添加新的列表项
        self.activity_alreadyModify_list.addItem(f"内容location：{name}")
    def on_content_search_bar_text_changed(self, text):
        # Filter the model based on the search bar's text
        self.model_content.setFilter(f"name LIKE '%{text}%'")
        self.model_content.select()

    
    def on_type_table_view_clicked(self, index):
        self.selected_index = index.row()
    def on_type_yes_button_clicked(self):
        # 获取选中行的记录
        record = self.model_type.record(self.selected_index)
        # 获取name列的值
        name = record.value("name")
        # 将name列的值赋给self.current_activity.name
        self.current_activity.type_location = name
        # 添加新的列表项
        self.activity_alreadyModify_list.addItem(f"类型location：{name}")        
        
        
        
        
    def on_type_search_bar_text_changed(self, text):
        # Filter the model based on the search bar's text
        self.model_type.setFilter(f"name LIKE '%{text}%'")
        self.model_type.select()

    def on_add_into_activity_button_clicked(self):
        # 获取选中的属性名
        selected_attribute = self.activity_attribute_list.currentItem().text()
        # 获取self.md_chosen_text_show的文本
        text = self.md_chosen_text_show.toPlainText()
        # 如果你想打印出对应的属性值，你可以使用一个字典来映射属性名和属性值
        '''attribute_value_mapping = {
            "内容location": self.current_activity.content_location,
            "类型location":self.current_activity.type_location,
            "活动名称": self.current_activity.name,
            "目标完成日": self.current_activity.target_completion_date,
            "目标时长": self.current_activity.target_duration,
            "进度描述": self.current_activity.progress_description,
            "抓手": self.current_activity.handle
            }'''
        attribute_name_mapping = {
            "内容location": "content_location",
            "类型location": "type_location",
            "活动名称": "name",
            "目标完成日": "target_completion_date",
            "目标时长": "target_duration",
            "进度描述": "progress_description",
            "抓手": "handle"
        }
        setattr(self.current_activity, attribute_name_mapping[selected_attribute], text)        
        # 添加新的列表项
        self.activity_alreadyModify_list.addItem(f"{selected_attribute}：{text}")
       



    '''def on_delete_chosen_button_clicked(self):
        # 获取选中的列表项
        selected_item = self.activity_alreadyModify_list.currentItem()
        if selected_item is not None:
            # 从列表中删除选中的列表项
            row = self.activity_alreadyModify_list.row(selected_item)
            self.activity_alreadyModify_list.takeItem(row)
            # 清空对应的活动属性
            attribute_name = selected_item.text().split("：")[0]
            attribute_value_mapping = {
                "内容location": self.current_activity.content_location,
                "类型location":self.current_activity.type_location,
                "活动名称": self.current_activity.name,
                "目标完成日": self.current_activity.target_completion_date,
                "目标时长": self.current_activity.target_duration,
                "进度描述": self.current_activity.progress_description,
                "抓手": self.current_activity.handle
            }
            attribute_value_mapping[attribute_name] = ""  '''
    def on_delete_chosen_button_clicked(self):
        # 获取选中的列表项
        selected_item = self.activity_alreadyModify_list.currentItem()
        if selected_item is not None:
            # 从列表中删除选中的列表项
            row = self.activity_alreadyModify_list.row(selected_item)
            self.activity_alreadyModify_list.takeItem(row)
            # 清空对应的活动属性
            attribute_name = selected_item.text().split("：")[0]
            attribute_name_mapping = {
                "内容location": "content_location",
                "类型location": "type_location",
                "活动名称": "name",
                "目标完成日": "target_completion_date",
                "目标时长": "target_duration",
                "进度描述": "progress_description",
                "抓手": "handle"
            }
            setattr(self.current_activity, attribute_name_mapping[attribute_name], "")


    def reset_current_activity(self):
        self.current_activity=Activity(name=" ")


    def retranslateUi(self,  NewActivityWindow):
        _translate = QApplication.translate
        # 窗口名称
        NewActivityWindow.setWindowTitle(_translate("添加新活动", "TimeLineV2"))


 
if __name__ == "__main__":
    
    activity = Activity(name="跑步", target_completion_date="2022-12-31", content_location="14-ada", 
                    type_location="户外", activity_status={"status": "进行中", "times_performed": 1}, 
                    target_duration=30, progress_description="已完成一半", 
                    handle="这是一段描述\n有多行的\n抓手") 

    activity_record = ActivityRecord(activity, start_time="20221105100000", end_time="20221105103000", 
                                    actual_duration=30, actual_content="跑了5公里", evaluation="感觉很好")

    
    #write_activity_in_md(activity)
    
    
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("D:\\学习and学校\\搞事情\\LAE\\TimelineAndKanban\\activity.db")

    app = QApplication(sys.argv)
    NewActivityWindow = QMainWindow()
    ui = Ui_new_activity(NewActivityWindow)
    ui.setupUi(db)
    NewActivityWindow.show()
    sys.exit(app.exec())
    
    
    


    
    


# 进度 左半边窗口 功能搞定~
