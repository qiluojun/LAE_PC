import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter import END
import re

with open(r'D:\学习and学校\obsidian\qiluo\03-Projects\01-自由探索\02-搞事情\LAE\test.md','r',encoding='utf-8') as f:
    text = f.read()
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


# Create a tkinter window
window = tk.Tk()
window.title("Sideline Names")
window.geometry("300x300")

# Create a Scrollbar and a Text widget
scrollbar = tk.Scrollbar(window)
text_widget = tk.Text(window, wrap=tk.WORD, yscrollcommand=scrollbar.set)

# Use the grid method to position the widgets
scrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
text_widget.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

# Add sideline names to the Text widget
for sideline_key, sideline_value in sidelines.items():
    name = sideline_value.get('name', 'No name found')
    text_widget.insert(tk.END, name + '\n')

# Configure the Scrollbar to work with the Text widget
scrollbar.config(command=text_widget.yview)


print(sidelines)

# Start the tkinter event loop
window.mainloop()