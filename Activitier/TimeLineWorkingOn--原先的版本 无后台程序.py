import time
import re
from PySide6.QtCore import QTimer,Qt
from PySide6.QtWidgets import *
from PySide6.QtSql import *
import sqlite3
from datetime import datetime, timedelta


import pyperclip

import sys
import os

# 获取当前文件的绝对路径
current_file_path = os.path.abspath(__file__)
# 获取当前文件的父目录
parent_dir = os.path.dirname(current_file_path)
# 获取functions文件夹的路径
functions_dir = os.path.join(parent_dir, 'ui', 'functions')

# 将functions文件夹的路径添加到Python的搜索路径中
sys.path.append(functions_dir)

# 获取ui文件夹的路径
ui_dir = os.path.join(parent_dir, 'ui')
# 将ui文件夹的路径添加到Python的搜索路径中
sys.path.append(ui_dir)

# 定义基本变量 
time_periods={}
period_index1 = 0
last_index = 0
period_index2 = 0 # 0 代表非任何时间段  


db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("D:\\学习and学校\\搞事情\\LAE\\TimelineAndKanban\\activity.db")


# 导入 窗口 ui  没写！！！
from ui.mainwindow_ui import Ui_MainWindow
from ui.new_period import Ui_Dialog as Ui_Dialog1 
from ui.end_period import Ui_Dialog as Ui_Dialog2
from ui.functions.Class_activityAndRecord import Activity,ActivityRecord
from ui.new_activity_ui import Ui_new_activity
from ui.activity_record_record_ui import Ui_new_activity_record
from ui.start_new_activity_ui import Ui_start_new_activity
from ui.activity_temp_closure_ui import Ui_activity_temp_closure_activity
from ui.functions.write_in_md_and_db import write_activity_in_db,write_activity_in_md,write_activity_record_in_db,write_activity_record_in_md,move_activity_to_the_end
from ui.functions.use_timestamp_read_activity import get_activity
# 导入 子界面 窗口

class new_period_window(QDialog):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_Dialog1()
 # 初始化界面
        self.ui.setupUi(self)

class end_period_window(QDialog):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_Dialog2()
 # 初始化界面
        self.ui.setupUi(self)

class new_activity_window(QMainWindow):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_new_activity(self)
 # 初始化界面
        self.ui.setupUi(db)

class new_activity_record_window(QMainWindow):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_new_activity_record(self)
 # 初始化界面
        self.ui.setupUi(db)

class start_new_activity_window(QMainWindow):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_start_new_activity(self)
 # 初始化界面
        self.ui.setupUi(db)

class activity_temp_closure_window(QMainWindow):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_activity_temp_closure_activity(self)
 # 初始化界面
        self.ui.setupUi() 





app = QApplication(sys.argv)
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi()
main_window = MyWindow()







'''  一、时段 '''

## 从md中读取time_periode的默认值
with open(r'D:\学习and学校\obsidian\qiluo\00-BASE\timeline.md','r',encoding='utf-8') as f:
   text = f.read()
   
for i in range(1, 9):
    time_period = {}
    name_pattern = re.compile(r'{}1【(.*?)】'.format(i))
    start_time_pattern = re.compile(r'{}2【(.*?)】'.format(i))
    end_time_pattern = re.compile(r'{}3【(.*?)】'.format(i))
    #nahh_pattern = re.compile(r'{}4【(.*?)】'.format(i))

    name_match = name_pattern.search(text)
    start_time_match = start_time_pattern.search(text)
    end_time_match = end_time_pattern.search(text)
    #nahh_match = nahh_pattern.search(text)

    if name_match:
        time_period['name'] = name_match.group(1)
    
    if start_time_match:
        time_period['start_time'] = start_time_match.group(1)
    
    if end_time_match:
        time_period['end_time'] = end_time_match.group(1)
    
    
    time_periods['time_period{}'.format(i)] = time_period
# 定义 当前时段 变量
empty_time_period={'name':"空"}
time_periods['time_period0']=empty_time_period
current_time_period = time_periods['time_period{}'.format(0)]
current_activity={}

