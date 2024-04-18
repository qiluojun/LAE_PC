import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title('判断程序')

# 创建标签和输入框

tk.Label(root, text='working', font=('TkDefaultFont', 20)).grid(row=0, column=0)
working_entry = tk.Entry(root, font=('TkDefaultFont', 20))
working_entry.grid(row=0, column=1)

tk.Label(root, text='energy', font=('TkDefaultFont', 20)).grid(row=1, column=0)
energy_entry = tk.Entry(root, font=('TkDefaultFont', 20))
energy_entry.grid(row=1, column=1)


tk.Label(root, text='anxiety', font=('TkDefaultFont', 20)).grid(row=2, column=0)
anxiety_entry = tk.Entry(root, font=('TkDefaultFont', 20))
anxiety_entry.grid(row=2, column=1)

# 创建标签用于显示信息
message_label = tk.Label(root, text='', font=('TkDefaultFont', 20))
message_label.grid(row=3, column=0, columnspan=2)


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
                message_label.config(text='慢跑一圈 俯卧撑 仰起 跳远 丢沙包等 ＞=10min 结束后重新实测')
            elif energy_value >= 2:
                message_label.config(text='散步 简单活动身体 结束后重新实测')
            else:
                message_label.config(text='找个地方躺着/靠着  冥想/睡觉 （不听 不看 除非是冥想引导音频） 结束后重新实测')
        else:
            if energy_value >=3.5:
                message_label.config(text='慢跑一圈 俯卧撑 仰起 跳远 丢沙包等 结束后继续working')
            else:
                message_label.config(text='听歌（no watching~）or 散步/简单活动身体 结束后继续working')


# 创建按钮
button = tk.Button(root, text='显示信息', font=('TkDefaultFont', 20), command=show_activities)
button.grid(row=4, column=0, columnspan=2)

# 运行窗口
root.mainloop()