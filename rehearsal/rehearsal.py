import tkinter as tk
import pandas as pd





# read data from activity_base.xlsx
activity_data = pd.read_excel("activity_data.xlsx")

# assign data to activity
activity = {}
for i in range(len(activity_data)):
    activity_name = str(activity_data.iloc[i, 0])
    positive = str(activity_data.iloc[i, 1]).replace("\\n", "\n")
    gousheng = str(activity_data.iloc[i, 2]).replace("\\n", "\n")
    others = str(activity_data.iloc[i, 3]).replace("\\n", "\n")
    activity[activity_name] = {'pos': positive, 'gou': gousheng, 'qita': others}

# 创建主窗口
root = tk.Tk()
root.title('预演')
root.configure(background="#7792DD")


# 设置窗口大小
root.geometry('1000x600')

# 创建左右两个frame
left_frame = tk.Frame(root)
left_frame.pack(side='left', fill='both', expand=True)

right_frame = tk.Frame(root)
right_frame.pack(side='right', fill='both', expand=True)
# set the background color of the left and right frames
left_frame.configure(background="#7792DD")
right_frame.configure(background="#7792DD")





# 创建列表框
activity_listbox = tk.Listbox(left_frame, font=('TkDefaultFont', 20),background="#92A8E4")
activity_listbox.grid(row=5, column=0, columnspan=2, pady=10)

# 添加活动名称到列表框
for activity_name in activity:
    activity_listbox.insert('end', activity_name)

# 创建标签用于显示信息
positive_message0 = tk.Message(right_frame, text='积极：', font=('TkDefaultFont', 25),background="#7792DD", width=500,foreground='orange')
positive_message0.grid(row=5, column=0, pady=10)
positive_message = tk.Message(right_frame, text='', font=('TkDefaultFont', 20),background="#7792DD", width=500)
positive_message.grid(row=6, column=0, pady=10)

gousheng_message0 = tk.Message(right_frame, text='狗剩：', font=('TkDefaultFont', 25),background="#7792DD", width=500,foreground='orange')
gousheng_message0.grid(row=7, column=0, pady=10)
gousheng_message = tk.Message(right_frame, text='', font=('TkDefaultFont', 20),background="#7792DD", width=500)
gousheng_message.grid(row=8, column=0, pady=10)

others_message0 = tk.Message(right_frame, text='其他：', font=('TkDefaultFont', 25),background="#7792DD", width=500,foreground='orange')
others_message0.grid(row=9, column=0, pady=10)
others_message = tk.Message(right_frame, text='', font=('TkDefaultFont', 20),background="#7792DD", width=500)
others_message.grid(row=10, column=0, pady=10)

# 定义按钮点击事件
def show_activity_info():
    # 获取当前选中的活动名称
    selected_activity = activity_listbox.get(activity_listbox.curselection())

    # 获取活动信息
    positive = activity[selected_activity]['pos']
    gousheng = activity[selected_activity]['gou']
    others = activity[selected_activity]['qita']

    # 显示活动信息
    positive_message.config(text=str(positive))
    gousheng_message.config(text=str(gousheng))
    others_message.config(text=str(others))

# 创建按钮
show_activity_info_button = tk.Button(left_frame, text='显示提醒', font=('TkDefaultFont', 20), command=show_activity_info,background="#B4C2EC")
show_activity_info_button.grid(row=8, column=0, columnspan=2, pady=10)

                
# 运行窗口
root.mainloop()

