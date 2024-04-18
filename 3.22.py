import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import messagebox
import pandas as pd




# 创建一个 Tkinter 窗口
root = tk.Tk()
root.title('焦虑状况判断程序') 
root.geometry('380x380')
#root.withdraw()  # 隐藏主窗口

# 提示输入框
class InputDialog(sd.Dialog):
    def body(self, master):
        tk.Label(master, text="请输入焦虑值（1-5）：").grid(row=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)
        return self.entry

    def validate(self):
        try:
            self.result = float(self.entry.get())
            return True
        except ValueError:
            messagebox.showerror("错误", "请输入数字！")
            return False

def warning1():#还好
    messagebox.showwarning("步骤1", "请立刻停止相关行动，闭上眼睛，并且深呼吸至少五次")
    messagebox.showwarning("步骤2", "你目前最抗拒焦虑的事情是什么？")
    messagebox.showwarning("步骤3", "请尝试进行五分钟，尝试之后 再进行反馈和相应的用时计划等")
def warning2():#累
    messagebox.showwarning("步骤1", "请立刻停止相关行动，闭上眼睛，并且深呼吸至少五次")
    messagebox.showwarning("步骤2", "请远离电子屏幕，选择：运动＞散步＞坐着吹风/冥想 至少10min")

while True:
    dlg = InputDialog(root, "请输入焦虑值（1-5）：")
    if dlg.result <= 0 or dlg.result >5 :
        messagebox.showerror("错误", "请输入1-5的值！")
    elif dlg.result < 3:
        messagebox.showinfo("正常", "你好~")
        break
    else:
        warning_label = tk.Label(root, text="请立刻执行 deep breathe loop!\n请在3分钟内完成。",
                     font=("Arial", 20), fg="blue")
        warning_label.pack(pady=30)
        # 添加一个 OK 按钮
        ok1_button = tk.Button(root, text="还好", command=warning1)
        ok1_button.pack(side='left')
        ok1_button.pack()
        ok2_button = tk.Button(root, text="累", command=warning2)
        ok2_button.pack(side='left')
        ok2_button.pack()
        

# 生成 Excel 表格
if messagebox.askyesno("输入值记录", "是否记录本次焦虑值？"):
    try:
        df = pd.read_excel("焦虑值历史记录.xlsx")
    except:
        df = pd.DataFrame(columns=["输入时间", "焦虑值"])
        df = df.append({"输入时间": pd.Timestamp.now(), "焦虑值": dlg.result}, ignore_index=True)
        df.to_excel("焦虑值历史记录.xlsx", index=False)

root.destroy()  # 关闭窗口



