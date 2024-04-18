import tkinter as tk
import time
from tkinter import messagebox

class A0:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("A0")

        #创建输入框，标签和按钮。
        self.activity_label = tk.Label(self.root, text="输入您的活动:")
        self.activity_label.pack()
        self.activity_entry = tk.Entry(self.root, width=30)
        self.activity_entry.pack()

        self.time_label = tk.Label(self.root, text="输入您的时间(分钟):")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.root, width=30)
        self.time_entry.pack()

        self.message_label = tk.Label(self.root, text="输入您的消息:")
        self.message_label.pack()
        self.message_entry = tk.Entry(self.root, width=30)
        self.message_entry.pack()

        self.submit_button = tk.Button(self.root, text="提交", command=self.submit)
        self.submit_button.pack()

        self.root.mainloop()

    def submit(self):
        #获取输入值并验证时间格式是否正确
        activity = self.activity_entry.get()
        time_string = self.time_entry.get()
        message = self.message_entry.get()

        if not activity or not message:
            #如果没有输入活动或消息，提示用户是否确认使用空白信息
            confirm = messagebox.askyesno(title="确认信息", message="您没有输入活动或消息，是否继续?")
            if confirm:
                activity = " "
                message = " "
            else:
                return

        try:
            time_in_minutes = int(time_string)
            if time_in_minutes <= 0 or time_in_minutes > 1440:
                #时间必须大于0小于1440(24小时)
                raise ValueError
        except ValueError:
            messagebox.showerror(title="错误", message="时间输入错误，请输入1到1440之间的整数。")
            return

        #转换为秒数
        time_in_seconds = time_in_minutes * 60
        self.countdown(activity, time_in_seconds, message)

    def countdown(self, activity, remaining_time, message):
        #创建消息框
        message_box = tk.Toplevel(self.root)
        message_box.title("提醒")

        #创建消息文本和确认按钮
        message_label = tk.Label(message_box, text=message)
        message_label.pack()

        confirm_button = tk.Button(message_box, text="我知道了", command=lambda:self.confirm(message_box))
        confirm_button.pack()

        #开始倒计时
        while remaining_time > 0:
            time.sleep(1)
            remaining_time -= 1

        #时间到了，激活锁屏
        self.lock_screen()

    def confirm(self, message_box):
        #关闭消息框
        message_box.destroy()

    def lock_screen(self):
        #激活锁屏
        pass

#运行程序
A0()
