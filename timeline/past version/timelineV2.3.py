import time
import tkinter as tk
from tkinter import END
import threading
import re
from activityCode import read_activity
from datetime import datetime
import os
from timeline_url import get_address



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
root = tk.Tk()
root.title("时段&活动（☆▽☆）")
root.geometry("1450x650")


# Create two frames 我也不知道为啥要俩frames 先搞了再说！
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True)
right_frame = tk.Frame(root)
right_frame.pack(side="left", fill="both", expand=True)


# 在主界面 呈现 当前period的信息 —— 后面每更新一次 都需要重新修改label的内容
# Create labels to display the attributes of the current period
current_period_name_label = tk.Label(left_frame, text="Name: " + current_time_period['name'], fg="#EF7228", font=("TkDefaultFont", 16))
current_period_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# 在主界面 呈现对应的plan
plan_text = tk.Text(left_frame,font=("TkDefaultFont",20),width=60, height=15)
plan_text.grid(row=1, column=0, padx=10, pady=10, sticky="w")



def read_plan():
    global period_index2
    global activities
    #print(period_index2)
    title_number = str(period_index2)
    title = '### ' + title_number
    directory = r'D:\学习and学校\obsidian\qiluo\01-Diary\日志存档'
    filename = os.path.join(directory, datetime.now().strftime('%Y-%m-%d') + '.md')
    if not os.path.exists(filename):
        plan_text.delete('1.0', tk.END)
        plan_text.insert(tk.END, f'File {filename} does not exist.')
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
    plan_text.delete('1.0', tk.END)
    plan_text.insert(tk.END, plan_show)
    activity_listbox.delete(0, tk.END)
    for activity in activities.values():
        activity_listbox.insert(tk.END, activity['name'])
    activity_listbox.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    

def refresh_plan():
    read_plan()
    global current_activity
    for zhanKong in activities.values():
        if current_activity:
            if current_activity['name'] == zhanKong['name']:
                current_activity['time']=zhanKong['time']
                current_activity['content']=zhanKong['content']

    

# 手动更新plan
button = tk.Button(left_frame, text='Show plan', command= refresh_plan,font=("TkDefaultFont",16))
button.grid(row=2, column=0, padx=10, pady=10, sticky="w")


# 添加 close programme

def on_closing():
    # stop the reminder_timer thread
    global time_period_timer
    if time_period_timer:
        time_period_timer.cancel()
    # destroy the root window
    root.destroy()



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
    time_period_timer = threading.Timer(60, check_period)
    time_period_timer.start()
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
    child_window = tk.Toplevel()
    child_window.title("开启新时段！")
    child_window.attributes('-topmost', True)
    child_window.geometry("800x200")
    # 显示根据index1 判断的当前时段
    recommend_period = time_periods['time_period{}'.format(period_index1)]
    recommend_period_label = tk.Label(child_window, text=f"推荐时段是：{recommend_period['name']}", font=("TkDefaultFont", 20), fg="blue")
    recommend_period_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
      


    # 指定新的period
    entry_label = tk.Label(child_window, text="请输入指定的period编号", font=("TkDefaultFont", 20), fg="blue")
    entry_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
       
    new_period_entry = tk.Entry(child_window, font=("TkDefaultFont", 20))
    new_period_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def start_by_set():
        global period_index2
        period_index2 = new_period_entry.get()
        current_time_period =  time_periods['time_period{}'.format(period_index2)]
        #print("选择了按照自定义")
        # 修正主窗口的 当前阶段 标签
        current_period_name_label.config(text="Name: " + current_time_period["name"])
        read_plan()

    def start_by_recommend():
        global period_index2
        period_index2 = period_index1
        current_time_period =  time_periods['time_period{}'.format(period_index2)]
        #print("选择了按照推荐")
        # 修正主窗口的 当前阶段 标签
        current_period_name_label.config(text="Name: " + current_time_period["name"])
        read_plan()

    # 创建俩按钮 
    by_set_button= tk.Button(child_window, text="start_by_set", command= start_by_set, font=("TkDefaultFont", 20))
    by_recommend_button = tk.Button(child_window, text="start_by_recommend", command= start_by_recommend, font=("TkDefaultFont", 20)) 
    by_recommend_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    by_set_button.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    

