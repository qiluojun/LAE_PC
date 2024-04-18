
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
        MainWindow.setObjectName("search activity")
        MainWindow.resize(700, 600)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('D:\\学习and学校\\搞事情\\LAE\\TimeLine2\\activity.db')
        self.db.open()

        self.model = QSqlTableModel(db=self.db)
        self.model.setTable('活动')
        #self.model.select()
        if self.model.select():
            self.table_view.setColumnHidden(2,True) 
            self.table_view.setModel(self.model)
        else:
            print("Error: ", self.model.lastError().text())

        self.table_view.clicked.connect(self.on_table_view_clicked)
        self.button.clicked.connect(self.on_button_clicked)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # Connect the search bar's textChanged signal to a custom slot
        self.search_bar.textChanged.connect(self.on_search_bar_text_changed)

    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "aaaa"))

    def on_table_view_clicked(self, index):
        #self.selected_name = self.model.record(index.row()).value("name")
        self.selected_index = index.row()
    def on_button_clicked(self):
        #self.label.setText(self.selected_name)
        self.label.setText(str(self.selected_index))
    def on_search_bar_text_changed(self, text):
        # Filter the model based on the search bar's text
        self.model.setFilter(f"name LIKE '%{text}%'")
        self.model.select()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