main_window.ui.current_time_period_label.setText("Name: " + current_time_period['name'])


# 每分钟一次 自动进行 时段确定
def check_period():
    current_time = time.strftime("%H%M")
    
    global period_index1
    for i in range(1,9):
        time_period = time_periods['time_period{}'.format(i)]
        if  time_period['start_time'] <= current_time < time_period['end_time']  :
            
            period_index1 = i
            break
        
           
        elif i == 8:
            period_index1 = 0
            
    
    # 预计 把所有 检查时间和使用行为的 语句 都放在另一个py里~（比如 2300以后使用浏览器行为→锁屏！）

check_period_timer = QTimer() # check period的计时器
check_period_timer.timeout.connect(check_period)
check_period_timer.start(60 * 1000)  # QTimer uses milliseconds

def on_closing():
    main_window.close()



# 定义 开启新时段 和 结束当前时段函数
def start_new_period():
    # pops up a child window  并生成新的 period_index2  
    global period_index2
    global current_time_period
    #global current_period_name_label
    main_window.child_window1=new_period_window()
    
    recommend_period = time_periods['time_period{}'.format(period_index1)]
    main_window.child_window1.ui.recommend_period_label.setText("推荐时段是："+ recommend_period['name'])

    def start_by_set():
        global period_index2
        period_index2 = main_window.child_window1.ui.new_period_entry.text()
        try:
            current_time_period =  time_periods['time_period{}'.format(period_index2)]
            #print("选择了按照自定义")
            # 修正主窗口的 当前阶段 标签
            main_window.ui.current_time_period_label.setText("Name: " + current_time_period["name"])
        except ValueError:
            print("请输入有效值")
        

    def start_by_recommend():
        global period_index2
        period_index2 = period_index1
        current_time_period =  time_periods['time_period{}'.format(period_index2)]
        #print("选择了按照推荐")
        # 修正主窗口的 当前阶段 标签
        main_window.ui.current_time_period_label.setText("Name: " + current_time_period["name"])
        

    # 创建俩按钮 

    main_window.child_window1.ui.by_set_button.clicked.connect(start_by_set)
    main_window.child_window1.ui.by_recommend_button.clicked.connect(start_by_recommend)
    main_window.child_window1.show()



def end_current_period():
    global period_index2
    global current_time_period

    period_index2 = 0
    current_time_period =  time_periods['time_period{}'.format(period_index2)]
    main_window.ui.current_time_period_label.setText("Name: " + current_time_period["name"])



def ask_if_start_new_period(): 
# pops up a child window  
    main_window.child_window2=end_period_window()
    main_window.child_window2.setWindowTitle("是否开启新时段")
    def yes_function():
        start_new_period()
        main_window.child_window2.close()
    # 创建是/否 按钮
    
    main_window.child_window2.ui.yes_button.clicked.connect(yes_function)
    main_window.child_window2.ui.no_button.clicked.connect(main_window.child_window2.close)
    main_window.child_window2.show()


def ask_if_end_current_period():
# pops up a child window  
    main_window.child_window3 = end_period_window()
    def yes_function():
        end_current_period()
        main_window.child_window3.close()
    # 创建是/否 按钮
    main_window.child_window3.ui.yes_button.clicked.connect(yes_function)
    main_window.child_window3.ui.no_button.clicked.connect(main_window.child_window3.close)
    main_window.child_window3.show()

main_window.ui.start_new_period_button.clicked.connect(start_new_period)
main_window.ui.end_period_button.clicked.connect(end_current_period)
main_window.ui.close_window_button.clicked.connect(on_closing)



'''二、活动'''
#  初始化 活动 和 子窗口
main_window.current_activity= Activity(name="")

main_window.start_activity_window= start_new_activity_window()
main_window.new_activity_window=new_activity_window()
main_window.activity_temp_closure_window = activity_temp_closure_window()
main_window.new_activity_record_window = new_activity_record_window()

