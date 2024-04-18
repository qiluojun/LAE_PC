import sys
import time
import re
import os
from PySide6.QtCore import QTimer,Qt
from PySide6.QtWidgets import *
from PySide6.QtSql import *
import sqlite3

sys.coinit_flags = 2
from pywinauto import Desktop

from mainwindow import Ui_MainWindow
from lock_screen import LockScreenWindow
from reminder_pop_up import Reminder_pop_up
from new_period import Ui_Dialog as Ui_Dialog1 
from end_period import Ui_Dialog as Ui_Dialog2
from basicStateRecord2 import Ui_Dialog as Ui_Dialog3



def for_test():
    print("test")




# 定义基本变量 
time_periods={}
period_index1 = 0
last_index = 0
period_index2 = 0 # 0 代表非任何时间段  
activities={}


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
class basic_state_record_window(QDialog):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_Dialog3()
 # 初始化界面
        self.ui.setupUi(self)   


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
    
    #if nahh_match:
        #time_period['nahh'] = nahh_match.group(1)
    
    
    time_periods['time_period{}'.format(i)] = time_period
# 定义 当前时段 变量
empty_time_period={'name':"空"}
time_periods['time_period0']=empty_time_period
current_time_period = time_periods['time_period{}'.format(0)]
current_activity={}





'''main_window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(main_window)'''

# 创建主窗口
class MyWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        #self.lock_window = None   Initialize lock_window
        self.ui = Ui_MainWindow()
 # 初始化界面
        self.ui.setupUi(self)
        
       



# 启动窗口
app = QApplication(sys.argv)

main_window=MyWindow()

# 显示主窗口 
main_window.show()
# bug 1
# 真奇怪 如果不把search activity 函数里的语句 放在setupUi里 就执行不了 为啥？
# 有可能与 search activity 里调用的其他函数有关
main_window.ui.current_period_name_label.setText("Name: " + current_time_period['name'])


# 链接 activity 相关功能——在mainwindow.py中实现了


'''
这一部分待写！！！！ new functions~
'''


# 链接 show plan 功能 
    # 更新！与activity 结合！ 还没写好哈哈哈
def read_plan():
    global period_index2
    global activities
    #print(period_index2)
    title_number = str(period_index2)
    title = '### ' + title_number
    directory = r'D:\学习and学校\obsidian\qiluo\01-Diary\日志存档'
    filename = os.path.join(directory, datetime.now().strftime('%Y-%m-%d') + '.md')
    if not os.path.exists(filename):
        main_window.ui.plan_text.clear()
        main_window.ui.plan_text.insertPlainText(f'File {filename} does not exist.')
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
    main_window.ui.plan_text.clear()
    main_window.ui.plan_text.insertPlainText(plan_show)
    main_window.ui.activity_list.clear()
    for activity in activities.values():
        item = QListWidgetItem(activity['name'])
        main_window.ui.activity_list.addItem(item)
    

def refresh_plan():
    read_plan()
    global current_activity
    for zhanKong in activities.values():
        if current_activity:
            if current_activity['name'] == zhanKong['name']:
                current_activity['time']=zhanKong['time']
                current_activity['content']=zhanKong['content']

    
main_window.ui.show_plan_button.clicked.connect(refresh_plan)
#main_window.ui.show_plan_button.clicked.connect(for_test)



# check period & 锁屏
def lock(locking_time):
    main_window.lock_window= LockScreenWindow(locking_time,period_index1)
    main_window.lock_window.show()

   
    
main_window.ui.lock_button.clicked.connect(lock) # 添加立刻锁屏按钮

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
            
    # 2140-2200 + 2300以后 进行预警！！  # 测试 所以加了一个！
    if current_time >=  '2140' :
        #lock(0.2) # 锁屏时长 #ceshi 
        windows = Desktop(backend="uia").windows()
        current_names = set(w.window_text() for w in windows if w.window_text().strip())
        danger = False
        for name in current_names:
            if "Edge"    in name or "PotPlayer" in name:
                danger = True
        if danger:
            lock(0.5)
    
    elif current_time >=  '1800' and current_time <= '2030' :
        if period_index2 == 0 or not(current_activity):
            main_window.pop_up=Reminder_pop_up(period_index1)
            main_window.pop_up.show()


check_period_timer = QTimer() # check period的计时器
check_period_timer.timeout.connect(check_period)
check_period_timer.start(60 * 1000)  # QTimer uses milliseconds



# 其他功能： close


def on_closing():
    if main_window.lock_window:
        main_window.lock_window.check_timer.stop()
    main_window.close()

main_window.ui.close_button.clicked.connect(on_closing)




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
            main_window.ui.current_period_name_label.setText("Name: " + current_time_period["name"])
        except ValueError:
            print("请输入有效值")
        read_plan()

    def start_by_recommend():
        global period_index2
        period_index2 = period_index1
        current_time_period =  time_periods['time_period{}'.format(period_index2)]
        #print("选择了按照推荐")
        # 修正主窗口的 当前阶段 标签
        main_window.ui.current_period_name_label.setText("Name: " + current_time_period["name"])
        read_plan()

    # 创建俩按钮 

    main_window.child_window1.ui.by_set_button.clicked.connect(start_by_set)
    main_window.child_window1.ui.by_recommend_button.clicked.connect(start_by_recommend)
    main_window.child_window1.show()



def end_current_period():
    global period_index2
    global current_time_period
    end_activity()
    # output_data() 
    period_index2 = 0
    current_time_period =  time_periods['time_period{}'.format(period_index2)]
    main_window.ui.current_period_name_label.setText("Name: " + current_time_period["name"])
    main_window.ui.plan_text.clear()
    main_window.ui.activity_list.clear()

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
main_window.ui.end_current_period_button.clicked.connect(end_current_period)
main_window.ui.close_button.clicked.connect(on_closing)





# 链接 state record 功能

def basic_state_record():
    main_window.child_window4 = basic_state_record_window()
    
    def basic_state_record_generate():
        basic_state={}
        basic_state['time']= datetime.now().strftime("%D:%H:%M")
        basic_state['tiredness'] = (main_window.child_window4.ui.tiredness)
        basic_state['exhaustion'] = (main_window.child_window4.ui.exhaustion)
        basic_state['anxiety'] = (main_window.child_window4.ui.anxiety)
        basic_state['vitality'] = (main_window.child_window4.ui.vitality)
        basic_state['activeness'] = (main_window.child_window4.ui.activeness)
        write_state(basic_state)
        main_window.current_state= State(basic_state,period_index1)
    # 创建确定按钮
    main_window.child_window4.ui.yes_button.clicked.connect(basic_state_record_generate)
    main_window.child_window4.show()

main_window.ui.basic_state_record_button.clicked.connect(basic_state_record)
check_period()







#sys.exit(app.exec())
app.exec()



















