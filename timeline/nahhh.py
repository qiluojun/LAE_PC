import time
import re
from activityCode import read_activity
from datetime import datetime
import os
from timeline_url import get_address
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFrame, QTextEdit, QGridLayout, QListView, QAbstractItemView, QListWidgetItem, QLineEdit, QInputDialog
from PySide6.QtCore import Qt, QTimer, QThread, Signal
from PySide6.QtGui import QFont




# 定义基本变量 
time_periods={}
period_index1 = 0
last_index = 0
period_index2 = 0 # 0 代表非任何时间段  
activities={}


## 从md中读取time_periode的默认值
with open(r'D:\学习and学校\obsidian\qiluo\00-MOC\timeline.md','r',encoding='utf-8') as f:
   text = f.read()

for i in range(1, 9):
    time_period = {}
    name_pattern = re.compile(r'{}1【(.*?)】'.format(i))
    start_time_pattern = re.compile(r'{}2【(.*?)】'.format(i))
    end_time_pattern = re.compile(r'{}3【(.*?)】'.format(i))
    nahh_pattern = re.compile(r'{}4【(.*?)】'.format(i))

    name_match = name_pattern.search(text)
    start_time_match = start_time_pattern.search(text)
    end_time_match = end_time_pattern.search(text)
    nahh_match = nahh_pattern.search(text)

    if name_match:
        time_period['name'] = name_match.group(1)
    
    if start_time_match:
        time_period['start_time'] = start_time_match.group(1)
    
    if end_time_match:
        time_period['end_time'] = end_time_match.group(1)
    
    if nahh_match:
        time_period['nahh'] = nahh_match.group(1)
    
    
    time_periods['time_period{}'.format(i)] = time_period
# 定义 当前时段 变量
empty_time_period={'name':"空"}
time_periods['time_period0']=empty_time_period
current_time_period = time_periods['time_period{}'.format(0)]
current_activity={}

# create a mainwindow
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("时段&活动（☆▽☆）")
window.setGeometry(100, 100, 1450, 650)


# Create two frames 我也不知道为啥要俩frames 先搞了再说！
left_frame = QFrame(window)
left_frame.setFrameShape(QFrame.StyledPanel)
right_frame = QFrame(window)
right_frame.setFrameShape(QFrame.StyledPanel)

layout = QVBoxLayout()
layout.addWidget(left_frame)
layout.addWidget(right_frame)
window.setLayout(layout)


# 在主界面 呈现 当前period的信息 —— 后面每更新一次 都需要重新修改label的内容
# Create labels to display the attributes of the current period
current_period_name_label = QLabel("Name: " + current_time_period['name'], left_frame)
current_period_name_label.setFont(QFont("TkDefaultFont", 16))
current_period_name_label.setStyleSheet("color: #EF7228")

# 在主界面 呈现对应的plan
plan_text = QTextEdit(left_frame)
plan_text.setFont(QFont("TkDefaultFont",20))
plan_text.setFixedSize(60, 15)



def read_plan():
    global period_index2
    global activities
    #print(period_index2)
    title_number = str(period_index2)
    title = '### ' + title_number
    directory = r'D:\学习and学校\obsidian\qiluo\01-Diary\日志存档'
    filename = os.path.join(directory, datetime.now().strftime('%Y-%m-%d') + '.md')
    if not os.path.exists(filename):
        plan_text.clear()
        plan_text.insertPlainText(f'File {filename} does not exist.')
        return
    with open(filename,'r',encoding='utf-8') as f:
        lines = f.readlines()
        plan = []
        record = False
        i=0
        for line in lines:
            
            if line.startswith(title):
                record = True
                i=1
            elif line.startswith('###'):
                record = False
                i=0
            elif i==1:
                if "+{" in line:
                    record = False
                elif "}+" in line:
                    record = True
                elif record:
                    plan.append(line)
    plan = ''.join(plan)
    plan_show=''
    activities,plan_show= read_activity(plan)
    plan_text.clear()
    plan_text.insertPlainText(plan_show)
    activity_listbox.clear()
    for activity in activities.values():
        item = QListWidgetItem(activity['name'])
        activity_listbox.addItem(item)
    

def refresh_plan():
    read_plan()
    global current_activity
    for zhanKong in activities.values():
        if current_activity:
            if current_activity['name'] == zhanKong['name']:
                current_activity['time']=zhanKong['time']
                current_activity['content']=zhanKong['content']

    

