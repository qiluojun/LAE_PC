# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setGeometry(QRect(0, 0, 381, 571))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.current_period_name_label = QLabel(self.left_frame)
        self.current_period_name_label.setObjectName(u"current_period_name_label")
        self.current_period_name_label.setGeometry(QRect(20, 10, 131, 20))
        self.show_plan_button = QPushButton(self.left_frame)
        self.show_plan_button.setObjectName(u"show_plan_button")
        self.show_plan_button.setGeometry(QRect(50, 360, 141, 31))
        self.basic_state_record_button = QPushButton(self.left_frame)
        self.basic_state_record_button.setObjectName(u"basic_state_record_button")
        self.basic_state_record_button.setGeometry(QRect(50, 420, 141, 41))
        self.plan_text = QTextEdit(self.left_frame)
        self.plan_text.setObjectName(u"plan_text")
        self.plan_text.setGeometry(QRect(20, 60, 341, 271))
        self.right_frame = QFrame(self.centralwidget)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setGeometry(QRect(380, 0, 421, 581))
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.start_new_period_button = QPushButton(self.right_frame)
        self.start_new_period_button.setObjectName(u"start_new_period_button")
        self.start_new_period_button.setGeometry(QRect(30, 10, 101, 24))
        self.end_current_period_button = QPushButton(self.right_frame)
        self.end_current_period_button.setObjectName(u"end_current_period_button")
        self.end_current_period_button.setGeometry(QRect(30, 40, 101, 24))
        self.close_button = QPushButton(self.right_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(30, 70, 101, 24))
        #自己新增的部分
        self.lock_button = QPushButton("lock now",self.right_frame)
        self.lock_button.setGeometry(QRect(30, 94, 101, 24))
        
        self.activity_list = QListWidget(self.right_frame)
        self.activity_list.setObjectName(u"activity_list")
        self.activity_list.setGeometry(QRect(30, 140, 256, 192))
        self.current_activity_name_label = QLabel(self.right_frame)
        self.current_activity_name_label.setObjectName(u"current_activity_name_label")
        self.current_activity_name_label.setGeometry(QRect(30, 360, 171, 20))
        self.new_activity_button = QPushButton(self.right_frame)
        self.new_activity_button.setObjectName(u"new_activity_button")
        self.new_activity_button.setGeometry(QRect(30, 410, 75, 24))
        self.end_activity_button = QPushButton(self.right_frame)
        self.end_activity_button.setObjectName(u"end_activity_button")
        self.end_activity_button.setGeometry(QRect(160, 410, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.current_period_name_label.setText(QCoreApplication.translate("MainWindow", u"current_period_name", None))
        self.show_plan_button.setText(QCoreApplication.translate("MainWindow", u"show plan", None))
        self.basic_state_record_button.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u57fa\u672c\u72b6\u6001", None))
        self.start_new_period_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u65b0\u65f6\u6bb5", None))
        self.end_current_period_button.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u5f53\u524d\u65f6\u6bb5", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.current_activity_name_label.setText(QCoreApplication.translate("MainWindow", u"current_activity_name", None))
        self.new_activity_button.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u6d3b\u52a8", None))
        self.end_activity_button.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u6d3b\u52a8", None))
    # retranslateUi

