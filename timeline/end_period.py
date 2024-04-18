# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'end_period.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(431, 236)
        self.yes_button = QPushButton(Dialog)
        self.yes_button.setObjectName(u"yes_button")
        self.yes_button.setGeometry(QRect(30, 30, 75, 24))
        self.no_button = QPushButton(Dialog)
        self.no_button.setObjectName(u"no_button")
        self.no_button.setGeometry(QRect(30, 100, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u662f\u5426\u7ed3\u675f\u5f53\u524d\u65f6\u6bb5", None))
        self.yes_button.setText(QCoreApplication.translate("Dialog", u"yes", None))
        self.no_button.setText(QCoreApplication.translate("Dialog", u"no", None))
    # retranslateUi

