import tkinter as tk
import pandas as pd

# read data from activity_base.xlsx
activity_data = pd.read_excel('activity_data.xlsx')

# assign data to activity
activity = {}
for i in range(len(activity_data)):
    activity_name = activity_data.iloc[i, 0]
    activity_1time_imit = activity_data.iloc[i, 1]
    activity_Ttime_imit = activity_data.iloc[i, 2]
    activity_tips = activity_data.iloc[i, 3]
    activity[activity_name] = {'1time_imit': activity_1time_imit, 'Ttime_imit': activity_Ttime_imit, 'tips': activity_tips}

# 创建主窗口
root = tk.Tk()
root.title('状态判断&活动选择及提醒')
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



# 创建标签和输入框
tk.Label(right_frame, text='working', font=('TkDefaultFont', 20),background="#7792DD").grid(row=0, column=0)
working_entry = tk.Entry(right_frame, font=('TkDefaultFont', 20),background="#92A8E4")
working_entry.grid(row=0, column=1)

tk.Label(right_frame, text='energy', font=('TkDefaultFont', 20),background="#7792DD").grid(row=1, column=0)
energy_entry = tk.Entry(right_frame, font=('TkDefaultFont', 20),background="#92A8E4")
energy_entry.grid(row=1, column=1)

tk.Label(right_frame, text='anxiety', font=('TkDefaultFont', 20),background="#7792DD").grid(row=2, column=0)
anxiety_entry = tk.Entry(right_frame, font=('TkDefaultFont', 20),background="#92A8E4")
anxiety_entry.grid(row=2, column=1)



# 创建列表框
activity_listbox = tk.Listbox(left_frame, font=('TkDefaultFont', 20),background="#92A8E4")
activity_listbox.grid(row=5, column=0, columnspan=2, pady=10)

# 添加活动名称到列表框
for activity_name in activity:
    activity_listbox.insert('end', activity_name)

# 创建标签用于显示信息
activity_info_label = tk.Label(left_frame, text='', font=('TkDefaultFont', 20),background="#7792DD")
activity_info_label.grid(row=6, column=0, columnspan=2, pady=10)

# 定义按钮点击事件
def show_activity_info():
    # 获取当前选中的活动名称
    selected_activity = activity_listbox.get(activity_listbox.curselection())

    # 获取活动信息
    activity_1time_imit = activity[selected_activity]['1time_imit']
    activity_Ttime_imit = activity[selected_activity]['Ttime_imit']
    activity_tips = activity[selected_activity]['tips']

    # 显示活动信息
    activity_info_label.config(text='推荐单次时长是：' + str(activity_1time_imit) + '\n推荐总时长是：' + str(activity_Ttime_imit) + '\n注意：' + activity_tips)

# 创建按钮
show_activity_info_button = tk.Button(left_frame, text='显示提醒', font=('TkDefaultFont', 20), command=show_activity_info,background="#B4C2EC")
show_activity_info_button.grid(row=7, column=0, columnspan=2, pady=10)


# 创建标签用于显示信息
message_label = tk.Label(right_frame, text='', font=('TkDefaultFont', 20),background="#7792DD")
message_label.grid(row=7, column=0, columnspan=2, pady=10)



# 定义按钮点击事件
def show_activities():
    # 获取当前焦虑值
    anxiety_value = float(anxiety_entry.get())
    energy_value = float(energy_entry.get())
    working_value = float(working_entry.get())
    if anxiety_value < 1 or anxiety_value > 5 or energy_value < 1 or energy_value > 5 or working_value < 1 or working_value > 5:
        message_label.config(text='Please enter a number between 1 and 5')
        return

    # 根据条件显示信息
    if working_value >= 3.5:
        message_label.config(text='及时小结 建模 灵活 定时定目标 休息！')
    else:
        if anxiety_value >= 3:
            if energy_value >= 3.5:
                message_label.config(text='慢跑一圈 俯卧撑 仰起 跳远 丢沙包等\n ＞=10min 结束后重新实测')
            elif energy_value >= 2:
                message_label.config(text='散步 简单活动身体 结束后重新实测')
            else:
                message_label.config(text='找个地方躺着/靠着  冥想/睡觉 \n（不听 不看 除非是冥想引导音频） 结束后重新实测')
        else:
            if energy_value >=3.5:
                message_label.config(text='慢跑一圈 俯卧撑 仰起 跳远 丢沙包等\n 结束后继续working')
            else:
                message_label.config(text='听歌（no watching~）or 散步/简单活动身体\n 结束后继续working')

# 创建按钮
button = tk.Button(right_frame, text='显示信息', font=('TkDefaultFont', 20), command=show_activities,background="#B4C2EC")
button.grid(row=4,column=0, columnspan=2, pady=10)
                
# 运行窗口
root.mainloop()
