import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter import END
import json


data = {}
try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    pass

mainline = data.get("mainline", {"name": "Mainline", "location": "Main Location", "date": "Main Date"})
side_line = data.get("side_line", [
    {"name": "Sideline 1", "location": "Location 1", "date": "Date 1"},
    {"name": "Sideline 2", "location": "Location 2", "date": "Date 2"},
    {"name": "Sideline 3", "location": "Location 3", "date": "Date 3"},
    {"name": "Sideline 4", "location": "Location 4", "date": "Date 4"},
    {"name": "Sideline 5", "location": "Location 5", "date": "Date 5"}
])






# Create the main window
root = tk.Tk()
root.title("PAD")
root.geometry("600x800")

# Create two frames
left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True)
right_frame = tk.Frame(root)
right_frame.pack(side="left", fill="both", expand=True)

# Load the image
image_path = "pic.jpg"  # Modify this to the path of your image
try:
    image = Image.open(image_path)
except FileNotFoundError:
    # Handle file not found error
    tk.messagebox.showwarning("Error", "Image file not found. Please try again.")
    root.destroy()
    exit()

# Resize the image
width, height = image.size
new_width, new_height = 250, 300  # Modify these values to adjust the size of the image
if width > new_width or height > new_height:
    ratio = min(new_width/width, new_height/height)
    image = image.resize((int(width*ratio), int(height*ratio)), Image.LANCZOS)

# Create a label to display the image
image_tk = ImageTk.PhotoImage(image)
label = tk.Label(left_frame, image=image_tk)
label.grid(row=0, column=0, padx=10, pady=10)

# Create a label to display the current time
time_label = tk.Label(left_frame, text=time.strftime("%Y.%m.%d"), font=("Arial", 16))
time_label.grid(row=1, column=0, padx=10, pady=10)





# Create an empty list to hold the sideline message widgets
sideline_message_widgets = []

# Create message widgets to display the attributes of the side_line
for i, sideline in enumerate(side_line):
    sideline_message = f"Name: {sideline['name']}\nLocation: {sideline['location']}\nDate: {sideline['date']}"
    sideline_message_widget = tk.Message(right_frame, text=sideline_message, width=200, fg="#87CEFA", font=("TkDefaultFont", 16))
    sideline_message_widget.grid(row=i+3, column=0, padx=10, pady=10, sticky="w")
    sideline_message_widgets.append(sideline_message_widget)



def change_mainline():
    # Create a child window
    child_window = tk.Toplevel(root)
    child_window.title("修改主线")

    # Create labels and entry widgets to allow the user to change the attributes of the mainline
    name_label = tk.Label(child_window, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(child_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)
    name_entry.insert(0, mainline["name"])

    location_label = tk.Label(child_window, text="Location:")
    location_label.grid(row=1, column=0, padx=10, pady=10)
    location_entry = tk.Entry(child_window)
    location_entry.grid(row=1, column=1, padx=10, pady=10)
    location_entry.insert(0, mainline["location"])

    date_label = tk.Label(child_window, text="Date:")
    date_label.grid(row=2, column=0, padx=10, pady=10)
    date_entry = tk.Entry(child_window)
    date_entry.grid(row=2, column=1, padx=10, pady=10)
    date_entry.insert(0, mainline["date"])

    # Create a function to update the attributes of the mainline
    def update_mainline():
        mainline["name"] = name_entry.get()
        mainline["location"] = location_entry.get()
        mainline["date"] = date_entry.get()
        mainline_name_label.config(text="Name: " + mainline["name"])
        mainline_location_label.config(text="Location: " + mainline["location"])
        mainline_date_label.config(text="Date: " + mainline["date"])
        child_window.destroy()
        with open("data.json", "w") as f:
            data["mainline"] = mainline
            json.dump(data, f)

    # Create an "OK" button to update the attributes of the mainline
    ok_button = tk.Button(child_window, text="OK", command=update_mainline)
    ok_button.grid(row=3, column=1, padx=10, pady=10)

# Add a command to the right_button to call the change_mainline function
right_button = tk.Button(left_frame, text="修改主线", command=change_mainline)
right_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky="w")


