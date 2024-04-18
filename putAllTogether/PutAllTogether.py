import subprocess
import tkinter as tk
import json
# To make the child and main windows twice bigger, and the text twice bigger, add the following code after the create_widgets method:


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("1200x400") # set the size of the main window to 800x400
        self.master.title("自制程序集合~")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file_listbox = tk.Listbox(self,width=60)
        self.file_listbox.pack(side="left", fill="both", expand=True)
        self.file_listbox.config(font=("TkDefaultFont", 20)) # set the font size of the listbox to 20


        self.launch_button = tk.Button(self)
        self.launch_button["text"] = "启动"
        self.launch_button["command"] = self.launch_selected_file
        self.launch_button.pack(side="right")

        self.edit_button = tk.Button(self)
        self.edit_button["text"] = "修改"
        self.edit_button["command"] = self.edit_selected_file
        self.edit_button.pack(side="right")

    def launch_selected_file(self):
        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        subprocess.run(selected_file)

    def edit_selected_file(self):
        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        edit_window = tk.Toplevel(self)
        edit_window.title("修改文件")
        edit_window.geometry("600x400") # set the size of the child window to 400x200

        edit_label = tk.Label(edit_window, text="点击修改")
        edit_label.pack(side="left")
        edit_label.config(font=("TkDefaultFont", 20))

        edit_entry = tk.Entry(edit_window, width=40)
        edit_entry.insert("end", selected_file)
        edit_entry.config(font=("TkDefaultFont", 20))
        edit_entry.pack(side="top")


        save_button = tk.Button(edit_window, text="保存", command=lambda: self.save_edited_file(selected_file, edit_entry.get()))
        save_button.pack(side="right")

    def save_edited_file(self, old_file_name, new_file_name):
        index = self.file_listbox.get(0, "end").index(old_file_name)
        self.file_listbox.delete(index)
        self.file_listbox.insert(index, new_file_name)
        self.file_listbox.selection_clear(0, "end")
        self.file_listbox.selection_set(index)
        self.file_listbox.activate(index)

        file_names = self.file_listbox.get(0, "end")
        with open("file_names.json", "w") as f:
            json.dump(file_names, f)

root = tk.Tk()
app = Application(master=root)



try:
    with open("file_names.json", "r") as f:
        file_names = json.load(f)
        for file_name in file_names:
            app.file_listbox.insert("end", file_name)
except FileNotFoundError:
    pass

app.mainloop()