# 手动更新plan
button = QPushButton('Show plan', left_frame)
button.setFont(QFont("TkDefaultFont",16))
button.clicked.connect(refresh_plan)


# 添加 close programme

def on_closing():
    # stop the reminder_timer thread
    global time_period_timer
    if time_period_timer:
        time_period_timer.cancel()
    # destroy the root window
    window.close()



# create a global variable to store the timer object
time_period_timer = None

# function to check what period
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
            #print("??")
    # check every minute
    # start the timer again
    global time_period_timer
    time_period_timer = QTimer()
    time_period_timer.timeout.connect(check_period)
    time_period_timer.start(60000)
    # 判断 index1是否发生了改变
    global last_index  # Declare last_index as a global variable
    #print("last index:")
    #print(last_index)
    #print("index1:")
    #print(period_index1)
    if period_index1 != last_index :
        last_index = period_index1

        if period_index1 !=0 and period_index2 == 0 :
            ask_if_start_new_period()
            #print("ask_if_start_new_period at")
            #print(current_time)
        else :
            ask_if_end_current_period()
            #print("ask_if_end_current_period")
            #print(current_time)     
    #print("check_period at")
    #print(current_time)    



# 定义 开启新时段 和 结束当前时段函数
def start_new_period():
    # pops up a child window  并生成新的 period_index2  
    global period_index2
    global current_time_period
    #global current_period_name_label
    child_window = QWidget()
    child_window.setWindowTitle("开启新时段！")
    child_window.setWindowModality(Qt.ApplicationModal)
    child_window.setGeometry(100, 100, 800, 200)
    # 显示根据index1 判断的当前时段
    recommend_period = time_periods['time_period{}'.format(period_index1)]
    recommend_period_label = QLabel(f"推荐时段是：{recommend_period['name']}", child_window)
    recommend_period_label.setFont(QFont("TkDefaultFont", 20))
    recommend_period_label.setStyleSheet("color: blue")
      


    # 指定新的period
    entry_label = QLabel("请输入指定的period编号", child_window)
    entry_label.setFont(QFont("TkDefaultFont", 20))
    entry_label.setStyleSheet("color: blue")
       
    new_period_entry = QLineEdit(child_window)
    new_period_entry.setFont(QFont("TkDefaultFont", 20))

    def start_by_set():
        global period_index2
        period_index2 = new_period_entry.text()
        current_time_period =  time_periods['time_period{}'.format(period_index2)]
        #print("选择了按照自定义")
        # 修正主窗口的 当前阶段 标签
        current_period_name_label.setText("Name: " + current_time_period["name"])
        read_plan()

    def start_by_recommend():
        global period_index2
        period_index2 = period_index1
        current_time_period =  time_periods['time_period{}'.format(period_index2)]
        #print("选择了按照推荐")
        # 修正主窗口的 当前阶段 标签
        current_period_name_label.setText("Name: " + current_time_period["name"])
        read_plan()

    # 创建俩按钮 
    by_set_button= QPushButton("start_by_set", child_window)
    by_set_button.setFont(QFont("TkDefaultFont", 20))
    by_set_button.clicked.connect(start_by_set)
    by_recommend_button = QPushButton("start_by_recommend", child_window)
    by_recommend_button.setFont(QFont("TkDefaultFont", 20))
    by_recommend_button.clicked.connect(start_by_recommend)

    layout = QGridLayout(child_window)
    layout.addWidget(recommend_period_label, 0, 0)
    layout.addWidget(entry_label, 1, 0)
    layout.addWidget(new_period_entry, 1, 1)
    layout.addWidget(by_recommend_button, 2, 0)
    layout.addWidget(by_set_button, 2, 1)
    child_window.setLayout(layout)
    child_window.show()


def end_current_period():
    global period_index2
    global current_time_period
    end_activity()
    # output_data() 
    period_index2 = 0
    current_time_period =  time_periods['time_period{}'.format(period_index2)]
    current_period_name_label.setText("Name: " + current_time_period["name"])
    plan_text.clear()
    activity_listbox.clear()
