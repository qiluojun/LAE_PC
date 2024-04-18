'''
非常神奇啊
pyside 直接给我把整个db展示出来了 我可以点击任何一个格子 
然后就可以在界面上使用标签把格子里的text 展示出来 六

'''
 

from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import Qt, QMetaObject
import sys

class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.centralwidget)
        self.search_bar = QLineEdit(self.centralwidget)
        self.layout.addWidget(self.search_bar)
        self.table_view = QTableView(self.centralwidget)
        self.layout.addWidget(self.table_view)
        self.label = QLabel(self.centralwidget)
        self.layout.addWidget(self.label)
        self.button = QPushButton("Display Name", self.centralwidget)
        self.layout.addWidget(self.button)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('D:\\学习and学校\\搞事情\\LAE\\TimeLine2\\file_paths.db')
        self.db.open()

            
        self.model = QSqlTableModel(db=self.db)
        self.model.setTable('Files')
        self.model.select()
        if self.model.select():
                self.table_view.setModel(self.model)
        else:
            print("Error: ", self.model.lastError().text())
            
        self.table_view.clicked.connect(self.on_table_view_clicked)
        self.button.clicked.connect(self.on_button_clicked)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "aaaa"))

    def on_table_view_clicked(self, index):
        self.selected_name = self.model.record(index.row()).value("name")

    def on_button_clicked(self):
        self.label.setText(self.selected_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QPushButton { background-color: #4d90fe; border-radius: 10px; }")
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
