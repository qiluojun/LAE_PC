# create a list "reminder_list", each member of the list stands for a "reminder". 
# every member has several attributes, first is the name, second is the time, third is the content.
import time
import tkinter as tk
import threading
import json

# create a global variable to store the timer object
reminder_timer = None

reminder_list = [("Reminder 1", "15:45", "Content 1"), ("Reminder 2", "15:46", "Content 2"),("Reminder 3", "15:55", "Content 3"),("Reminder 4", "15:45", "Content 4"),("Reminder 5", "15:45", "Content 5")]

# function to check if it's time to remind
def check_reminder():
    current_time = time.strftime("%H:%M")
    with open('reminders.json', 'r') as f:
        reminder_list = json.load(f)
    for reminder in reminder_list:
        if reminder[1] == current_time:
            # pops up a child window, which displays the information of that member's third attribute(content)
            child_window = tk.Toplevel()
            child_window.title(reminder[0])
            child_window.attributes('-topmost', True)
            child_window.geometry("300x200")
            content_label = tk.Label(child_window, text=reminder[2], font=("TkDefaultFont", 20), fg="blue")
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
root.geometry("600x800")
# add a button to close the program
close_button = tk.Button(root, text="Close", command=on_closing)
close_button.pack()



# load the reminder_list from the JSON file
try:
    with open('reminders.json', 'r') as f:
        reminder_list = json.load(f)
except FileNotFoundError:
    reminder_list = [("Reminder 1", "15:45", "Content 1"), ("Reminder 2", "15:46", "Content 2"),("Reminder 3", "15:55", "Content 3"),("Reminder 4", "15:45", "Content 4"),("Reminder 5", "15:45", "Content 5")]

# create a frame to hold the listbox and the reminder_info_label
frame = tk.Frame(root)
frame.pack()

# put the listbox on the left
listbox = tk.Listbox(frame, font=("TkDefaultFont", 20))
for reminder in reminder_list:
    listbox.insert(tk.END, reminder[0])
listbox.pack(side=tk.LEFT)

# put the reminder_info_label on the right
reminder_info_label = tk.Label(frame, text="", font=("TkDefaultFont", 20))
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

# add a new frame to the left of the existing frame that contains the listbox
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT)

# add a button and three entries for the user to input a new name, time, and content for the selected reminder
new_name_entry = tk.Entry(left_frame, font=("TkDefaultFont", 20))
new_name_entry.pack()
new_time_entry = tk.Entry(left_frame, font=("TkDefaultFont", 20))
new_time_entry.pack()
new_content_entry = tk.Entry(left_frame, font=("TkDefaultFont", 20))
new_content_entry.pack()

def update_reminder():
    # get the selected reminder from the listbox
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        # update the selected reminder with the values entered in the new entries
        reminder_list[selected_index] = (new_name_entry.get(), new_time_entry.get(), new_content_entry.get())
        # update the listbox with the new name of the selected reminder
        listbox.delete(selected_index)
        listbox.insert(selected_index, new_name_entry.get())
        # save the updated reminder_list to a JSON file
        with open('reminders.json', 'w') as f:
            json.dump(reminder_list, f)

update_button = tk.Button(left_frame, text="Update Reminder", command=update_reminder, font=("TkDefaultFont", 20))
update_button.pack()

# start the reminder checking function in a separate thread
reminder_timer = threading.Thread(target=check_reminder)
reminder_timer.start()

# start the main loop
root.mainloop()

# 4.10 优化 