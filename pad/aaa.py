import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import time
from tkinter import END

# create a variable named"words".
# insert a label displayed the content of "words".
# also add a button below it, named "修改今日之言". 
# it pops up a child window , in which  you can change the content of "words",
# the change will be displayed on the mainwindow once you click "ok" button on that child window.import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Picture Display")
root.geometry("600x800")
# create a StringVar object named "words_var"
words_var = tk.StringVar(value="Hello World!")

# insert a label displayed the content of "words_var"
label = tk.Label(root, textvariable=words_var)
label.pack()

# also add a button below it, named "修改今日之言"
def change_words():
    # create a child window
    child_window = tk.Toplevel(root)
    child_window.title("修改今日之言")
    
    # add a label and an entry widget to the child window
    label = tk.Label(child_window, text="请输入新的内容：")
    label.pack()
    entry = tk.Entry(child_window)
    entry.pack()
    
    # add a button to the child window
    def update_words():
        # update the value of "words_var"
        words_var.set(entry.get())
        # close the child window
        child_window.destroy()
    button = tk.Button(child_window, text="确定", command=update_words)
    button.pack()

button = tk.Button(root, text="修改今日之言", command=change_words)
button.pack()

root.mainloop()