from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer,Qt

class InterfaceTransition:
    def __init__(self, interface_code):
        self.interface_code = interface_code
        self.transitions = {}  # 字典，键是条件，值是下一个界面的InterfaceTransition对象

    def add_transition(self, condition, next_interface):
        self.transitions[condition] = next_interface

    def get_next_interface(self, condition):
        return self.transitions.get(condition, None)




class Conditioner(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Conditioner")
        self.setGeometry(200, 200, 600, 400)
        # 设置窗口始终在最顶层
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        
        self.current_interface_index = '0'  # 好家伙 index两个变量用不上了 但是懒得删
        self.last_interface_index = '0'  
        
        self.selected_button = None
        self.waiting_minutes=0
        # 构建界面跳转图
        self.interface_graph = self.build_interface_graph()
        self.current_interface = self.interface_graph['0']  # 初始界面
        self.interface_history = [] 
        
        
        # 设置中央窗口和布局
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)



        # 初始化初始界面
        self.inter_0()

    def reset_window(self):
        # 重置窗口到初始状态的逻辑
        self.selected_button = None
       
        # 重置界面图和当前界面
        self.interface_graph = self.build_interface_graph()
        self.current_interface = self.interface_graph['0']
        # 清空历史记录
        self.interface_history.clear()
        # 重新初始化初始界面
        self.inter_0()
    

    def closeEvent(self, event):
        super().closeEvent(event)
        self.reset_window()
        # 当窗口关闭时，检查是否有父窗口并且父窗口有startTimer方法，然后重新启动计时器
        if self.parent() and hasattr(self.parent(), 'startTimer'):
            self.parent().startTimer()


    
    

    def inter_0(self):
        
        self.last_interface_index= self.current_interface_index
        self.current_interface_index = "0"
        
        self.clear_layout(self.layout)

        self.selected_button = None
        self.label = QLabel("是否为正常使用？")
        
        # 创建并添加初始界面的按钮
        self.button01Yes = QPushButton("Yes")
        self.button01No = QPushButton("No")
        self.button01Yes.setCheckable(True)
        self.button01No.setCheckable(True)
        self.button01Yes.clicked.connect(lambda: self.toggle_button(self.button01Yes))
        self.button01No.clicked.connect(lambda: self.toggle_button(self.button01No))
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button01Yes)
        self.layout.addWidget(self.button01No)


        self.button01Yes.clicked.connect(lambda: self.set_selected_button("button01Yes"))
        self.button01No.clicked.connect(lambda: self.set_selected_button("button01No"))


        # next button
        self.add_next_button()
        
    
 
    
   
    
    
    
    def inter_01(self):
        self.clear_layout(self.layout)
        self.selected_button = None
        self.last_interface_index = self.current_interface_index
        self.current_interface_index = "01"
        
        # 界面设置...
        
        
        self.label = QLabel("<p>您已选择正常使用&nbsp;</p><p>xx分钟后再来询问</p>")
        self.layout.addWidget(self.label)
        
        # 添加输入框
        self.input_minutes = QLineEdit()
        self.layout.addWidget(self.input_minutes)
        
        
        self.add_confirm_button()
        self.add_back_button()
        
    def add_confirm_button(self):
        # 创建确定按钮
        self.confirmButton = QPushButton("确定")
        self.layout.addWidget(self.confirmButton)
        # 连接按钮点击信号到处理函数
        self.confirmButton.clicked.connect(self.handle_confirm)

    def handle_confirm(self):
        
        # 顺便加一个 点以后 有√特效        
        original_text = self.confirmButton.text()
        self.confirmButton.setText("√")
        # Use QTimer.singleShot to change the text back to the original text after 1 second
        QTimer.singleShot(1000, lambda: self.confirmButton.setText(original_text))

        
        # 从输入框获取分钟数
        self.waiting_minutes = float(self.input_minutes.text())

   
    def inter_021(self):
        self.clear_layout(self.layout)
        self.selected_button = 'next'

        # 创建上中下三个子layout
        top_layout = QVBoxLayout()
        middle_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()

        # 上layout添加一个富文本label
        label_top = QLabel("是否存在下列<b><font color='red'>异常</font></b>？")
        top_layout.addWidget(label_top)

        middle_row_1_layout =QHBoxLayout()
        middle_row_2_layout =QHBoxLayout()
        
        self.middle_row_1_lable=QLabel("心理上：")
        self.middle_row_2_lable=QLabel("生理上：")
        
        self.middle_row_1_button1=QPushButton("焦躁不安")
        self.middle_row_1_button2=QPushButton("不开心")
        self.middle_row_1_button3=QPushButton("抗拒某事")
        self.middle_row_1_button4=QPushButton("心累 需人工爆破")
        self.middle_row_1_button1.setCheckable(True)
        self.middle_row_1_button2.setCheckable(True)
        self.middle_row_1_button3.setCheckable(True)
        self.middle_row_1_button4.setCheckable(True)
        self.middle_row_1_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button1))
        self.middle_row_1_button2.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button2))
        self.middle_row_1_button3.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button3))
        self.middle_row_1_button4.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button4))
        
        
        self.middle_row_2_button1=QPushButton("久坐身体不适")
        self.middle_row_2_button2=QPushButton("暴饮暴食")
        self.middle_row_2_button3=QPushButton("眼睛不适")
        self.middle_row_2_button4=QPushButton("脑子发麻")
        self.middle_row_2_button1.setCheckable(True)
        self.middle_row_2_button2.setCheckable(True)
        self.middle_row_2_button3.setCheckable(True)
        self.middle_row_2_button4.setCheckable(True)
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button1))
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button2))
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button3))
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button4))
        
        middle_row_1_layout.addWidget(self.middle_row_1_lable)
        middle_row_1_layout.addWidget(self.middle_row_1_button1)
        middle_row_1_layout.addWidget(self.middle_row_1_button2)
        middle_row_1_layout.addWidget(self.middle_row_1_button3)
        middle_row_1_layout.addWidget(self.middle_row_1_button4)

        middle_row_2_layout.addWidget(self.middle_row_2_lable)    
        middle_row_2_layout.addWidget(self.middle_row_2_button1)
        middle_row_2_layout.addWidget(self.middle_row_2_button2)
        middle_row_2_layout.addWidget(self.middle_row_2_button3)
        middle_row_2_layout.addWidget(self.middle_row_2_button4)
        
        middle_layout.addLayout(middle_row_1_layout)
        middle_layout.addLayout(middle_row_2_layout)
        
        
        # 下layout添加返回和下一步按钮
        self.backButton = QPushButton("返回上一步")
        self.backButton.clicked.connect(self.go_to_last_interface)
        bottom_layout.addWidget(self.backButton)

        self.nextButton = QPushButton("下一步")
        self.nextButton.clicked.connect(self.go_to_next_interface)
        bottom_layout.addWidget(self.nextButton)

        
        
        
        # 将上中下layout添加到主layout
        self.layout.addLayout(top_layout)
        self.layout.addStretch(1)
        self.layout.addLayout(middle_layout)
        self.layout.addStretch(3)
        self.layout.addLayout(bottom_layout)
        self.layout.addStretch(1)

    def inter_022(self):
        
        self.clear_layout(self.layout)
        self.selected_button = None

        # 创建上中下三个子layout
        top_layout = QVBoxLayout()
        middle_layout = QVBoxLayout()
        bottom_layout = QHBoxLayout()

        # 上layout添加一个富文本label
        label_top = QLabel("请选择具体情况")
        top_layout.addWidget(label_top)

        middle_row_1_layout =QHBoxLayout()
        middle_row_2_layout =QHBoxLayout()
        
        middle_row_1_lable=QLabel("脑子：")
        middle_row_2_lable=QLabel("身体：")
        
        self.middle_row_1_button1=QPushButton("尚可")
        self.middle_row_1_button2=QPushButton("中等损耗")
        self.middle_row_1_button3=QPushButton("严重损耗")
        
        self.middle_row_1_button1.setCheckable(True)
        self.middle_row_1_button2.setCheckable(True)
        self.middle_row_1_button3.setCheckable(True)
        
        self.middle_row_1_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button1))
        self.middle_row_1_button2.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button2))
        self.middle_row_1_button3.clicked.connect(lambda: self.toggle_button(self.middle_row_1_button3))
        
        
        
        self.middle_row_2_button1=QPushButton("尚可")
        self.middle_row_2_button2=QPushButton("中等损耗")
        self.middle_row_2_button3=QPushButton("严重损耗")
        
        self.middle_row_2_button1.setCheckable(True)
        self.middle_row_2_button2.setCheckable(True)
        self.middle_row_2_button3.setCheckable(True)
        
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button1))
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button2))
        self.middle_row_2_button1.clicked.connect(lambda: self.toggle_button(self.middle_row_2_button3))
        
        
        middle_row_1_layout.addWidget(middle_row_1_lable)
        middle_row_1_layout.addWidget(self.middle_row_1_button1)
        middle_row_1_layout.addWidget(self.middle_row_1_button2)
        middle_row_1_layout.addWidget(self.middle_row_1_button3)
        

        middle_row_2_layout.addWidget(middle_row_2_lable)    
        middle_row_2_layout.addWidget(self.middle_row_2_button1)
        middle_row_2_layout.addWidget(self.middle_row_2_button2)
        middle_row_2_layout.addWidget(self.middle_row_2_button3)
        
        
        middle_layout.addLayout(middle_row_1_layout)
        middle_layout.addLayout(middle_row_2_layout)
        
        
        # 下layout添加返回和下一步按钮
        self.backButton = QPushButton("返回上一步")
        self.backButton.clicked.connect(self.go_to_last_interface)
        bottom_layout.addWidget(self.backButton)

        self.nextButton = QPushButton("下一步")
        self.nextButton.clicked.connect(self.status_checker022)
        self.nextButton.clicked.connect(self.go_to_next_interface)
        bottom_layout.addWidget(self.nextButton)

        
        
        
        # 将上中下layout添加到主layout
        self.layout.addLayout(top_layout)
        self.layout.addStretch(1)
        self.layout.addLayout(middle_layout)
        self.layout.addStretch(3)
        self.layout.addLayout(bottom_layout)
        self.layout.addStretch(1)


    
    def inter_0221(self):
        self.clear_layout(self.layout)
        self.selected_button = None
       
        
        # 界面设置...
        
        self.label = QLabel('<p><span style="color:#00D5FF;font-size:9pt;">直接睡觉休息</span></p><p><span style="color:#2C2B29;font-size:9pt;"><span style="font-size:16px;">无任何</span><strong><span style="font-size:16px;">媒体</span></strong><span style="font-size:16px;">&nbsp;</span></span></p><p><span style="color:#2C2B29;font-size:9pt;">所有事情下个时段再开始</span></p><p><span style="color:#2C2B29;font-size:9pt;"><br /></span></p><p><span style="color:#2C2B29;font-size:9pt;background-color:#DFC5A4;">负罪不安 　しないで</span></p><p><span style="color:#2C2B29;font-size:9pt;background-color:#FFE500;">担心休息的效果　しないで</span></p><p><span style="color:#2C2B29;font-size:16px;background-color:#E56600;"><strong>担心担心　しないで！！！</strong></span></p>')
        self.layout.addWidget(self.label)
        
        self.add_back_button()
        self.add_next_button()
    
    
    def inter_0222(self):
        self.clear_layout(self.layout)
        
        
        
        if self.selected_button ==  '0222-1':
            self.label = QLabel('<p style="text-align:center;"><span style="color:#E394DC;font-family:Consolas, &quot;font-size:24px;background-color:#181818;">运动 5-10min</span></p><p style="text-align:center;"><span style="color:#E394DC;font-family:Consolas, &quot;font-size:24px;background-color:#181818;"></span></p>')
        else: 
            self.label = QLabel('<p style="text-align:center;"><span style="color:#E394DC;font-family:Consolas, &quot;font-size:24px;background-color:#181818;">静休5-10min no媒体</span></p><p style="text-align:center;"><span style="color:#E394DC;font-family:Consolas, &quot;font-size:24px;background-color:#181818;"></span></p>')
            
            
        self.selected_button = 'next'
            
        
        # 界面设置...
        
        
        self.layout.addWidget(self.label)
        
        self.add_back_button()
        self.add_next_button()
    
    def inter_02221(self):
        self.clear_layout(self.layout)
        self.selected_button = None
       
        
        # 界面设置...
        
        self.label = QLabel('<p style="text-align:center;">选择合适的活动：</p><p>时间是否合适？</p><p>是否有明显焦虑项？</p><p>脑力是否合适？</span></p>')
        self.layout.addWidget(self.label)
        
        self.add_back_button()
        self.add_next_button()
    
    
    
    
    def inter_0223(self):
        self.clear_layout(self.layout)
        self.selected_button = None
       
        
        # 界面设置...
        
        self.label = QLabel('<span style="color:#E394DC;text-align:center;font-family:Consolas, &quot;font-size:16px;background-color:#181818;">站起来</span><strong><span style="font-size:16px;">&nbsp;活动一下&nbsp;</span></strong><span style="color:#E394DC;font-family:Consolas, &quot;font-size:16px;background-color:#181818;">然后尝试 原计划 几分钟！</span></p>')
        self.layout.addWidget(self.label)
        
        self.add_back_button()
        self.add_next_button()
    

    '''功能区'''

 
    def status_checker022(self):
        
        if self.middle_row_1_button3.isChecked() or self.middle_row_2_button3.isChecked():
            self.selected_button = "0221"
        elif self.middle_row_1_button2.isChecked() :
            if self.middle_row_2_button2.isChecked() :
                self.selected_button = "0222-2"
            else:
                self.selected_button = "0222-1"
        else:
            self.selected_button = "0223"
        

    def toggle_button(self, button):
        if button.isChecked():
            button.setStyleSheet("background-color: lightgreen;")
        else:
            button.setStyleSheet("")

    


    def set_selected_button(self, button_name):
        self.selected_button = button_name
        
    def add_back_button(self):
        # 添加返回上一步的按钮
        self.backButton = QPushButton("返回上一步")
        self.layout.addWidget(self.backButton)
        self.backButton.clicked.connect(self.go_to_last_interface)

    def add_next_button(self):
        # 添加返回上一步的按钮
        self.nextButton = QPushButton("下一步")
        self.layout.addWidget(self.nextButton)
        self.nextButton.clicked.connect(self.go_to_next_interface)


    





    
    def build_interface_graph(self):
        # 构建界面跳转图
        interface_0 = InterfaceTransition('0')
        interface_01 = InterfaceTransition('01')
        interface_021 = InterfaceTransition('021')
        interface_022 = InterfaceTransition('022')
        interface_0221 = InterfaceTransition('0221')
        interface_0222 = InterfaceTransition('0222')
        interface_02221 = InterfaceTransition('02221')
        interface_0223 = InterfaceTransition('0223')
        # 添加更多界面和转换逻辑
        
        # 定义跳转逻辑
        interface_0.add_transition('button01Yes', interface_01)
        interface_0.add_transition('button01No', interface_021)
        interface_021.add_transition('next', interface_022)
        interface_022.add_transition('0221', interface_0221)
        interface_022.add_transition('0222-1', interface_0222)
        interface_022.add_transition('0222-2', interface_0222)
        interface_022.add_transition('0223', interface_0223)
        interface_0222.add_transition('next', interface_02221)
        
        # 添加更多转换逻辑
        
        '''
        # 构建界面跳转图
        interface_0 = InterfaceTransition('0')
        interface_01 = InterfaceTransition('01')
        interface_021 = InterfaceTransition('021')
        interface_011 = InterfaceTransition('011')
        interface_0111 = InterfaceTransition('0111')
        
        # 定义跳转逻辑
        interface_0.add_transition('button01Yes', interface_01)
        interface_0.add_transition('button01No', interface_021)
        interface_01.add_transition('next', interface_011)  # 假设从01到011是按下“下一步”按钮
        interface_011.add_transition('next', interface_0111)  # 同上
        '''
        
        
        
        
        
        return {
            '0': interface_0,
            '01': interface_01,
            '021': interface_021,
            '022': interface_022,
            '0221':interface_0221,
            '0222':interface_0221,
            '02221':interface_02221,
            '0223':interface_0223,
            # 添加更多界面
        }

    def go_to_next_interface(self):
        next_interface = self.current_interface.get_next_interface(self.selected_button)
        if next_interface:
            # 在跳转之前，将当前界面的代码推入历史栈中
            self.interface_history.append(self.current_interface.interface_code)
            self.current_interface = next_interface
            # 调用相应界面的方法
            getattr(self, f"inter_{self.current_interface.interface_code}")()
        else:
            # 如果没有找到下一个界面，可以在这里处理
            pass
    
    
    
    
    def go_to_last_interface(self):
        if self.interface_history:
            # 从历史栈中弹出最后一个界面代码
            last_interface_code = self.interface_history.pop()
            # 找到对应的界面对象
            self.current_interface = self.interface_graph[last_interface_code]
            # 调用相应界面的方法
            getattr(self, f"inter_{self.current_interface.interface_code}")()
        else:
            # 如果历史栈为空，可以在这里处理（比如禁用返回按钮或显示提示信息）
            pass
    
    
    
    
    
    
   

    def clear_layout(self, layout):
        # 清除布局逻辑...
        pass




    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                sub_layout = item.layout()
                if sub_layout is not None:
                    self.clear_layout(sub_layout)
                    sub_layout.deleteLater()

if __name__ == "__main__":
    app = QApplication([])
    window = Conditioner()
    window.show()
    app.exec()