# create a list "reminder_list", each member of the list stands for a "reminder". every member has severl attributes, first is the name, second is the time, third is the content. when the program starts, it create a mainwindow, which has a list box displaying the names(first attributes) of the members in reminder_list. the program also use threading to perform the "remind on time" function: once the current time is the same to a time recorded in reminder_list, the function will pops up a child window, which displays the information of that member's third attribute(content).import threading
import time
import tkinter as tk
import threading

# create a list "reminder_list", each member of the list stands for a "reminder". 
# every member has several attributes, first is the name, second is the time, third is the content.
reminder_list = [("Reminder 1", "15:45", "Content 1"), ("Reminder 2", "15:46", "Content 2"),("Reminder 3", "15:55", "Content 3"),("Reminder 4", "15:45", "Content 4"),("Reminder 5", "15:45", "Content 5")]

# function to check if it's time to remind
def check_reminder():
    current_time = time.strftime("%H:%M")
    for reminder in reminder_list:
        if reminder[1] == current_time:
            # pops up a child window, which displays the information of that member's third attribute(content)
            child_window = tk.Toplevel()
            child_window.title(reminder[0])
            child_window.geometry("200x100")
            content_label = tk.Label(child_window, text=reminder[2])
            content_label.grid()
    # check every minute
    threading.Timer(60, check_reminder).start()

# create a mainwindow, which has a list box displaying the names(first attributes) of the members in reminder_list
root = tk.Tk()
root.title("Reminder List")
root.geometry("600x800")

# create a frame to hold the listbox and the reminder_info_label
frame = tk.Frame(root)
frame.pack()

# put the listbox on the left
listbox = tk.Listbox(frame)
for reminder in reminder_list:
    listbox.insert(tk.END, reminder[0])
listbox.pack(side=tk.LEFT)

# put the reminder_info_label on the right
reminder_info_label = tk.Label(frame, text="")
reminder_info_label.pack(side=tk.RIGHT)

# add event binding to update the reminder_info_label
def update_reminder_info(event):
    # get the selected reminder from the listbox
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        selected_reminder = reminder_list[selected_index]
        # update the reminder_info_label with the time and content of the selected reminder
        reminder_info_label.config(text=f"Time: {selected_reminder[1]}\nContent: {selected_reminder[2]}")

listbox.bind("<<ListboxSelect>>", update_reminder_info)

# start the reminder checking function in a separate thread
threading.Thread(target=check_reminder).start()

# start the main loop
root.mainloop()





# 子窗口可以出来 但是……会有一分钟的误差 哈哈哈哈
# 第二次的优化add a new function to the main window. if the user choose a reminder's name on the list box, 
# next to it there is a new area where the time and the content of that reminder will be displayed.