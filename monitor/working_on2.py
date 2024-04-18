'''
this may be the one, but:
有无进一步优化的可能性？ 
1. 比如识别具体的窗口名称 比如赤途的窗口名称 而非只有electron
2. 遗漏了我自己写的小程序？

'''


import psutil

def monitor():
    processes = {}
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'] == 'System Idle Process':
            continue
        if proc.info['name'] == 'taskmgr.exe':
            continue
        if proc.info['pid'] == 0:
            continue
        app_name = proc.info['name'].split('.')[0]
        if app_name not in processes:
            processes[app_name] = proc.info['name']
    for app_name in sorted(processes.keys()):
        print(app_name)



def monitor2():
    processes = {}
    for proc in psutil.process_iter(['name', 'pid']):
        if proc.info['name'] == 'System Idle Process':
            continue
        if proc.info['name'] == 'taskmgr.exe':
            continue
        if proc.info['pid'] == 0:
            continue
        app_name = proc.info['name'].split('.')[0]
        if app_name not in processes:
            processes[app_name] = []
        processes[app_name].append(proc.info['name'])
    for app_name in sorted(processes.keys()):
        print(app_name)
        for process_name in processes[app_name]:
            print('\t', process_name)



import subprocess

cmd = 'powershell \"gps | where {$_.MainWindowTitle } | select Description'
proc = subprocess.Popen (cmd, shell=True, stdout=subprocess.PIPE)

for line in proc.stdout:
    decoded_line = line.decode ('cp936', errors='ignore')
    if not decoded_line [0].isspace ():
        print (decoded_line.rstrip ())