def ask_if_start_new_period():
    # pops up a child window  
    child_window1 = QWidget()
    child_window1.setWindowTitle("是否开启新时段")
    child_window1.setWindowModality(Qt.ApplicationModal)
    child_window1.setGeometry(300, 200, 500, 500)

    def yes_function():
        start_new_period()
        child_window1.close()
    # 创建是/否 按钮
    yes_button= QPushButton("yes", child_window1)
    yes_button.setFont(QFont("TkDefaultFont", 20))
    yes_button.clicked.connect(yes_function)
    no_button = QPushButton("no", child_window1)
    no_button.setFont(QFont("TkDefaultFont", 20))
    no_button.clicked.connect(child_window1.close)
    layout = QVBoxLayout()
    layout.addWidget(yes_button)
    layout.addWidget(no_button)
    child_window1.setLayout(layout)
    child_window1.show()

def ask_if_end_current_period():
    # pops up a child window  
    child_window2 = QWidget()
    child_window2.setWindowTitle("是否结束当前时段")
    child_window2.setWindowModality(Qt.ApplicationModal)
    child_window2.setGeometry(300, 200)
    def yes_function():
        end_current_period()
        child_window2.close()
    # 创建是/否 按钮
    yes_button= QPushButton("yes", child_window2)
    yes_button.setFont(QFont("TkDefaultFont", 20))
    yes_button.clicked.connect(yes_function)
    no_button = QPushButton("no", child_window2)
    no_button.setFont(QFont("TkDefaultFont", 20))
    no_button.clicked.connect(child_window2.close)
    layout = QVBoxLayout()
    layout.addWidget(yes_button)
    layout.addWidget(no_button)
    child_window2.setLayout(layout)
    child_window2.show()


# 在主窗口上放对应的俩按钮
start_new_period_button= QPushButton("开启新时段", right_frame)
start_new_period_button.setFont(QFont("TkDefaultFont", 20))
start_new_period_button.clicked.connect(start_new_period)
end_current_period_button = QPushButton("结束当前时段", right_frame)
end_current_period_button.setFont(QFont("TkDefaultFont", 20))
end_current_period_button.clicked.connect(end_current_period)
layout = QVBoxLayout()
layout.addWidget(start_new_period_button)
layout.addWidget(end_current_period_button)
right_frame.setLayout(layout)
close_button = QPushButton("Close", right_frame)
close_button.setFont(QFont("TkDefaultFont", 20))
close_button.clicked.connect(on_closing)
layout.addWidget(close_button)


# start the period checking function in a separate thread
class TimePeriodThread(QThread):
    def run(self):
        check_period()

time_period_timer = TimePeriodThread()

time_period_timer.start()




# 下面是呈现activity的部分
activity_listbox = QListView(right_frame)
activity_listbox.setFont(QFont("TkDefaultFont", 20))

for activity in activities:
    item = QListWidgetItem(activity['name'])
    activity_listbox.addItem(item)
layout.addWidget(activity_listbox)




# 先在这里写 然后放在mainwindow上？ 
# 然后是呈现当前活动 + 结算



def update_activity():
    # get the selected reminder from the listbox
    selected_index = activity_listbox.currentIndex().row()
    global current_activity
    if selected_index is not None:
        current_activity=activities['activity{}'.format(selected_index+1)]
        current_activity_name_label.setText("Name: " + current_activity['name'])
        current_activity['start_time']= datetime.now().strftime("%H:%M")

def end_activity():
    #1. 读取地址 
    
    global current_activity
    if current_activity:
        current_activity['date']=datetime.now().strftime("%D")
        current_activity['end_time']=datetime.now().strftime("%H:%M")
        # Convert start_time and end_time to datetime objects
        start_time = datetime.strptime(current_activity['start_time'], "%H:%M")
        end_time = datetime.strptime(current_activity['end_time'], "%H:%M")

        # Calculate the time difference
        time_difference = end_time - start_time

        current_activity['lenth'] = str(time_difference)
        decoded_url=get_address(current_activity['address'])
        content=''
        #2. 对应地址处 写对应的变量！ 小心局部与全局的问题
        # 先定义出要写的 content
        content = '\n\n{}--{}-{}  {} vs {}\n{}'.format(current_activity['date'],current_activity['start_time'],current_activity['end_time'],current_activity['lenth'],current_activity['time'],current_activity['content'])
        # 写入
        with open(decoded_url,'a',encoding='utf-8') as f:
            f.write(content)
    # 最后再清空
    current_activity={}
    current_activity_name_label.setText("Name: 空")





