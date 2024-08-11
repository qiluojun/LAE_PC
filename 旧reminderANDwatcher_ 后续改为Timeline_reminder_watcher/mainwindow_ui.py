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

class MultiLineSqlTableModel(QSqlTableModel):
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and index.column() == self.fieldIndex("name"):  # 假设"name"是需要换行的列
            text = super().data(index, role)
            # 根据需要将文本分割为多行
            # 这里的示例仅为了演示，可能需要根据实际文本内容调整
            return '\n'.join(text[i:i+20] for i in range(0, len(text), 20))
        return super().data(index, role)
        

class Ui_MainWindow(object):  # from reminder_finalversion.py

    def __init__(self,MainWindow):
        # 主界面初始化-- 左右分半
        
        
        self.centralwidget = QWidget(MainWindow)
        self.layout=QHBoxLayout(self.centralwidget)
        # Create a layout for the frame
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout,2)
        self.layout.addLayout(self.right_layout,1)
           
        # 创建界面
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1440, 773)
        MainWindow.resize(1000, 600)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
		
	
		# 设置左半边： 没想好干啥 先占个空
        # 创建控件 
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("D:/学习and学校/搞事情/LAE/TimelineAndKanban/activity.db")
        if not self.db.open():
            QMessageBox.critical(None, "Cannot open database",
                "Unable to establish a database connection.\nThis example needs SQLite support. Please read "
                "the Qt SQL driver documentation for information how to build it.\n\n"
                "Click Cancel to exit.", QMessageBox.Cancel)
            return

        # Display the "goals" table
        self.model_goals = MultiLineSqlTableModel(self.centralwidget, self.db)
        self.model_goals.setTable("goals")
        self.model_goals.select()
        
        self.model_expectations= MultiLineSqlTableModel(self.centralwidget, self.db)
        self.model_expectations.setTable("expectations")
        self.model_expectations.select()
        
        self.goals_table_view = QTableView(self.centralwidget)
        self.goals_table_view.setModel(self.model_goals)
        self.goals_table_view.resizeRowsToContents()
        self.goals_table_view.setSortingEnabled(True)

        self.expectations_table_view =QTableView(self.centralwidget)
        self.expectations_table_view.setModel(self.model_expectations)
        self.expectations_table_view.resizeRowsToContents()
        self.expectations_table_view.setSortingEnabled(True)
        # 安排位置

        self.left_layout.addWidget(self.goals_table_view)
        self.left_layout.addWidget(self.expectations_table_view)
        
        # 设置右半边
        # 创建控件 
        
        # 设置右半边
        # 创建控件 
        self.reminder_label = QLabel(self.centralwidget)
        #reminder = '<p>&nbsp;最近心态比较脆<br /><span> </span><strong><span style="font-size:2px;color:#E53333;">&nbsp;超！LAE快了！艹！太好啦！！但是一旦 知乎 b站 小说 漫画 你绝对会心态爆炸！</span></strong>加油！<br /><span> </span>&nbsp;你所恐惧的害怕的痛苦 都是焦虑狗剩带来的！<br />一定坚守体系！开好时段！<span style="font-size:16px;color:#00D5FF;"><strong>提前做好规划！！</strong></span></p><p>加油！！！</p>'
        reminder = ('<p style="text-align:center;">'
	                '<span style="font-size:24px;color:#E53333;"><strong>check point 3.3！</strong></span><span style="font-size:16px;">并且有一次爆破期！</span>'
                    '</p>'
                    '<p style="text-align:center;">'
                    '<strong><span style="font-size:16px;">焦虑狗剩才是最痛苦的事情！直接去做反而蛮开心！</span></strong>'
                    '</p>'
                    '<p style="text-align:center;">'
                    '<span style="font-size:16px;">请严格防止焦虑狗剩出现，以及注意运动和睡眠！</span>'
                    '</p>'
                    '<p style="text-align:center;">'
                    '<span style="color:#4C33E5;"><span style="font-size:16px;">近期很容易出现沮丧焦虑自我怀疑等情绪--都是</span><strong><span style="font-size:16px;">friction</span></strong><span style="font-size:16px;">！</span></span> '
                    '</p>'
                    '<p style="text-align:center;">'
                    '<span style="font-size:16px;">尽力去做就完了！加油！</span>'
                    '</p>')
        self.reminder_label.setText(reminder)
        self.reminder_label.setTextFormat(Qt.RichText)  # Enable rich text formatting
        self.right_layout.addWidget(self.reminder_label)
        
       
        self.retranslateUi( MainWindow)
        QMetaObject.connectSlotsByName( MainWindow)

    
    def setupUi(self):
            
        pass
    
    
    

    def retranslateUi(self,  MainWindow):
        _translate = QApplication.translate
        # 窗口名称
        MainWindow.setWindowTitle(_translate("reminderANDwatcher", "reminderANDwatcher"))


 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec())


# 进度 左半边窗口 功能搞定~
