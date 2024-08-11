from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, 
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QDoubleSpinBox,QMessageBox,QSlider)

from PySide6.QtWidgets import QSystemTrayIcon, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QStyle

import sys
import sqlite3
import datetime
import time
import os


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        self.yes_button = QPushButton(Dialog)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setGeometry(QRect(20, 350, 75, 24))
        
        
        self.activeness_label = QLabel(Dialog)
        self.activeness_label.setObjectName(u"activeness_label")
        self.activeness_label.setGeometry(QRect(20, 20, 65, 16))
        self.joy_label = QLabel(Dialog)
        self.joy_label.setObjectName(u"joy_label")
        self.joy_label.setGeometry(QRect(20, 60, 65, 16))
        self.anxiety_label = QLabel(Dialog)
        self.anxiety_label.setObjectName(u"anxiety_label")
        self.anxiety_label.setGeometry(QRect(20, 100, 65, 16))
        self.exhaustion_label = QLabel(Dialog)
        self.exhaustion_label.setObjectName(u"exhaustion_label")
        self.exhaustion_label.setGeometry(QRect(20, 140, 65, 16))
        self.vitality_label = QLabel(Dialog)
        self.vitality_label.setObjectName(u"vitality_label")
        self.vitality_label.setGeometry(QRect(20, 180, 61, 16))
        self.sleepiness_label = QLabel(Dialog)
        self.sleepiness_label.setObjectName(u"sleepiness_label")
        self.sleepiness_label.setGeometry(QRect(20, 220, 61, 16))
        self.hope_label = QLabel(Dialog)
        self.hope_label.setObjectName(u"hope_label")
        self.hope_label.setGeometry(QRect(20, 260, 61, 16))      
        
        
        self.activeness_value_label = QLabel(Dialog)
        self.activeness_value_label.setObjectName(u"activeness_value_label")
        self.activeness_value_label.setGeometry(QRect(240, 20, 65, 16))
        self.joy_value_label = QLabel(Dialog)
        self.joy_value_label.setObjectName(u"joy_value_label")
        self.joy_value_label.setGeometry(QRect(240, 60, 65, 16))
        self.anxiety_value_label = QLabel(Dialog)
        self.anxiety_value_label.setObjectName(u"anxiety_value_label")
        self.anxiety_value_label.setGeometry(QRect(240, 100, 65, 16))
        self.exhaustion_value_label = QLabel(Dialog)
        self.exhaustion_value_label.setObjectName(u"exhaustion_value_label")
        self.exhaustion_value_label.setGeometry(QRect(240, 140, 65, 16))
        self.vitality_value_label = QLabel(Dialog)
        self.vitality_value_label.setObjectName(u"vitality_value_label")
        self.vitality_value_label.setGeometry(QRect(240, 180, 65, 16))
        self.sleepiness_value_label = QLabel(Dialog)
        self.sleepiness_value_label.setObjectName(u"sleepiness_value_label")
        self.sleepiness_value_label.setGeometry(QRect(240, 220, 65, 16))
        self.hope_value_label = QLabel(Dialog)
        self.hope_value_label.setObjectName(u"hope_value_label")
        self.hope_value_label.setGeometry(QRect(240, 260, 65, 16))
        
        
        self.activeness_slider = QSlider(Qt.Horizontal, Dialog)
        self.activeness_slider.setObjectName(u"activeness_slider")
        self.activeness_slider.setGeometry(QRect(120, 20, 113, 20))
        self.activeness_slider.setMinimum(10)
        self.activeness_slider.setMaximum(50)
        self.activeness_slider.setValue(30)  # Set the default value to 3.00
        self.activeness= 3.0
        self.activeness_changed = False
        self.activeness_slider.valueChanged.connect(self.update_activeness)

        
        self.joy_slider = QSlider(Qt.Horizontal, Dialog)
        self.joy_slider.setObjectName(u"joy_slider")
        self.joy_slider.setGeometry(QRect(120, 60, 113, 20))
        self.joy_slider.setMinimum(10)
        self.joy_slider.setMaximum(50)
        self.joy_slider.setValue(30)  # Set the default value to 3.00
        self.joy= 3.0
        self.joy_changed = False
        self.joy_slider.valueChanged.connect(self.update_joy)
        
        self.anxiety_slider = QSlider(Qt.Horizontal, Dialog)
        self.anxiety_slider.setObjectName(u"anxiety_slider")
        self.anxiety_slider.setGeometry(QRect(120, 100, 113, 20))
        self.anxiety_slider.setMinimum(10)
        self.anxiety_slider.setMaximum(50)
        self.anxiety_slider.setValue(30)  # Set the default value to 3.00
        self.anxiety= 3.0
        self.anxiety_changed = False
        self.anxiety_slider.valueChanged.connect(self.update_anxiety)
        
        
        self.exhaustion_slider = QSlider(Qt.Horizontal, Dialog)
        self.exhaustion_slider.setObjectName(u"exhaustion_slider")
        self.exhaustion_slider.setGeometry(QRect(120, 140, 113, 20))
        self.exhaustion_slider.setMinimum(10)
        self.exhaustion_slider.setMaximum(50)
        self.exhaustion_slider.setValue(30)  # Set the default value to 3.00
        self.exhaustion= 3.0
        self.exhaustion_changed = False
        self.exhaustion_slider.valueChanged.connect(self.update_exhaustion)
        
        self.vitality_slider = QSlider(Qt.Horizontal, Dialog)
        self.vitality_slider.setObjectName(u"vitality_slider")
        self.vitality_slider.setGeometry(QRect(120, 180, 113, 20))
        self.vitality_slider.setMinimum(10)
        self.vitality_slider.setMaximum(50)
        self.vitality_slider.setValue(30)  # Set the default value to 3.00
        self.vitality= 3.0
        self.vitality_changed = False
        self.vitality_slider.valueChanged.connect(self.update_vitality)
        
        self.sleepiness_slider = QSlider(Qt.Horizontal, Dialog)
        self.sleepiness_slider.setObjectName(u"sleepiness_slider")
        self.sleepiness_slider.setGeometry(QRect(120, 220, 113, 20))
        self.sleepiness_slider.setMinimum(10)
        self.sleepiness_slider.setMaximum(50)
        self.sleepiness_slider.setValue(30)  # Set the default value to 3.00
        self.sleepiness= 3.0
        self.sleepiness_changed = False
        self.sleepiness_slider.valueChanged.connect(self.update_sleepiness)
    
        
        self.hope_slider = QSlider(Qt.Horizontal, Dialog)
        self.hope_slider.setObjectName(u"hope_slider")
        self.hope_slider.setGeometry(QRect(120, 260, 113, 20))
        self.hope_slider.setMinimum(10)
        self.hope_slider.setMaximum(50)
        self.hope_slider.setValue(30)  # Set the default value to 3.00
        self.hope= 3.0
        self.hope_changed = False
        self.hope_slider.valueChanged.connect(self.update_hope)
        
        self.yes_button.clicked.connect(self.show_message)
        
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bb0\u5f55\u57fa\u7840\u72b6\u6001", None))
        self.yes_button.setText(QCoreApplication.translate("Dialog", u"\u751f\u6210\u8bb0\u5f55", None))
        
        self.activeness_label.setText(QCoreApplication.translate("Dialog", u"Activeness", None))
        self.joy_label.setText(QCoreApplication.translate("Dialog", u"Joy", None))
        self.anxiety_label.setText(QCoreApplication.translate("Dialog", u"Anxiety", None))
        self.exhaustion_label.setText(QCoreApplication.translate("Dialog", u"Exhaustion", None))
        self.vitality_label.setText(QCoreApplication.translate("Dialog", u"Vitality", None))
        self.sleepiness_label.setText(QCoreApplication.translate("Dialog", u"sleepiness", None))
        self.hope_label.setText(QCoreApplication.translate("Dialog", u"Hope", None))
    # retranslateUi

    def update_sleepiness(self, value):
        self.sleepiness = value / 10.0
        self.sleepiness_changed = True
        self.sleepiness_value_label.setText(str(self.sleepiness))
    def update_joy(self, value):
        self.joy = value / 10.0
        self.joy_changed = True
        self.joy_value_label.setText(str(self.joy))
    def update_anxiety(self, value):
        self.anxiety = value / 10.0
        self.anxiety_changed = True
        self.anxiety_value_label.setText(str(self.anxiety))
    def update_vitality(self, value):
        self.vitality = value / 10.0
        self.vitality_changed = True
        self.vitality_value_label.setText(str(self.vitality))
    def update_activeness(self, value):
        self.activeness = value / 10.0
        self.activeness_changed = True
        self.activeness_value_label.setText(str(self.activeness))
    def update_hope(self, value):
        self.hope = value / 10.0
        self.hope_changed = True
        self.hope_value_label.setText(str(self.hope))
    def update_exhaustion(self, value):
        self.exhaustion = value / 10.0
        self.exhaustion_changed = True
        self.exhaustion_value_label.setText(str(self.exhaustion))


    def show_message(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("已成功添加记录")
        msgBox.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(500, msgBox.accept)  # 0.5 seconds
        msgBox.exec()




class basic_state_record_window(QDialog):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_Dialog()
 # 初始化界面
        self.ui.setupUi(self)   
        self.ui.yes_button.clicked.connect(self.basic_state_record_generate)

    def basic_state_record_generate(self):
        basic_state={}
        basic_state['time']=  datetime.datetime.now().strftime("%D:%H:%M:%S")
        if self.ui.sleepiness_changed:
            basic_state['sleepiness'] = (self.ui.sleepiness)
        else:
            basic_state['sleepiness'] = 0
        if self.ui.joy_changed:
            basic_state['joy'] = (self.ui.joy)
        else:
            basic_state['joy'] = 0
        if self.ui.anxiety_changed:
            basic_state['anxiety'] = (self.ui.anxiety)
        else:
            basic_state['anxiety'] = 0
        if self.ui.vitality_changed:
            basic_state['vitality'] = (self.ui.vitality)
        else:
            basic_state['vitality'] = 0
        if self.ui.activeness_changed:
            basic_state['activeness'] = (self.ui.activeness)
        else:
            basic_state['activeness'] = 0
        if self.ui.exhaustion_changed:
            basic_state['exhaustion'] = (self.ui.exhaustion)
        else:
            basic_state['exhaustion'] = 0
        if self.ui.hope_changed:
            basic_state['hope'] = (self.ui.hope)
        else:
            basic_state['hope'] = 0
        
        # Commit the changes to the database
        
        self.write_state(basic_state)
    
        '''# Show a system tray notification
        tray_icon = QSystemTrayIcon(QApplication.style().standardIcon(QStyle.SP_ComputerIcon), self)
        tray_icon.show()
        tray_icon.showMessage("Success", "State recorded successfully!", QSystemTrayIcon.Information, 2000)'''

    def write_state(self,basic_state):
        
        # Create a connection to the database file
        conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()


        # Insert the values into the database
        cursor.execute('''
            INSERT INTO basic_state (time, 积极度, 愉悦度, 焦虑度, 脑损度, 体力值, 困倦度,希望感 )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (basic_state['time'], basic_state['activeness'], basic_state['joy'], basic_state['anxiety'], basic_state['exhaustion'], basic_state['vitality'],basic_state['sleepiness'],basic_state['hope']))
        # Commit the changes to the database
        conn.commit()
        # Close the database connection
        conn.close()    
    
# 启动窗口
app = QApplication(sys.argv)

main_window=basic_state_record_window()

# 显示主窗口 
main_window.show()

app.exec()
