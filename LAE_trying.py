import tkinter as tk
import time

def show_rest_window(remind):
    rest_window = tk.Toplevel()
    rest_window.title("Rest Time!")
    rest_window.geometry("300x200+500+300") # set size and position of window
    rest_label = tk.Label(rest_window, text=f"{selected_message}\n{remind}", font=("TkDefaultFont", 20, "bold"))# set font size and color
    rest_label.pack()

def start_timer():
    t_value = int(float(entry.get()) * 60) # convert minutes to seconds
    remind = remind_entry.get()
    time.sleep(t_value)
    show_rest_window(remind)

# create main window
main_window = tk.Tk()
main_window.title("Timer")

# create label and entry for inputting time
time_label = tk.Label(main_window, text="Enter time in minutes:")
time_label.pack()
entry = tk.Entry(main_window)
entry.pack()

# create label and entry for inputting remind
remind_label = tk.Label(main_window, text="Enter reminder:")
remind_label.pack()
remind_entry = tk.Entry(main_window)
remind_entry.pack()

# create button to start timer
start_button = tk.Button(main_window, text="Start Timer", command=start_timer)
start_button.pack()

# create listbox
message_choices = ["how are you?", "开心呢", "aodihsaio"]
list_box = tk.Listbox(main_window)
for message in message_choices:
    list_box.insert(tk.END, message)
list_box.pack()

selected_index = list_box.curselection()[0]
selected_message = message_choices[selected_index]

main_window.mainloop()