def open_start_new_activity_window():
    '''   debug ： 这里不能这样搞 可以考虑封装到外面或是一条一条列举'''
    #print("???")
    main_window.start_activity_window.ui.start_chosen_activity_button.clicked.connect(
        lambda: (
            setattr(main_window.current_activity, 'timestamp', main_window.start_activity_window.ui.current_activity.timestamp),
            main_window.start_activity_window.close(),
            new_activity_start()
        )
    )
    
    main_window.start_activity_window.ui.add_new_activity_button.clicked.connect(
        lambda: (
            main_window.new_activity_window.ui.activity_alreadyModify_list.clear(),
            main_window.new_activity_window.ui.reset_current_activity(),
            main_window.new_activity_window.show(),
            main_window.start_activity_window.close()
        )
    )
    
    main_window.start_activity_window.show()
    # 然后开始了新活动  


def on_start_now_button_clicked():
    # 首先 相当于 按了 添加活动 按钮
    main_window.new_activity_window.ui.current_activity.timestamp=main_window.new_activity_window.ui.current_activity.generate_timestamp()

    
    #print("main_window.new_activity_window.ui.current_activity.timestamp",main_window.new_activity_window.ui.current_activity.timestamp)
    # 然后传递 活动的 时间戳
    setattr(main_window.current_activity, 'timestamp', main_window.new_activity_window.ui.current_activity.timestamp)
    
    write_activity_in_md(main_window.new_activity_window.ui.current_activity)
    write_activity_in_db(main_window.new_activity_window.ui.current_activity)


    # 然后 开启活动 并且 关闭子窗口
    new_activity_start()
    main_window.new_activity_window.close()
    if main_window.new_activity_window.ui.current_activity.handle:
        
        pyperclip.copy(main_window.new_activity_window.ui.current_activity.handle)
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("已成功将抓手复制至剪切板")
    msgBox.setStandardButtons(QMessageBox.Ok)
    QTimer.singleShot(500, msgBox.accept)  # 0.5 seconds
    msgBox.exec()

def open_new_activity_record_window():
    main_window.new_activity_record_window.ui.current_activity=Activity(name=' ')
    main_window.new_activity_record_window.ui.current_activity_record= ActivityRecord(main_window.new_activity_record_window.ui.current_activity)
    main_window.new_activity_record_window.show()

main_window.ui.start_activity_button.clicked.connect(open_start_new_activity_window)
main_window.new_activity_window.ui.start_now_button.clicked.connect(on_start_now_button_clicked)
main_window.ui.activity_record_record_button.clicked.connect(open_new_activity_record_window)




# 活动计时部分！！！ & 活动监控部分！！

# 创建一个新的变量来跟踪提示开关状态
reminder_is_on = False

# 创建一个新的变量来跟踪暂停状态
is_paused = False
activity_length = timedelta(seconds=0)
continuous_activity_length = timedelta(seconds=0)


def check_continuous_duration():
    global continuous_activity_length
    total_seconds = continuous_activity_length.total_seconds()
    #print(total_seconds)
    if total_seconds >= 20 * 60:  # 超过20分钟
        msgBox = QMessageBox()
        msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置窗口标志
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("连续时间较长！ 请自行判断是否狗剩 是否需要休息 或 更换活动！！！")
        msgBox.exec()
def check_total_duration():
    global activity_length
    total_seconds = activity_length.total_seconds()
    if 60 * 60 +12 >= total_seconds >= 60 * 60:  # 超过60分钟
        msgBox = QMessageBox()
        msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)  # 设置窗口标志
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("总时长较长！达到计划上限！ 请自行判断是否狗剩 以及适时结束活动")
        msgBox.exec()
    elif total_seconds >= 80 * 60:  # 超过80分钟
        QMessageBox.information(None, "提示", "超过80min：狗剩风险极高！我知道你很急！但是！！！！")



def new_activity_start():
    global reminder_is_on
    # 首先 更新获得的 活动的 各项内容 
    main_window.current_activity = get_activity(main_window.current_activity.timestamp)
    # 更新活动标签
    main_window.ui.current_activity_label.setText("当前进行的活动为：" + main_window.current_activity.name)
    # 开始计时
    start_activity_timer()    
    # 复制抓手到剪切板
    if main_window.current_activity.handle:
        pyperclip.copy(main_window.current_activity.handle)
    if main_window.current_activity.type_location == "12-编程":
        reminder_is_on = True

