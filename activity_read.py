
import pandas as pd
import tkinter as tk

# read data from activity_base.xlsx
activity_data = pd.read_excel('activity_base.xlsx')

# assign data to activity
activity = {}
for i in range(len(activity_data)):
    activity_name = activity_data.iloc[i, 0]
    activity_1time_imit = activity_data.iloc[i, 1]
    activity_Ttime_imit = activity_data.iloc[i, 2]
    activity_tips = activity_data.iloc[i, 3]
    activity[activity_name] = {'1time_imit': activity_1time_imit, 'Ttime_imit': activity_Ttime_imit, 'tips': activity_tips}

# create main window
window = tk.Tk()
window.title("Activity Reminder")

# create list box on the left
listbox = tk.Listbox(window)
for name in activity.keys():
    listbox.insert(tk.END, name)
listbox.pack(side=tk.LEFT)

# create area for showing information on the right
info_area = tk.Frame(window)
info_area.pack(side=tk.LEFT, padx=20)

# function to show reminder
def show_reminder():
    # clear previous information
    for widget in info_area.winfo_children():
        widget.destroy()
    # get selected activity
    selected_activity = listbox.get(listbox.curselection())
    # get information related to selected activity
    selected_activity_info = activity[selected_activity]
    # create labels to display information
    label1 = tk.Label(info_area, text=f"推荐单次时长是：{selected_activity_info['1time_imit']}")
    label1.pack()
    label2 = tk.Label(info_area, text=f"推荐总时长是：{selected_activity_info['Ttime_imit']}")
    label2.pack()
    label3 = tk.Label(info_area, text=f"注意：{selected_activity_info['tips']}")
    label3.pack()

# create button to show reminder
button = tk.Button(window, text="Show Reminder", command=show_reminder)
button.pack()

window.mainloop()





# 第一次的要求please write a program, the function is: 1. it can read the data from activity_base.xlsx , the first row is the Chinese names of the column variables. 2. assign the data from the file to "activity", details: the content of the first column of the data is activity.name, second column is activity.1time_imit, follow this pattern, then activity.Ttime_imit and activity.tips. print the content of activity in the end.

# 第二次： please modify the function. create a main window, which has a list box on the left, and a area for showing information later on the right. In the list box, it displays the names of the activity(show the content of activity_name).the user choose one activity from it, and click the button below(named:"show reminder"). and the information related will be displayed on the right area: from the top to the bottom, it shows :"推荐单次时长是：": activity_1time_imit; "推荐总时长是：": activity_Ttime_imit;"注意：":activity_tips.    after this, user can choose another activity to see a another set of information(which means the function can run repeatedly).

#第三次 when I choose to see a another activity, the information shown previously didn't disappear. please make it refresh the information area before show new information.