# 创建俩按钮 
new_activity_button= QPushButton("新活动", right_frame)
new_activity_button.setFont(QFont("TkDefaultFont", 20))
new_activity_button.clicked.connect(update_activity)
end_activity_button = QPushButton("结束活动", right_frame)
end_activity_button.setFont(QFont("TkDefaultFont", 20))
end_activity_button.clicked.connect(end_activity)
layout.addWidget(new_activity_button)
layout.addWidget(end_activity_button)
# 主界面 呈现当前活动
current_activity_name_label = QLabel("", right_frame)
current_activity_name_label.setFont(QFont("TkDefaultFont", 16))
current_activity_name_label.setStyleSheet("color: #EF7228")
layout.addWidget(current_activity_name_label)


def basic_state_record():
    child_window = QWidget()
    child_window.setWindowTitle("记录基础状态")
    child_window.setWindowModality(Qt.ApplicationModal)
    child_window.setGeometry(800, 400)
    # 创建属性输入框
    tiredness_label = QLabel("困倦度：", child_window)
    tiredness_label.setFont(QFont("TkDefaultFont", 20))
    tiredness_label.setStyleSheet("color: blue")
    tiredness_entry = QLineEdit(child_window)
    tiredness_entry.setFont(QFont("TkDefaultFont", 20))

    exhaustion_label = QLabel("脑损度：", child_window)
    exhaustion_label.setFont(QFont("TkDefaultFont", 20))
    exhaustion_label.setStyleSheet("color: blue")
    exhaustion_entry = QLineEdit(child_window)
    exhaustion_entry.setFont(QFont("TkDefaultFont", 20))

    anxiety_label = QLabel("焦虑度：", child_window)
    anxiety_label.setFont(QFont("TkDefaultFont", 20))
    anxiety_label.setStyleSheet("color: blue")
    anxiety_entry = QLineEdit(child_window)
    anxiety_entry.setFont(QFont("TkDefaultFont", 20))

    vitality_label = QLabel("体力值：", child_window)
    vitality_label.setFont(QFont("TkDefaultFont", 20))
    vitality_label.setStyleSheet("color: blue")
    vitality_entry = QLineEdit(child_window)
    vitality_entry.setFont(QFont("TkDefaultFont", 20))

    activeness_label = QLabel("积极愉悦度：", child_window)
    activeness_label.setFont(QFont("TkDefaultFont", 20))
    activeness_label.setStyleSheet("color: blue")
    activeness_entry = QLineEdit(child_window)
    activeness_entry.setFont(QFont("TkDefaultFont", 20))

    def basic_state_record_generate():
        basic_state={}
        basic_state['time']= datetime.now().strftime("%D:%H:%M")
        basic_state['tiredness'] = (tiredness_entry.text())
        basic_state['exhaustion'] = (exhaustion_entry.text())
        basic_state['anxiety'] = (anxiety_entry.text())
        basic_state['vitality'] = (vitality_entry.text())
        basic_state['activeness'] = (activeness_entry.text())
        content=''
        content = '{} {} {} {} {} {}\n'.format(basic_state['time'],basic_state['tiredness'],basic_state['exhaustion'],basic_state['anxiety'],basic_state['vitality'],basic_state['activeness'])
        with open(r'D:\学习and学校\obsidian\qiluo\00-MOC\basic_state.md','a',encoding='utf-8') as f:
            f.write(content)
        # 创建确定按钮
    yes_button = QPushButton("生成记录", child_window)
    yes_button.setFont(QFont("TkDefaultFont", 20))
    yes_button.clicked.connect(basic_state_record_generate)
    layout = QVBoxLayout()
    layout.addWidget(tiredness_label)
    layout.addWidget(tiredness_entry)
    layout.addWidget(exhaustion_label)
    layout.addWidget(exhaustion_entry)
    layout.addWidget(anxiety_label)
    layout.addWidget(anxiety_entry)
    layout.addWidget(vitality_label)
    layout.addWidget(vitality_entry)
    layout.addWidget(activeness_label)
    layout.addWidget(activeness_entry)
    layout.addWidget(yes_button)
    child_window.setLayout(layout)
    child_window.show()







#  创建 【基本状态记录】 按钮
update_button = QPushButton("记录基本状态", left_frame)
update_button.setFont(QFont("TkDefaultFont", 20))
update_button.clicked.connect(basic_state_record)
layout.addWidget(update_button)







# start the main loop
app.exec()





