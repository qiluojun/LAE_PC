import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from PySide6.QtWidgets import QSystemTrayIcon, QMenu

from questionnaire_copy import Ui_questionnaire
from PySide6.QtGui import QIcon, QAction
import app_rc # 由pyside6-rcc生成的资源文件 
 
 
 
 
class MyMainWindow(QMainWindow):
    # 继承一个QMainWindow，点右上角不会退出
    def __init__(self):
        QMainWindow.__init__(self)

    def closeEvent(self, event):
        # 忽略退出事件，而是隐藏到托盘
        event.ignore()
        self.hide()


class MySysTrayWidget(QWidget):
    def __init__(self, ui=None, app=None, window=None):
        QWidget.__init__(self)  # 必须调用，否则信号系统无法启用

        # 私有变量
        self.__ui = ui
        self.__app = app
        self.__window = window
        #self.__ui.setupUi(self.__window)
        #self.__ui.setupUi(self)
        
        
        # 配置系统托盘
        self.__trayicon = QSystemTrayIcon(self)
        self.__trayicon.setIcon(QIcon(':/app_icon.png'))
        self.__trayicon.setToolTip('D22Maid\n热键Ctrl+Alt+M')

        # 创建托盘的右键菜单
        self.__traymenu = QMenu()
        self.__trayaction = []
        self.addTrayMenuAction('显示主界面', self.show_userinterface)
        self.addTrayMenuAction('退出', self.quit)

        # 配置菜单并显示托盘
        self.__trayicon.setContextMenu(self.__traymenu) #把tpMenu设定为托盘的右键菜单
        self.__trayicon.show()  #显示托盘   

        # 连接信号
        self.__ui.pushButton.clicked.connect(self.hide_userinterface)

        # 默认隐藏界面
        #self.hide_userinterface()

    def __del__(self):
        pass

    def addTrayMenuAction(self, text='empty', callback=None):
        a = QAction(text, self)
        a.triggered.connect(callback)
        self.__traymenu.addAction(a)
        self.__trayaction.append(a)

    def quit(self):
        # 真正的退出
        self.__app.exit()

    def show_userinterface(self):
        self.__window.show()

    def hide_userinterface(self):
        self.__window.hide()














if __name__=='__main__':
    # 初始化应用和窗口
    app = QApplication(sys.argv)
    win = MyMainWindow()
    
    # 载入界面
    ui = Ui_questionnaire(win)
    ui.setupUi()
    
 
    # 创建系统托盘项目
    tray = MySysTrayWidget(app=app, window=win, ui=ui)

    # 显示窗口
    win.show()

    # 运行应用
    sys.exit(app.exec())




app = QApplication(sys.argv)
questionnaireWindow = QMainWindow()
ui = Ui_questionnaire(questionnaireWindow)
ui.setupUi()
    