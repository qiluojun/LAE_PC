
'''
这个可以用欸！ 我只要把这个稍微和 2 结合一下 看能不能有windowtitle的时候输出title 否则输出maintitle！
import subprocess

cmd = 'powershell \"gps | where {$_.MainWindowTitle -or $_.Description } | where {$_.MainWindowHandle -ne 0} | select Description, ProcessName | Sort-Object ProcessName | Select-Object -Unique ProcessName"'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in proc.stdout:
    decoded_line = line.decode('cp936', errors='ignore')
    if not decoded_line[0].isspace():
        print(decoded_line.rstrip())
        
     

'''    

''' 
   
介个！是我目前最喜欢的版本！最最最详细！而且全！是windowtiltle 但是有好多不需要的端码号啥的？
import win32gui

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

win32gui.EnumWindows( winEnumHandler, None )
'''




from pywinauto import Application, Desktop

import time




#time.sleep(3)


def get_current_window():

    # 获取所有前台窗口的名称
    windows = Desktop(backend="uia").windows()
    #print([w.window_text() for w in windows])




    # 过滤掉任务栏窗口和标题为空的窗口
    filtered_windows = [w for w in windows if w.window_text() != "任务栏" and w.window_text()]
    filtered_windows = [w for w in filtered_windows if w.window_text() != "Program Manager" and w.window_text()]

    if filtered_windows:
        # 连接到过滤后列表中的第一个窗口
        app = Application(backend="uia").connect(process=filtered_windows[0].process_id())
        top_window = app.top_window()
        #print("Top window: ", top_window.window_text())
        return top_window.window_text()
    else:
        #print("没有找到合适的窗口来连接。")
        return None

#get_current_window()