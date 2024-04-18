 # -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_period.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(366, 235)
        self.by_set_button = QPushButton(Dialog)
        self.by_set_button.setObjectName(u"by_set_button")
        self.by_set_button.setGeometry(QRect(30, 180, 81, 24))
        self.recommend_period_label = QLabel(Dialog)
        self.recommend_period_label.setObjectName(u"recommend_period_label")
        self.recommend_period_label.setGeometry(QRect(30, 30, 100, 16))
        self.entry_label = QLabel(Dialog)
        self.entry_label.setObjectName(u"entry_label")
        self.entry_label.setGeometry(QRect(30, 70, 141, 16))
        self.new_period_entry = QLineEdit(Dialog)
        self.new_period_entry.setObjectName(u"new_period_entry")
        self.new_period_entry.setGeometry(QRect(30, 100, 113, 20))
        self.by_recommend_button = QPushButton(Dialog)
        self.by_recommend_button.setObjectName(u"by_recommend_button")
        self.by_recommend_button.setGeometry(QRect(150, 180, 101, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5f00\u542f\u65b0\u65f6\u6bb5!", None))
        self.by_set_button.setText(QCoreApplication.translate("Dialog", u"by set", None))
        self.recommend_period_label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.entry_label.setText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u6307\u5b9a\u7684period\u7f16\u53f7:", None))
        self.by_recommend_button.setText(QCoreApplication.translate("Dialog", u"by recommend", None))
    # retranslateUi

