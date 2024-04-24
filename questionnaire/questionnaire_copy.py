from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime,QTimer, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import datetime
import sys

from class_question_answer import Question
from write_answer_in_db import write_answer_in_db,get_question_from_db


class Ui_questionnaire(object):  # from reminder_finalversion.py
    def set_layout_visible(self, layout, visible):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget() is not None:
                item.widget().setVisible(visible)
            elif item.layout() is not None:
                self.set_layout_visible(item.layout(), visible)


    def __init__(self,questionnaireWindow):
        self.centralwidget = QWidget(questionnaireWindow)
        self.layout = QHBoxLayout(self.centralwidget)

        # 左边的布局
        self.left_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout, 1)

        # 左边的控件
        self.question_list = QListWidget(self.centralwidget)

        self.ans_condition_label = QLabel("回答情况", self.centralwidget)
        self.pushButton= QPushButton("close", self.centralwidget)
        
        # 将控件添加到左边的布局
        self.left_layout.addWidget(self.question_list, 3)
        self.left_layout.addWidget(self.ans_condition_label, 1)
        self.left_layout.addWidget(self.pushButton, 1)
        
        
        # 右边的布局
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.right_layout, 1)

        # 右边的控件
        self.ques_stem_line = QLineEdit("文本", self.centralwidget)
        self.ques_stem_line.setReadOnly(True)
   
        
        
        

        
        
        
        
        # 离散选择题的布局
        self.slider = QSlider(Qt.Horizontal, self.centralwidget)
        self.option_label_top = QLabel("text", self.centralwidget)
        self.slider_top_layout = QHBoxLayout()
        self.slider_top_layout.addStretch()  # 添加弹性空间
        self.slider_top_layout.addWidget(self.option_label_top)
        self.slider_top_layout.addStretch()  # 添加弹性空间
                
        self.option_label_bottom_left = QLabel("text", self.centralwidget)
        self.option_label_bottom_right = QLabel("text", self.centralwidget)
        self.option_label_bottom_layout=QHBoxLayout()
        self.option_label_bottom_layout.addWidget(self.option_label_bottom_left)
        self.option_label_bottom_layout.addStretch()
        self.option_label_bottom_layout.addWidget(self.option_label_bottom_right)
        
        
        self.discrete_layout = QVBoxLayout()
        #self.discrete_layout.addWidget(self.ques_stem_line, 2)
        self.discrete_layout.addLayout(self.slider_top_layout)
        self.discrete_layout.addWidget(self.slider)
        self.discrete_layout.addLayout(self.option_label_bottom_layout)
        
        
        # 连续性选择题的布局
        self.continual_layout = QHBoxLayout()
        self.continual_slider = QSlider(Qt.Horizontal, self.centralwidget)
        '''self.continual_slider.setMinimum(10)
        self.continual_slider.setMaximum(50)
        self.continual_slider.setValue(30)  # Set the default value to 3.00
        self.continual_slider_value= 3.0
        self.continual_slider_value_changed = False
        self.continual_slider.valueChanged.connect(self.on_continual_slider_value_changed)'''
        self.continual_slider_label = QLabel(" ", self.centralwidget)
        self.continual_layout.addWidget(self.continual_slider,3)
        self.continual_layout.addWidget(self.continual_slider_label,1)
        
        

        
        
        # 主观题的布局
        self.subjective_layout = QHBoxLayout()
        self.subjective_line = QLineEdit("请输入：", self.centralwidget)
        self.confirm_button = QPushButton("确认", self.centralwidget)
        self.subjective_layout.addWidget(self.subjective_line,3)
        self.subjective_layout.addWidget(self.confirm_button,1)
        # 未点击提目前默认隐藏所有回答布局
        self.set_layout_visible(self.subjective_layout, False)
        self.set_layout_visible(self.discrete_layout, False)
        self.set_layout_visible(self.continual_layout, False)
        
        self.submit_button = QPushButton("提交", self.centralwidget)

        # 将控件添加到右边的布局
        
        
        
        
        
        self.right_layout.addWidget(self.ques_stem_line, 3)
        self.right_layout.addLayout(self.discrete_layout, 1)
        self.right_layout.addLayout(self.continual_layout, 1)
        self.right_layout.addLayout(self.subjective_layout, 2)
        self.right_layout.addWidget(self.submit_button, 1)

        questionnaireWindow.setCentralWidget(self.centralwidget)
        questionnaireWindow.resize(1000, 600)
        
        # Connect signals
        self.question_list.currentItemChanged.connect(self.update_question)
        
        

        
        
    
        self.submit_button.clicked.connect(self.record_answer)
    
    
    def set_discrete_layout(self):
        question = self.question_list.currentItem().data(Qt.UserRole)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        
        # Update the slider 
        self.slider.setRange(1, question.choice_num)
        if question.answer_content:
            self.slider.setValue(question.answer_content)
        else:self.slider.setValue(3)  
        
        self.slider.valueChanged.connect(self.on_discrete_slider_value_changed)
        # Update the question stem line
        self.ques_stem_line.setText(question.ques_stem)


        
        # Update the option labels
        if question.answer_content:
            print("question.answer_content:",question.answer_content)
            previous_choice = question.choice[question.answer_content]
        else :
            previous_choice = None
        self.option_label_top.setText(previous_choice)
        #print(question.choice)
        self.option_label_bottom_left.setText(question.choice[1])
        self.option_label_bottom_right.setText(question.choice[question.choice_num])
    
    def set_continual_layout(self):
        question = self.question_list.currentItem().data(Qt.UserRole)
        
        # Set slider properties  # 这里有待改成题目的属性变量
        self.continual_slider.setMinimum(10)
        self.continual_slider.setMaximum(50)
        if question.answer_content:
            self.continual_slider.setValue(question.answer_content*10)
        else:self.continual_slider.setValue(30) 
          
        # Set the default value to 3.00
        self.continual_slider_value= 3.0
        self.continual_slider_value_changed = False
        self.continual_slider.valueChanged.connect(self.on_continual_slider_value_changed)
        self.ques_stem_line.setText(question.ques_stem)
        
        
    
    def set_subjective_layout(self):
        question = self.question_list.currentItem().data(Qt.UserRole)
        if question.answer_content:
            self.subjective_line.setText(question.answer_content)
        else:self.subjective_line.setText(" ")
        self.confirm_button.clicked.connect(self.on_subjective_button_being_clicked)
        self.ques_stem_line.setText(question.ques_stem)

    def update_question(self, current, previous):
        # Get the current question
        #print("update_question being called")
        question = current.data(Qt.UserRole)

        # Check if question is None
        if question is None:
            return
        
        
        if question.continuity is None:
            # Show subjective layout and hide others
            self.set_layout_visible(self.subjective_layout, True)
            self.set_layout_visible(self.discrete_layout, False)
            self.set_layout_visible(self.continual_layout, False)
            self.set_subjective_layout()
        elif question.continuity == 1:
            # Show discrete layout and hide others
            self.set_layout_visible(self.subjective_layout, False)
            self.set_layout_visible(self.discrete_layout, True)
            self.set_layout_visible(self.continual_layout, False)
            self.set_discrete_layout()
        elif question.continuity == 0.1:
            # Show continual layout and hide others
            self.set_layout_visible(self.subjective_layout, False)
            self.set_layout_visible(self.discrete_layout, False)
            self.set_layout_visible(self.continual_layout, True)
            self.set_continual_layout()
    



    def setupUi(self):
        pass
    
    def on_continual_slider_value_changed(self,value):
        question = self.question_list.currentItem().data(Qt.UserRole)
            
        self.continual_slider_value = value / 10.0
        self.continual_slider_value_changed = True
        self.continual_slider_label.setText(str(self.continual_slider_value))
        
        question.answer_content= self.continual_slider_value
        self.question_list.currentItem().setData(Qt.UserRole,question)
        
        
        # Clear the QListWidgetItem text
        self.question_list.currentItem().setText("")
        # Create a QLabel with rich text and set it as the widget for the current item
        label = QLabel(question.ques_stem + " "+" <font color='gray'>" +"回答："+ str(question.answer_content) + "</font>")
        self.question_list.setItemWidget(self.question_list.currentItem(), label)

        # Update the ques_stem_line text
        self.ques_stem_line.setText(question.ques_stem.replace("【】","【" +  str(question.answer_content)+"】"))
    

    def on_discrete_slider_value_changed(self, value):
        # Get the current question
        #print("on_discrete_slider_value_changed being called")
        question = self.question_list.currentItem().data(Qt.UserRole)
        question.answer_content= value
        self.question_list.currentItem().setData(Qt.UserRole,question)
        
        
        
        # Update the option label
        self.option_label_top.setText(question.choice[value])

        # Clear the QListWidgetItem text
        self.question_list.currentItem().setText("")
        # Create a QLabel with rich text and set it as the widget for the current item
        label = QLabel(question.ques_stem + " "+" <font color='gray'>" +"回答："+ question.choice[value] + "</font>")
        self.question_list.setItemWidget(self.question_list.currentItem(), label)

        # Update the ques_stem_line text
        self.ques_stem_line.setText(question.ques_stem.replace("【】","【" + question.choice[value]+"】"))

    def on_subjective_button_being_clicked(self):
        question = self.question_list.currentItem().data(Qt.UserRole)
        question.answer_content= self.subjective_line.text()
        self.question_list.currentItem().setData(Qt.UserRole,question)
        
        # Clear the QListWidgetItem text
        self.question_list.currentItem().setText("")
        # Create a QLabel with rich text and set it as the widget for the current item
        label = QLabel(question.ques_stem + " "+" <font color='gray'>" +"回答："+ question.answer_content + "</font>")
        self.question_list.setItemWidget(self.question_list.currentItem(), label)
        
        # Update the ques_stem_line text
        self.ques_stem_line.setText(question.ques_stem.replace("【】","【" + question.answer_content +"】"))


    def record_answer(self):
        #print("?")
        question_set=[]
        for i in range(self.question_list.count()):
            item = self.question_list.item(i)
            question = item.data(Qt.UserRole)
            question.generate_time()
            question_set.append(question)
        write_answer_in_db(question_set)
        original_text = self.submit_button.text()
        # Change the text of the button to "√"
        self.submit_button.setText("√")
        # Use QTimer.singleShot to change the text back to the original text after 1 second
        QTimer.singleShot(1000, lambda: self.submit_button.setText(original_text))
        
        
    
    
    
    
        

    def retranslateUi(self, questionnaireWindow):
        _translate = QApplication.translate
        # 窗口名称
        questionnaireWindow.setWindowTitle(_translate("数据收集", "GRADUATION"))

