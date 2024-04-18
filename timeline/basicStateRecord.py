# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basicStateRecord.ui'
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
        Dialog.resize(400, 300)
        self.yes_button = QPushButton(Dialog)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setGeometry(QRect(20, 250, 75, 24))
        self.tiredness_label = QLabel(Dialog)
        self.tiredness_label.setObjectName(u"tiredness_label")
        self.tiredness_label.setGeometry(QRect(20, 20, 54, 16))
        self.exhaustion_label = QLabel(Dialog)
        self.exhaustion_label.setObjectName(u"exhaustion_label")
        self.exhaustion_label.setGeometry(QRect(20, 60, 54, 16))
        self.anxiety_label = QLabel(Dialog)
        self.anxiety_label.setObjectName(u"anxiety_label")
        self.anxiety_label.setGeometry(QRect(20, 100, 54, 16))
        self.vitality_label = QLabel(Dialog)
        self.vitality_label.setObjectName(u"vitality_label")
        self.vitality_label.setGeometry(QRect(20, 140, 54, 16))
        self.activeness_label = QLabel(Dialog)
        self.activeness_label.setObjectName(u"activeness_label")
        self.activeness_label.setGeometry(QRect(20, 180, 61, 16))
        self.tiredness_entry = QLineEdit(Dialog)
        self.tiredness_entry.setObjectName(u"tiredness_entry")
        self.tiredness_entry.setGeometry(QRect(110, 20, 113, 20))
        self.exhaustion_entry = QLineEdit(Dialog)
        self.exhaustion_entry.setObjectName(u"exhaustion_entry")
        self.exhaustion_entry.setGeometry(QRect(110, 60, 113, 20))
        self.anxiety_entry = QLineEdit(Dialog)
        self.anxiety_entry.setObjectName(u"anxiety_entry")
        self.anxiety_entry.setGeometry(QRect(110, 100, 113, 20))
        self.vitality_entry = QLineEdit(Dialog)
        self.vitality_entry.setObjectName(u"vitality_entry")
        self.vitality_entry.setGeometry(QRect(110, 140, 113, 20))
        self.activeness_entry = QLineEdit(Dialog)
        self.activeness_entry.setObjectName(u"activeness_entry")
        self.activeness_entry.setGeometry(QRect(110, 180, 113, 20))
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bb0\u5f55\u57fa\u7840\u72b6\u6001", None))
        self.yes_button.setText(QCoreApplication.translate("Dialog", u"\u751f\u6210\u8bb0\u5f55", None))
        self.tiredness_label.setText(QCoreApplication.translate("Dialog", u"\u56f0\u5026\u5ea6", None))
        self.exhaustion_label.setText(QCoreApplication.translate("Dialog", u"\u8111\u635f\u5ea6", None))
        self.anxiety_label.setText(QCoreApplication.translate("Dialog", u"\u7126\u8651\u5ea6", None))
        self.vitality_label.setText(QCoreApplication.translate("Dialog", u"\u4f53\u529b\u503c", None))
        self.activeness_label.setText(QCoreApplication.translate("Dialog", u"\u79ef\u6781\u6109\u60a6\u5ea6", None))
    # retranslateUi

