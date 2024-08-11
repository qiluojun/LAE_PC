
from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import sqlite3
import sys
from pynput import keyboard
import pyperclip
from datetime import datetime, timedelta












class Ui_period_end(object):  
    
    
    def __init__(self,period_end_window):
        #变量初始化
        self.current_period=None

    def setuiUi(self,current_period):
        self.current_period=current_period
        # 根据具体的时段 来弹出结算窗口