def change_sideline():
    # Create a child window
    child_window = tk.Toplevel(root)
    child_window.title("修改支线")

    # Create a listbox to display the names of the sidelines
    listbox = tk.Listbox(child_window)
    for i, sideline in enumerate(side_line):
        listbox.insert(i, sideline["name"])
    listbox.grid(row=0, column=0, padx=10, pady=10)

    # Create labels and entry widgets to allow the user to change the attributes of the selected sideline
    name_label = tk.Label(child_window, text="Name:")
    name_label.grid(row=1, column=0, padx=10, pady=10)
    name_entry = tk.Entry(child_window)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    location_label = tk.Label(child_window, text="Location:")
    location_label.grid(row=2, column=0, padx=10, pady=10)
    location_entry = tk.Entry(child_window)
    location_entry.grid(row=2, column=1, padx=10, pady=10)

    date_label = tk.Label(child_window, text="Date:")
    date_label.grid(row=3, column=0, padx=10, pady=10)
    date_entry = tk.Entry(child_window)
    date_entry.grid(row=3, column=1, padx=10, pady=10)

    # Create a function to update the attributes of the selected sideline
    def update_sideline():
        if listbox.curselection():
            index = listbox.curselection()[0]
            sideline = side_line[index]
            sideline["name"] = name_entry.get()
            sideline["location"] = location_entry.get()
            sideline["date"] = date_entry.get()
            sideline_message_widgets[index].config(text=f"Name: {sideline['name']}\nLocation: {sideline['location']}\nDate: {sideline['date']}")
            child_window.destroy()
            with open("data.json", "w") as f:
                data["side_line"] = side_line
                json.dump(data, f)

    # Create an "OK" button to update the attributes of the selected sideline
    ok_button = tk.Button(child_window, text="OK", command=update_sideline)
    ok_button.grid(row=4, column=1, padx=10, pady=10)

    # Bind the listbox to update the labels and entry widgets when a sideline is selected
    def on_select(event):
        if listbox.curselection():
            index = listbox.curselection()[0]
            sideline = side_line[index]
            name_entry.delete(0, END)
            name_entry.insert(END, sideline["name"])
            location_entry.delete(0, END)
            location_entry.insert(END, sideline["location"])
            date_entry.delete(0, END)
            date_entry.insert(END, sideline["date"])
    listbox.bind("<<ListboxSelect>>", on_select)



# Add commands to the left_button to call the change_sideline function for each sideline
left_button = tk.Button(left_frame, text="修改支线", command=change_sideline)
left_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2, sticky="w")


# Position the frames in the main window
left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="left", fill="both", expand=True)




# at the right frame,add labels to show attributes of the side_lide and the mainline. details are as followed:
# at the upper area, add 3 labels to display attributes of mainline: name,location and date from up to bottom accordingly.
# at the lower area, add 5 message widgets to display attributes of the 5 sidelines.  put line feed between different attributes within the same widget.

# Create labels to display the attributes of the mainline
mainline_name_label = tk.Label(right_frame, text="Name: " + mainline["name"], fg="#EF7228", font=("TkDefaultFont", 16))
mainline_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
mainline_location_label = tk.Label(right_frame, text="Location: " + mainline["location"], fg="#EF7228", font=("TkDefaultFont", 16))
mainline_location_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
mainline_date_label = tk.Label(right_frame, text="Date: " + mainline["date"], fg="#EF7228", font=("TkDefaultFont", 16))
mainline_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")


# at the left frame:
# create a variable named"words".
# then below the time lable,insert a label displayed the content of "words".
# also add a button below the right_button, named "修改今日之言". 
# it pops up a child window , in which  you can change the content of "words",
# the change will be displayed on the mainwindow once you click "ok" button on that child window.
# Create a variable named "words"


# Load the value of words from a json file
with open("data.json", "r") as f:
    data = json.load(f)
    if "words" in data:
        words_value = data["words"]
    else:
        words_value = "" # or any default value you want to assign

# Assign the value of words
words = tk.StringVar(value=words_value)

# Create a label to display the content of "words"
words_label = tk.Label(left_frame, textvariable=words, font=("TkDefaultFont", 12))
words_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

# Create a function to update the content of "words"
def update_words():
    # Create a child window
    child_window = tk.Toplevel(root)
    child_window.title("修改今天的tips~")

    # Create labels and entry widgets to allow the user to change the content of "words"
    words_label = tk.Label(child_window, text="请输入新的内容：")
    words_label.grid(row=0, column=0, padx=10, pady=10)
    words_entry = tk.Entry(child_window)
    words_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create a function to update the content of "words"
    def update():
        words.set(words_entry.get())
        child_window.destroy()

        # Save the value of words to a json file
        with open("data.json", "w") as f:
            data["words"] = words.get()
            json.dump(data, f)

    # Create an "OK" button to update the content of "words"
    ok_button = tk.Button(child_window, text="OK", command=lambda: update())
    ok_button.grid(row=1, column=1, padx=10, pady=10)

# Create a button to call the update_words function
update_button = tk.Button(left_frame, text="修改今天的tips~", command=update_words)
update_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2, sticky="w")



# Start the main loop
root.mainloop()




# 啊啊啊啊啊烦死了 怎么会这样 只能写个小程序了
