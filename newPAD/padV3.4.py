import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter import END
import json
import re


# 读取md文件
with open(r'D:\学习and学校\obsidian\qiluo\00-MOC\pad_content.md','r',encoding='utf-8') as f:
    text = f.read()

''' 从md中读取 mainline'''

mainline = {}
Mname_pattern = re.compile(r'M{}【(.*?)】'.format(1))
Mlocation_pattern = re.compile(r'M{}【(.*?)】'.format(2))
Mdate_pattern = re.compile(r'M{}【(.*?)】'.format(3))
Mname_match = Mname_pattern.search(text)
Mlocation_match = Mlocation_pattern.search(text)
Mdate_match = Mdate_pattern.search(text)
mainline['name'] = Mname_match.group(1)
mainline['location'] = Mlocation_match.group(1)
mainline['date'] = Mdate_match.group(1)

# 从md中读取 sidelines
sidelines = {}
for i in range(1, 9):
    sideline = {}
    name_pattern = re.compile(r'{}1【(.*?)】'.format(i))
    location_pattern = re.compile(r'{}2【(.*?)】'.format(i))
    date_pattern = re.compile(r'{}3【(.*?)】'.format(i))

    name_match = name_pattern.search(text)
    location_match = location_pattern.search(text)
    date_match = date_pattern.search(text)

    if name_match:
        sideline['name'] = name_match.group(1)
    else:
        print('No match found for name of sideline{}'.format(i))

    if location_match:
        sideline['location'] = location_match.group(1)
    else:
        print('No match found for location of sideline{}'.format(i))

    if date_match:
        sideline['date'] = date_match.group(1)
    else:
        print('No match found for date of sideline{}'.format(i))

    sidelines['sideline{}'.format(i)] = sideline



# Create the main window
root = tk.Tk()
root.title("PAD")
root.geometry("1200x800")

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


''' 看这里看这里看这里！！
'''
# Create a Scrollbar and a Text widget for sidelines
sideline_scrollbar = tk.Scrollbar(right_frame)
sideline_scrollbar.grid(row=5, column=2, rowspan=4, sticky=tk.N+tk.S)
sideline_text_widget = tk.Text(right_frame, wrap=tk.WORD, yscrollcommand=sideline_scrollbar.set, width=50, height=30, font=("TkDefaultFont", 16), fg="darkblue")
sideline_text_widget.grid(row=5, column=0, rowspan=4, padx=10, pady=10, sticky="w")

# Add sideline names and details to the Text widget
for i in range(1,9):
    sideline=sidelines['sideline{}'.format(i)] 
    sideline_details = f"Name: {sideline['name']}\nLocation: {sideline['location']}\nDate: {sideline['date']}\n\n"
    sideline_text_widget.insert(tk.END, sideline_details)

# Configure the Scrollbar to work with the Text widget
sideline_scrollbar.config(command=sideline_text_widget.yview)



# Create a function to handle the selection of a sideline
def select_sideline(event):
    # Get the index of the selected line
    index = sideline_text_widget.index(tk.CURRENT)
    # Get the name of the selected sideline
    name = sideline_text_widget.get(index + "linestart", index + "lineend")
    # Do something with the selected sideline
    print(f"Selected sideline: {name}")

# Bind the Text widget to the select_sideline function
sideline_text_widget.bind("<Button-1>", select_sideline)








# Position the frames in the main window
left_frame.pack(side="left", fill="both", expand=True)
right_frame.pack(side="left", fill="both", expand=True)




# at the right frame,add labels to show attributes of the side_lide and the mainline. details are as followed:
# at the upper area, add 3 labels to display attributes of mainline: name,location and date from up to bottom accordingly.
# at the lower area, add 5 message widgets to display attributes of the 5 sidelines.  put line feed between different attributes within the same widget.

# Create labels to display the attributes of the mainline
mainline_name_label = tk.Label(right_frame, text="Name: " + mainline["name"], fg="#EF7228", font=("TkDefaultFont", 16))
mainline_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
mainline_name_label.configure(fg="#7c511a")

mainline_location_label = tk.Label(right_frame, text="Location: " + mainline["location"], fg="#EF7228", font=("TkDefaultFont", 16))
mainline_location_label.configure(fg="#7c511a")
mainline_location_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")


mainline_date_label = tk.Label(right_frame, text="Date: " + mainline["date"], fg="#EF7228", font=("TkDefaultFont", 16))
mainline_date_label.configure(fg="#7c511a")
mainline_date_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")


# at the left frame:
# create a variable named"words".
# then below the time lable,insert a label displayed the content of "words".


'''# WORDS!!!'''
words_value = ""
words_pattern = re.compile(r'W【(.*?)】')
words_match = words_pattern.search(text)
words_value = words_match.group(1)


# Assign the value of words
words = tk.StringVar(value=words_value)

# Create a label to display the content of "words"
words_label = tk.Label(left_frame, textvariable=words, font=("TkDefaultFont", 12))
words_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

'''rules'''


# 从md中读取 rules
rules = {}
for i in range(1, 9):
    rule = {}
    content_pattern = re.compile(r'r{}1【(.*?)】'.format(i))
    area_pattern = re.compile(r'r{}2【(.*?)】'.format(i))


    content_match = content_pattern.search(text)
    area_match = area_pattern.search(text)
    rule['content'] = content_match.group(1)
    rule['area'] = area_match.group(1)

    rules['rule{}'.format(i)] = rule




rules_scrollbar = tk.Scrollbar(left_frame)
rules_scrollbar.grid(row=5, column=2, rowspan=4, sticky=tk.N+tk.S)
rules_text_widget = tk.Text(left_frame, wrap=tk.WORD, yscrollcommand=rules_scrollbar.set, width=50, height=20, font=("TkDefaultFont", 16))
rules_text_widget.configure(fg="#7c511a")
rules_text_widget.grid(row=5, column=0, rowspan=4, padx=10, pady=10, sticky="w")


# Add sideline names and details to the Text widget
for i in range(1,9):
    rule=rules['rule{}'.format(i)] 
    rule_details = f"{rule['content']}\narea: {rule['area']}\n\n"
    rules_text_widget.insert(tk.END, rule_details)

# Configure the Scrollbar to work with the Text widget
sideline_scrollbar.config(command=rules_text_widget.yview)






# Start the main loop
root.mainloop()




# 啊啊啊啊啊烦死了 怎么会这样 只能写个小程序了
