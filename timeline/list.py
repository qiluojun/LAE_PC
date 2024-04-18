# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

class Ui_time_period_and_activity(object):
    def setupUi(self, time_period_and_activity):
        if not time_period_and_activity.objectName():
            time_period_and_activity.setObjectName(u"time_period_and_activity")
        time_period_and_activity.resize(740, 499)
        self.activity_list = QListWidget(time_period_and_activity)
        QListWidgetItem(self.activity_list)
        QListWidgetItem(self.activity_list)
        self.activity_list.setObjectName(u"activity_list")
        self.activity_list.setGeometry(QRect(60, 80, 256, 192))

        self.retranslateUi(time_period_and_activity)

        QMetaObject.connectSlotsByName(time_period_and_activity)
    # setupUi

    def retranslateUi(self, time_period_and_activity):
        time_period_and_activity.setWindowTitle(QCoreApplication.translate("time_period_and_activity", u"Dialog", None))

        __sortingEnabled = self.activity_list.isSortingEnabled()
        self.activity_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.activity_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("time_period_and_activity", u"ababab", None));
        ___qlistwidgetitem1 = self.activity_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("time_period_and_activity", u"sdssd", None));
        self.activity_list.setSortingEnabled(__sortingEnabled)

    # retranslateUi

