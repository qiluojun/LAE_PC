import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import messagebox
import pandas as pd

# 创建一个 Tkinter 窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

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

while True:
    dlg = InputDialog(root, "请输入焦虑值（1-5）：")
    if dlg.result is None:
        break
    if dlg.result <= 0 or dlg.result >5 :
        messagebox.showerror("错误", "请输入1-5的值！")
    elif dlg.result < 3:
        messagebox.showinfo("正常", "你好~")
        break
    else:
        messagebox.showwarning("警告", "请立刻执行 \ndeep breathe loop!")
        messagebox.showwarning("步骤1", "请立刻停止相关行动，并且深呼吸")
        messagebox.showwarning("步骤2", "请立刻远离屏幕，直到身心状态恢复到一定程度后再返回")
        #怎么样调大字号 以及 加粗 以及换行？
        messagebox.showwarning("步骤3", "请进行判断：体力值/不适度如何？\n ①立刻休息方式运动 远离所有电子屏幕 包括音乐\n ②开始尝试最抗拒拖延的活动 5min！ 然后再对活动进行计划设定目标~")
# 生成 Excel 表格
if messagebox.askyesno("输入值记录", "是否记录本次焦虑值？"):
    try:
        df = pd.read_excel("焦虑值历史记录.xlsx")
    except:
        df = pd.DataFrame(columns=["输入时间", "焦虑值"])
    df = df.append({"输入时间": pd.Timestamp.now(), "焦虑值": dlg.result}, ignore_index=True)
    df.to_excel("焦虑值历史记录.xlsx", index=False)

root.destroy()  # 关闭窗口
