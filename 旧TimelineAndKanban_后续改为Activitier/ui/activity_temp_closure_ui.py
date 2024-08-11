from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import sqlite3
import sys
from pynput import keyboard
import pyperclip
from datetime import datetime, timedelta


from functions.Class_activityAndRecord import Activity, ActivityRecord
from functions.circle_choose import MyListener
from functions.use_timestamp_read_activity import get_activity
from functions.write_in_md_and_db import (
    write_activity_in_db,write_activity_in_md,find_path,write_activity_record_in_db,
    write_activity_record_in_md, update_activity_in_db,update_activity_in_md,move_activity_to_the_end)


# 焯 实际时长计算用的函数！ 唉 格式惹的祸啊！
def str_to_timedelta(time_str):
    h, m, s = map(int, time_str.split(':'))
    return timedelta(hours=h, minutes=m, seconds=s)

def timedelta_to_str(time_delta):
    total_seconds = int(time_delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"



class Ui_activity_temp_closure_activity(object):  # from reminder_finalversion.py

    def __init__(self,Activity_Temp_Closure_Window):
        #变量初始化
        self.current_activity=Activity(name=' ')
        self.current_activity_record= ActivityRecord(self.current_activity)
        
        # 主界面初始化-- 左中右分三部分
        self.centralwidget = QWidget(Activity_Temp_Closure_Window)
        self.layout=QHBoxLayout(self.centralwidget)
        # Create a layout for the frame
        self.left_layout = QVBoxLayout()
        self.middle_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout,2)
        self.layout.addLayout(self.middle_layout,1)
        self.layout.addLayout(self.right_layout,3)
           
        # 创建界面
        Activity_Temp_Closure_Window.setObjectName(" Activity_Temp_Closure_Window")
        Activity_Temp_Closure_Window.resize(1000, 600)
        self.centralwidget.setObjectName("centralwidget")
        Activity_Temp_Closure_Window.setCentralWidget(self.centralwidget)
        # 设置窗口始终在顶部
        Activity_Temp_Closure_Window.setWindowFlags(Activity_Temp_Closure_Window.windowFlags() | Qt.WindowStaysOnTopHint)
        
        # 设置左边：
        # 创建控件 
        self.md_chosen_text_show = QTextEdit(self.centralwidget)
        self.activity_attribute_list = QListWidget(self.centralwidget)
        
        # 安排位置
        self.left_layout.addWidget(self.md_chosen_text_show,1)
        self.left_layout.addWidget(self.activity_attribute_list,3)
        
        # 设置中间：
        # 创建控件 
        self.modify_activity_attribute_button = QPushButton("修改活动属性", self.centralwidget)
        self.modify_activity_record_attribute_button = QPushButton("修改活动记录属性", self.centralwidget)
        self.generate_activity_record_button = QPushButton("生成暂时活动记录", self.centralwidget)
        self.generate_activity_record_final_button =QPushButton("生成完结活动记录", self.centralwidget)
        
        # 安排位置
        self.middle_layout.addWidget(self.modify_activity_attribute_button)
        self.middle_layout.addWidget(self.modify_activity_record_attribute_button)
        self.middle_layout.addWidget(self.generate_activity_record_button)
        self.middle_layout.addWidget(self.generate_activity_record_final_button)
        # 设置右边：
        # 创建控件 
        self.activity_record_attribute_list = QListWidget(self.centralwidget)
        
        # 安排位置
        self.right_layout.addWidget(self.activity_record_attribute_list)
        
        self.retranslateUi(Activity_Temp_Closure_Window)
        QMetaObject.connectSlotsByName(Activity_Temp_Closure_Window)
    def on_text_copied(self, text):
        self.md_chosen_text_show.setText(text)
    
    def setupUi(self):
        print("setup!")
        # 清空列表
        self.activity_attribute_list.clear()
        self.activity_record_attribute_list.clear()
        
        # 活动record 属性 名称 值 的映射
        self.activity_record_attribute_value_mapping ={
            "进行时段": self.current_activity_record.time_period,
            "开始时间": self.current_activity_record.actual_duration['start_time'],
            "结束时间": self.current_activity_record.actual_duration['end_time'],
            "实际时长": self.current_activity_record.actual_duration['duration'],
            "实际内容": self.current_activity_record.actual_content,
            "评价/备注": self.current_activity_record.evaluation
        }
        
        self.activity_attribute_value_mapping = {
            "内容location": self.current_activity.content_location,
            "类型location":self.current_activity.type_location,
            "活动名称": self.current_activity.name,
            "目标完成日": self.current_activity.target_completion_date,
            "目标时长": self.current_activity.target_duration,
            "进度描述": self.current_activity.progress_description,
            "抓手": self.current_activity.handle
        }
        
        self.activity_record_attribute_name_mapping = {
            "进行时段": "time_period",
            "开始时间": "start_time",
            "结束时间": "end_time",
            "实际时长": "duration",
            "实际内容": "actual_content",
            "评价/备注": "evaluation"
        }
        
        self.activity_attribute_name_mapping = {
                "内容location": "content_location",
                "类型location": "type_location",
                "活动名称": "name",
                "目标完成日": "target_completion_date",
                "目标时长": "target_duration",
                "进度描述": "progress_description",
                "抓手": "handle"
            }
        
        
        
        
        # md_chosen_text_show 呈现它的内容 
     
        for name, value in self.activity_attribute_value_mapping.items():
            
            self.activity_attribute_list.addItem(f"{name}：{value}")
    

        # activity_record_attribute_list 呈现它的内容
        
        for name, value in self.activity_record_attribute_value_mapping.items():
            self.activity_record_attribute_list.addItem(f"{name}：{value}")
    
        # 处理 md中选中内容显示到text_show中
        # 创建MyListener实例
        self.listener = MyListener()
        self.listener.text_copied.connect(self.on_text_copied)
        # 在新的线程中启动监听器
        self.listener.start()
        
        # 连接 modify_activity_attribute_button 的点击事件
        self.modify_activity_attribute_button.clicked.connect(self.on_modify_activity_attribute_button_clicked)
        # 连接 modify_activity_record_attribute_button 的点击事件
        self.modify_activity_record_attribute_button.clicked.connect(self.on_modify_activity_record_attribute_button_clicked)
        # 连接 activity_attribute_list 的双击事件 （代替按钮）
        self.activity_attribute_list.itemDoubleClicked.connect(self.on_modify_activity_attribute_button_clicked)
        # 连接 activity_record_attribute_list 的双击事件（代替按钮）
        self.activity_record_attribute_list.itemDoubleClicked.connect(self.on_modify_activity_record_attribute_button_clicked)
        #  连接 generate_activity_record_button 的功能 
        self.generate_activity_record_button.clicked.connect(self.on_generate_activity_record_button_clicked)
        
        self.generate_activity_record_final_button.clicked.connect(self.on_generate_activity_record_final_button_clicked)
    
    def resetUi(self):
        # 清空列表
        self.activity_attribute_list.clear()
        self.activity_record_attribute_list.clear()
        
        # 活动record 属性 名称 值 的映射
        self.activity_record_attribute_value_mapping ={
            "进行时段": self.current_activity_record.time_period,
            "开始时间": self.current_activity_record.actual_duration['start_time'],
            "结束时间": self.current_activity_record.actual_duration['end_time'],
            "实际时长": self.current_activity_record.actual_duration['duration'],
            "实际内容": self.current_activity_record.actual_content,
            "评价/备注": self.current_activity_record.evaluation
        }
        
        self.activity_attribute_value_mapping = {
            "内容location": self.current_activity.content_location,
            "类型location":self.current_activity.type_location,
            "活动名称": self.current_activity.name,
            "目标完成日": self.current_activity.target_completion_date,
            "目标时长": self.current_activity.target_duration,
            "进度描述": self.current_activity.progress_description,
            "抓手": self.current_activity.handle
        }
        
        self.activity_record_attribute_name_mapping = {
            "进行时段": "time_period",
            "开始时间": "start_time",
            "结束时间": "end_time",
            "实际时长": "duration",
            "实际内容": "actual_content",
            "评价/备注": "evaluation"
        }
        
        self.activity_attribute_name_mapping = {
                "内容location": "content_location",
                "类型location": "type_location",
                "活动名称": "name",
                "目标完成日": "target_completion_date",
                "目标时长": "target_duration",
                "进度描述": "progress_description",
                "抓手": "handle"
            }
        
        
        
        
        # md_chosen_text_show 呈现它的内容 
     
        for name, value in self.activity_attribute_value_mapping.items():
            
            self.activity_attribute_list.addItem(f"{name}：{value}")
    

        # activity_record_attribute_list 呈现它的内容
        
        for name, value in self.activity_record_attribute_value_mapping.items():
            self.activity_record_attribute_list.addItem(f"{name}：{value}")        
    
    
    def retranslateUi(self,  Activity_Temp_Closure_Window):
        _translate = QApplication.translate
        # 窗口名称
        Activity_Temp_Closure_Window.setWindowTitle(_translate("暂时结算", "TimeLineV2"))

    # 更新 activity_attribute_list 中的项
    def on_modify_activity_attribute_button_clicked(self):
            # 获取选中的属性名
            selected_attribute = self.activity_attribute_list.currentItem().text().split("：")[0]
            # 获取 self.md_chosen_text_show 的文本
            text = self.md_chosen_text_show.toPlainText()
            # 更新属性值
            
            setattr(self.current_activity, self.activity_attribute_name_mapping[selected_attribute], text)
            
            for i in range(self.activity_attribute_list.count()):
                if self.activity_attribute_list.item(i).text().startswith(selected_attribute):
                    self.activity_attribute_list.item(i).setText(f"{selected_attribute}：{text}")
                    break
    # 更新 activity_record_attribute_list 中的项
    def on_modify_activity_record_attribute_button_clicked(self):
        # 获取选中的属性名
        selected_attribute = self.activity_record_attribute_list.currentItem().text().split("：")[0]
        # 获取 self.md_chosen_text_show 的文本
        text = self.md_chosen_text_show.toPlainText()
        
        # 更新属性值
        if selected_attribute in ["开始时间", "结束时间","实际时长"]:
            self.current_activity_record.actual_duration[self.activity_record_attribute_name_mapping[selected_attribute]] = text
        else:
            setattr(self.current_activity_record, self.activity_record_attribute_name_mapping[selected_attribute], text)
        
        for i in range(self.activity_record_attribute_list.count()):
            if self.activity_record_attribute_list.item(i).text().startswith(selected_attribute):
                self.activity_record_attribute_list.item(i).setText(f"{selected_attribute}：{text}")
                break
    
    def on_generate_activity_record_button_clicked(self):
        # 我知道了 可以非常方便地  通过 get activity等 获得 活动的属性 所以 旧有数据 直接用新数据覆盖即可~
        # 更新旧记录！
        #  更新累计时长~
        if type(self.current_activity_record.actual_duration['duration']) == str:
            self.current_activity_record.actual_duration['duration']=str_to_timedelta(self.current_activity_record.actual_duration['duration'])
        if self.current_activity.time_accumulated:
            time_accumulated = str_to_timedelta(self.current_activity.time_accumulated)
        else: time_accumulated = timedelta()

        duration = self.current_activity_record.actual_duration['duration']
        time_accumulated += duration
        self.current_activity.time_accumulated = timedelta_to_str(time_accumulated)
        self.current_activity_record.actual_duration['duration']=timedelta_to_str(self.current_activity_record.actual_duration['duration'])
        # 进行状态  和 累计次数~
        self.current_activity.activity_status["status"]='进行中'
        self.current_activity_record.activity_status['status']='进行中'
        self.current_activity.activity_status["times_performed"]+=1
        self.current_activity_record.activity_status["times_performed"]=self.current_activity.activity_status["times_performed"]
        # 覆盖旧纪录
        update_activity_in_md(self.current_activity)
        update_activity_in_db(self.current_activity)
        
        
        # 向 db 和 md 中 写入活动记录 
        self.current_activity_record.record_timestamp=self.current_activity_record.generate_timestamp()
        #print(self.current_activity_record.actual_duration)
        #print({self.current_activity_record.record_timestamp[:8]}-{self.current_activity_record.actual_duration['start_time'][8:]}-{self.current_activity_record.actual_duration['end_time'][8:]}-{self.current_activity_record.actual_duration['duration']})
        
        write_activity_record_in_md(self.current_activity_record)
        write_activity_record_in_db(self.current_activity_record)
        #self.current_activity.
        
        
        # 修改db 和 md中活动的对应内容
        #self.show_message()
                # Save the original text of the button
        original_text = self.generate_activity_record_button.text()

        # Change the text of the button to "√"
        self.generate_activity_record_button.setText("√")

        # Use QTimer.singleShot to change the text back to the original text after 1 second
        QTimer.singleShot(1000, lambda: self.generate_activity_record_button.setText(original_text))
        
    
    def on_generate_activity_record_final_button_clicked(self):
        
        # 更新旧记录！
        #  更新累计时长~
        if type(self.current_activity_record.actual_duration['duration']) == str:
            self.current_activity_record.actual_duration['duration']=str_to_timedelta(self.current_activity_record.actual_duration['duration'])
        if self.current_activity.time_accumulated:
            time_accumulated = str_to_timedelta(self.current_activity.time_accumulated)
        else: time_accumulated = timedelta()

        duration = self.current_activity_record.actual_duration['duration']
        time_accumulated += duration
        self.current_activity.time_accumulated = timedelta_to_str(time_accumulated)
        self.current_activity_record.actual_duration['duration']=timedelta_to_str(self.current_activity_record.actual_duration['duration'])
        # 进行状态  和 累计次数~
        self.current_activity.activity_status["status"]='已完结'
        self.current_activity_record.activity_status['status']='已完结'
        self.current_activity.activity_status["times_performed"]+=1
        self.current_activity_record.activity_status["times_performed"]=self.current_activity.activity_status["times_performed"]
        # 覆盖旧纪录
        update_activity_in_md(self.current_activity)
        update_activity_in_db(self.current_activity)
        
        
        # 向 db 和 md 中 写入活动记录 
        self.current_activity_record.record_timestamp=self.current_activity_record.generate_timestamp()
        #print(self.current_activity_record.actual_duration)
        #print({self.current_activity_record.record_timestamp[:8]}-{self.current_activity_record.actual_duration['start_time'][8:]}-{self.current_activity_record.actual_duration['end_time'][8:]}-{self.current_activity_record.actual_duration['duration']})
        
        write_activity_record_in_md(self.current_activity_record)
        write_activity_record_in_db(self.current_activity_record)
        move_activity_to_the_end(self.current_activity)
        #self.current_activity. 
        #self.show_message()       
        # Save the original text of the button
        original_text = self.generate_activity_record_final_button.text()

        # Change the text of the button to "√"
        self.generate_activity_record_final_button.setText("√")

        # Use QTimer.singleShot to change the text back to the original text after 1 second
        QTimer.singleShot(1000, lambda: self.generate_activity_record_final_button.setText(original_text))
        
        
    '''def show_message(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("已成功添加记录")
        msgBox.setStandardButtons(QMessageBox.Ok)
        #msgBox.setWindowModality(Qt.ApplicationModal)  # 设置消息框始终在顶部
        QTimer.singleShot(500, msgBox.accept)  # 0.5 seconds
        msgBox.exec()'''
    

    
    
    
    
    
if __name__ == "__main__":
    current_activity = Activity(name="跑步", target_completion_date="2022-12-31", content_location="141+222-sds", 
                    type_location="输出", activity_status={"status": "进行中", "times_performed": 1}, 
                    target_duration=30, progress_description="已完成一半", 
                    handle="这是一段描述\n有多行的\n抓手") 
    
    app = QApplication(sys.argv)
    Activity_Temp_Closure_Window = QMainWindow()
    ui = Ui_activity_temp_closure_activity(Activity_Temp_Closure_Window)
    ui.setupUi()
    Activity_Temp_Closure_Window.show()
    sys.exit(app.exec())
