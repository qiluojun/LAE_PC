
import time
import tkinter as tk
from tkinter import END
import threading
import re

## 从md中读取reminder的数据
with open(r'D:\学习and学校\obsidian\qiluo\00-MOC\timeline.md','r',encoding='utf-8') as f:
    reminder_text = f.read()


# 读取md文件
with open(r'D:\学习and学校\obsidian\qiluo\00-MOC\timeline.md','r',encoding='utf-8') as f:
    linee= f.readlines()
    a=len(linee)

# 从md中读取 sidelines
reminders = {}
for i in range(1, a+1):
    reminder = {}
    name_pattern = re.compile(r'{}1【(.*?)】'.format(i))
    location_pattern = re.compile(r'{}2【(.*?)】'.format(i))
    time_pattern = re.compile(r'{}3【(.*?)】'.format(i))

    name_match = name_pattern.search(reminder_text)
    location_match = location_pattern.search(reminder_text)
    time_match = time_pattern.search(reminder_text)

    if name_match:
        reminder['name'] = name_match.group(1)
    else:
        print('No match found for name of reminder{}'.format(i))

    if location_match:
        reminder['location'] = location_match.group(1)
    else:
        print('No match found for location of reminder{}'.format(i))

    if time_match:
        reminder['time'] = time_match.group(1)
    else:
        print('No match found for date of reminder{}'.format(i))
    reminders['reminder{}'.format(i)] = reminder












# create a global variable to store the timer object
reminder_timer = None

#reminder_list = [("Reminder 1", "15:45", "Content 1"), ("Reminder 2", "15:46", "Content 2"),("Reminder 3", "15:55", "Content 3"),("Reminder 4", "15:45", "Content 4"),("Reminder 5", "15:45", "Content 5")]

# function to check if it's time to remind
def check_reminder():
    current_time = time.strftime("%H:%M")
    #with open('reminders.json', 'r') as f:
        #reminder_list = json.load(f)
    for i in range(1,a+1):
        reminder=reminders['reminder{}'.format(i)]
        if reminder['time'] == current_time:
            # pops up a child window, which displays the information of that member's third attribute(content)
            child_window = tk.Toplevel()
            child_window.title(reminder['name'])
            child_window.attributes('-topmost', True)
            child_window.geometry("300x200")
            content_label = tk.Label(child_window, text=reminder['location'], font=("TkDefaultFont", 20), fg="blue")
            content_label.grid()
    # check every minute
    # start the timer again
    global reminder_timer
    reminder_timer = threading.Timer(60, check_reminder)
    reminder_timer.start()


def on_closing():
    # stop the reminder_timer thread
    global reminder_timer
    if reminder_timer:
        reminder_timer.cancel()
    # destroy the root window
    root.destroy()


# create a mainwindow, which has a list box displaying the names(first attributes) of the members in reminder_list
root = tk.Tk()
root.title("Reminder List")
root.geometry("1000x500")
# add a button to close the program
close_button = tk.Button(root, text="Close", command=on_closing)
close_button.pack()




# create a frame to hold the listbox and the reminder_info_label
frame = tk.Frame(root)
frame.pack()

# put the listbox on the left
listbox = tk.Listbox(frame, font=("TkDefaultFont", 20))
for i in range(1,a+1):
    reminder=reminders['reminder{}'.format(i)]
    listbox.insert(tk.END, reminder['name'])
listbox.pack(side=tk.LEFT)

# put the reminder_info_label on the right
reminder_info_label = tk.Label(frame, text="", font=("TkDefaultFont", 20))
reminder_info_label.pack(side=tk.RIGHT)

# add event binding to update the reminder_info_label
def update_reminder_info(event):
    # get the selected reminder from the listbox
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0]+1)
        selected_reminder = reminders['reminder{}'.format(selected_index)]
        # update the reminder_info_label with the time and content of the selected reminder
        reminder_info_label.config(text=f"time: {selected_reminder['time']}\nlocation: {selected_reminder['location']}")
listbox.bind("<<ListboxSelect>>", update_reminder_info)

# add a new frame to the left of the existing frame that contains the listbox
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT)

# start the reminder checking function in a separate thread
reminder_timer = threading.Thread(target=check_reminder)
reminder_timer.start()

# start the main loop
root.mainloop()
