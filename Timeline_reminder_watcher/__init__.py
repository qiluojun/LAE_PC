from Today import Today,Period

from end_ui import Ui_period_end

from PySide6.QtCore import QTimer, QTime,  Qt



class period_end_window(QMainWindow): # 载入 时段结算窗口 
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_period_end(self)



        
        



main_window = QMainWindow() # 待载入UI文件
main_window.window_action=' '

main_window.period_end_window=period_end_window()



main_window.today = Today()
main_window.today.get_periods()

Main_timer= QTimer("1 min")

def Main_timer_func():
    main_window.window_action=main_window.today.check_period()
    if main_window.window_action: # 如果非空 代表需要有所“作为”，然后 根据action的名字触发动作窗口，并且 窗口根据时段等属性来特定化
        if 'ask' in main_window.window_action:
            main_window.ask_window.ui.setupUi(main_window.today.current_period)
            main_window.ask_window.show()
            # 抓手在这里 要把ask window 搞出来（替换 时段结束窗口即可）
            # 然后 根据平板图的树 把整个判断逻辑的框架搞出来！哦！