def start_activity_timer():
    global is_paused, activity_length,activity_timer,start_time,continuous_activity_length,continuous_timer
    # 开始计时
    activity_length = timedelta(seconds=0)
    start_time = datetime.now()
    is_paused = False
    activity_timer = QTimer()
    continuous_timer = QTimer()
    # 连接计时器的超时信号到update_label函数
    activity_timer.timeout.connect(update_label)
    continuous_timer.timeout.connect(update_continuous_label)  # 连接连续计时器的超时信号到新的更新函数
    # 开始计时器每秒更新标签
    activity_timer.start(2000)  # 每1s更新一次
    continuous_timer.start(2000)  # 连续计时器也每1s更新一次


def update_label():
    global is_paused, activity_length
    if not is_paused:
        # 计算经过的时间
        activity_length += timedelta(seconds=2)
        total_seconds = activity_length.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        # 更新标签的格式化时间
        main_window.ui.timer_label.setText(formatted_time)
        # 检查活动类型，如果满足条件则启动提示器
        if reminder_is_on:
            check_total_duration()


def update_continuous_label():
    global is_paused, continuous_activity_length
    if not is_paused:
        # 计算经过的时间
        continuous_activity_length += timedelta(seconds=2)
        total_seconds = continuous_activity_length.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        # 更新标签的格式化时间
        main_window.ui.continuous_timer_label.setText(formatted_time)  # 假设你有一个标签用于显示连续时间
        if reminder_is_on:
            check_continuous_duration()

def pause_resume_activity():
    global is_paused,continuous_activity_length
    # 切换暂停状态
    is_paused = not is_paused
    if is_paused:
        # 如果暂停，重置连续活动长度
        continuous_activity_length = timedelta(seconds=0)

def restart_activity():
    global activity_length, activity_timer, continuous_activity_length, continuous_timer
    # 停止当前的计时器
    if activity_timer is not None:
        activity_timer.stop()
    if continuous_timer is not None:
        continuous_timer.stop()
    # 重置活动长度
    activity_length = timedelta(seconds=0)
    continuous_activity_length = timedelta(seconds=0)  # 重置连续活动长度
    # 重新开始计时
    start_activity_timer()


def end_activity():
    global activity_timer
    activity_timer.stop()
    continuous_timer.stop()
    main_window.current_activity_record= ActivityRecord(main_window.current_activity)
    main_window.current_activity_record.actual_duration['duration']= activity_length
    # 生成结束时间 和时间戳
    end_time   = datetime.now()
    main_window.current_activity_record.actual_duration["end_time"] = end_time.strftime("%H:%M")
    main_window.current_activity_record.actual_duration["start_time"] = start_time.strftime("%H:%M")
    #main_window.current_activity_record.record_timestamp= main_window.current_activity_record.generate_timestamp()
    main_window.activity_temp_closure_window.ui.current_activity =main_window.current_activity
    main_window.activity_temp_closure_window.ui.current_activity_record =main_window.current_activity_record
    main_window.activity_temp_closure_window.ui.resetUi()
    main_window.activity_temp_closure_window.show()
    #print(main_window.activity_temp_closure_window.ui.current_activity_record.name)
    











# 连接按钮的点击信号到相应的函数
main_window.ui.start_restart_button.clicked.connect(restart_activity)
main_window.ui.pause_button.clicked.connect(pause_resume_activity)    
main_window.ui.end_activity_button.clicked.connect(end_activity)
    

#  来自 开启新活动 子窗口 开始选中活动 self.start_chosen_activity_button 
#   add_new_activity_button 应该出发 添加新活动 子窗口 


# 通过 开启活动 的 添加新活动再开始 调用 添加新活动 并关闭自身： 建议在此主程序中定义功能~

# 开启活动 内部 定义一个 activity  然后 再来个  main_window.current_activity = main_window.childwindow.activity 即可~
# 这样传过去之后，再关闭child window（再一次，按钮功能在这里定义）


check_period()
main_window.show()
sys.exit(app.exec())