def end_current_period():
    global period_index2
    global current_time_period
    end_activity()
    # output_data() 
    period_index2 = 0
    current_time_period =  time_periods['time_period{}'.format(period_index2)]
    current_period_name_label.config(text="Name: " + current_time_period["name"])
    plan_text.delete('1.0', tk.END)
    activity_listbox.delete(0, tk.END)

def ask_if_start_new_period():
# pops up a child window  
    child_window1 = tk.Toplevel()
    child_window1.title("是否开启新时段")
    child_window1.attributes('-topmost', True)
    child_window1.geometry("300x200")
    def yes_function():
        start_new_period()
        child_window1.destroy()
    # 创建是/否 按钮
    yes_button= tk.Button(child_window1, text="yes", command=yes_function , font=("TkDefaultFont", 20))
    no_button = tk.Button(child_window1, text="no", command= child_window1.destroy, font=("TkDefaultFont", 20)) 
    yes_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    no_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")   

def ask_if_end_current_period():
# pops up a child window  
    child_window2 = tk.Toplevel()
    child_window2.title("是否结束当前时段")
    child_window2.attributes('-topmost', True)
    child_window2.geometry("300x200")
    def yes_function():
        end_current_period()
        child_window2.destroy()
    # 创建是/否 按钮
    yes_button= tk.Button(child_window2, text="yes", command=yes_function , font=("TkDefaultFont", 20))
    no_button = tk.Button(child_window2, text="no", command= child_window2.destroy, font=("TkDefaultFont", 20)) 
    yes_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    no_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")   
 



# 在主窗口上放对应的俩按钮
start_new_period_button= tk.Button(right_frame, text="开启新时段", command= start_new_period, font=("TkDefaultFont", 20))
end_current_period_button = tk.Button(right_frame, text="结束当前时段", command= end_current_period, font=("TkDefaultFont", 20)) 
start_new_period_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")
end_current_period_button.grid(row=3, column=0, padx=10, pady=10, sticky="w")
close_button = tk.Button(right_frame, text="Close", command=on_closing,font=("TkDefaultFont", 20))
close_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")



# start the period checking function in a separate thread
time_period_timer = threading.Thread(target=check_period)
time_period_timer.start()




# 下面是呈现activity的部分
activity_listbox = tk.Listbox(right_frame, font=("TkDefaultFont", 20),width=40)

for activity in activities:
    activity_listbox.insert(tk.END, activity['name']) 
activity_listbox.grid(row=5, column=0, padx=10, pady=10, sticky="w")




# 先在这里写 然后放在mainwindow上？ 
# 然后是呈现当前活动 + 结算



def update_activity():
    # get the selected reminder from the listbox
    selected_index = activity_listbox.curselection()
    global current_activity
    if selected_index:
        selected_index = int(selected_index[0])
        current_activity=activities['activity{}'.format(selected_index+1)]
        current_activity_name_label.config(text="Name: " + current_activity['name'])
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
    current_activity_name_label.config(text="Name: 空")





# 创建俩按钮 
new_activity_button= tk.Button(right_frame, text="新活动", command=update_activity, font=("TkDefaultFont", 20))
end_activity_button = tk.Button(right_frame, text="结束活动", command=end_activity, font=("TkDefaultFont", 20)) 
new_activity_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")
end_activity_button.grid(row=7, column=0, padx=200, pady=10, sticky="w")
# 主界面 呈现当前活动
current_activity_name_label = tk.Label(right_frame, text="" , fg="#EF7228", font=("TkDefaultFont", 16))
current_activity_name_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")





# start the main loop
root.mainloop()