def add_questions_to_list(question_set, list_widget):
    for question in question_set:
        item = QListWidgetItem(question.ques_stem)
        item.setData(Qt.UserRole, question)
        #print("question.choice",question.choice)
        list_widget.addItem(item)



if __name__ == "__main__":
    
    # 设计一个模块 到时候 自动根据 question 生成对应的choice 赋值给question
    choice_test=['一点都不','不太','有一点','相当','非常']
    question_test1=Question(variable='anxiety',ques_stem='我现在感到【】焦虑',choice_num=5,ques_id=233,choice=choice_test)
    question_test2=Question(variable='anxiety',ques_stem='我现在感到【】紧张',choice_num=5,ques_id=234,choice=choice_test)
    
 
    app = QApplication(sys.argv)
    questionnaireWindow = QMainWindow()
    ui = Ui_questionnaire(questionnaireWindow)
    ui.setupUi()
    
    
    # 添加问题进入程序！！！！重要至极！！ 到时候 直接给窗口输入一个字典或者列表包含所有题目即可 
        #即需要 先写个模块 确认需要的题目 从db读题目+选项 生成题目类变量 并且组装到字典里啥的~
    # Add the questions to the list widget
    
    # 创建问题集合
    question_set = get_question_from_db()

    # 添加问题到列表
    add_questions_to_list(question_set, ui.question_list)
    
    
    
    
    '''item1 = QListWidgetItem(question_test1.ques_stem)
    item1.setData(Qt.UserRole, question_test1)
    ui.question_list.addItem(item1)

    item2 = QListWidgetItem(question_test2.ques_stem)
    item2.setData(Qt.UserRole, question_test2)
    ui.question_list.addItem(item2)'''

    
    
    questionnaireWindow.show()
    sys.exit(app.exec())
    