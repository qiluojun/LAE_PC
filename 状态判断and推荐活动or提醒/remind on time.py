import tkinter as tk
import datetime
from tkinter import messagebox
import threading

class Reminder:
    def __init__(self, master):
        self.master = master
        self.master.title("Reminder")
        self.master.geometry("800x600")
        
        # default reminder time and message
        self.reminder_time = datetime.time(hour=11)
        self.reminder_message = "嘿嘿嘿"
        
        # create labels and entry widgets for reminder time and message
        tk.Label(self.master, text="Reminder Time (HH:MM)").grid(row=0, column=0, padx=10, pady=10)
        self.time_entry = tk.Entry(self.master)
        self.time_entry.insert(0, self.reminder_time.strftime("%H:%M"))
        self.time_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(self.master, text="Reminder Message").grid(row=1, column=0, padx=10, pady=10)
        self.message_entry = tk.Entry(self.master)
        self.message_entry.insert(0, self.reminder_message)
        self.message_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # create button to update reminder time and message
        tk.Button(self.master, text="Update Reminder", command=self.update_reminder).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
    def update_reminder(self):
        # get reminder time and message from entry widgets
        time_str = self.time_entry.get()
        message_str = self.message_entry.get()
        
        # convert time string to datetime.time object
        try:
            time_obj = datetime.datetime.strptime(time_str, "%H:%M").time()
        except ValueError:
            # handle invalid time format
            tk.messagebox.showerror("Error", "Invalid time format. Please enter time in HH:MM format.")
            return
        
        # update reminder time and message
        self.reminder_time = time_obj
        self.reminder_message = message_str
        
        # show confirmation message
        messagebox.showinfo("Success", "Reminder updated successfully.")
        # schedule reminder to appear at specified time using threading
        now = datetime.datetime.now().time()
        delay = (datetime.datetime.combine(datetime.date.today(), self.reminder_time) - datetime.datetime.combine(datetime.date.today(), now)).total_seconds()
        threading.Timer(delay, self.run).start()
        
    def run(self):
        # create child window for reminder
        self.reminder_window = tk.Toplevel(self.master)
        self.reminder_window.title("Reminder")
        self.reminder_window.geometry("300x200")
        self.reminder_window.attributes('-topmost', True)
        # create label widget with reminder message
        reminder_label = tk.Label(self.reminder_window, text=self.reminder_message,font=("Arial", 20))
        reminder_label.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    reminder = Reminder(root)
    root.mainloop()
        



# 请编写一个程序，运行程序后，会弹出一个主窗口。主窗口的功能是修改稍后子窗口的弹出时间和提醒内容。在未修改的情况下，系统会于11：00弹出一个子窗口，窗口上有提示语：“嘿嘿嘿”。
#主窗口中可以修改子窗口的弹出时间和提醒内容。（通过输入框和按钮来实现）。


# 优化想法：    添加一个及以上的提醒时间和内容预设 修改的时候也可以这么改  改成一个列表 列表成员代表提醒数
# 列表的第一个属性是名称 第二个属性是时间 第三个属性是内容~ 
# 然后主窗口 用list box  呈现名称  点击之后呈现时间 和 内容 可以点击修改时间和内容~
# AI说可以 那就试试！