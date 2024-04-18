# 打印出 新打开的进程名称 
import wmi

c = wmi.WMI()

watcher = c.Win32_Process.watch_for("creation")

while True:
    new_process = watcher()
    print(new_process.Caption)