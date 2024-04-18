from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *


from datetime import timedelta
import datetime
import sys



class Ui_settlement(object):  # from reminder_finalversion.py
    '''def set_layout_visible(self, layout, visible):
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.setVisible(visible)'''


    def __init__(self,settlementWindow):
        self.centralwidget = QWidget(settlementWindow)
        self.layout = QHBoxLayout(self.centralwidget)

        # 左边的布局
        self.left_layout = QVBoxLayout()
        self.layout.addLayout(self.left_layout, 1)

        # 左边布局的控件
        self.view_button = QPushButton("查看")
        self.main_side_line_list = QListWidget()

        # 添加内容位置项
        self.main_side_line_list.addItem(QListWidgetItem("12-what to do"))
        self.main_side_line_list.addItem(QListWidgetItem("32-live and have fun--LAE!"))

        # 当选中内容位置项时，显示相应的活动记录
        self.main_side_line_list.itemClicked.connect(self.display_activity_records)

        self.left_layout.addWidget(self.view_button)
        self.left_layout.addWidget(self.main_side_line_list)

        # 右边的布局
        self.right_layout = QVBoxLayout()
        self.layout.addLayout(self.right_layout, 1)

        # 右边布局的控件
        self.activity_record_table = QTableView()
        self.right_layout.addWidget(self.activity_record_table)
        
        self.db = QSqlDatabase.addDatabase("QSQLITE", "my_connection")
        self.db.setDatabaseName(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
        self.db.open()
        
        settlementWindow.setCentralWidget(self.centralwidget)
        settlementWindow.resize(1000, 600)

    def setupUi(self):
        pass

    def display_activity_records(self, item):
        # 连接到SQLite数据库
        location_id = item.text().split("-")[0]


        
        
        
        
        if self.db.open():
            # 创建模型
            model = QSqlTableModel(db=self.db)
            model.setTable("activity_record")
            model.setFilter(f"content_location LIKE '{location_id}%'")
            model.select()

            query = QSqlQuery()
            query.exec(f"SELECT actual_duration FROM activity_record WHERE content_location LIKE '{location_id}%'")
            # 计算总计时
            total_time = timedelta()
            while query.next():
                time_str = query.value("actual_duration")
                h, m, s = map(int, time_str.split(":"))
                total_time += timedelta(hours=h, minutes=m, seconds=s)

            # 添加到列表中
            item = QListWidgetItem(item.text() + " <font color='gray'>" + str(total_time) + "</font>")
            self.main_side_line_list.addItem(item)
            

            # 将模型设置到表格视图
            self.activity_record_table.setModel(model)



    def retranslateUi(self, settlementWindow):
        _translate = QApplication.translate
        # 窗口名称
        settlementWindow.setWindowTitle(_translate("活动结算", "TIMELINE2"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    settlementWindow = QMainWindow()
    ui = Ui_settlement(settlementWindow)
    ui.setupUi()
    settlementWindow.show()
    sys.exit(app.exec())
    