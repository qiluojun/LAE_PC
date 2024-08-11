from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, 
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QDoubleSpinBox,QMessageBox)




import sys
import sqlite3
import os



''' part 1  自动写 活动内容_简  '''
def update_activity_sim():
    def process_folder(folder_path, cursor):
        for root, dirs, files in os.walk(folder_path):
            for name in files:
                file_path = os.path.join(root, name)
                name_without_ext, ext = os.path.splitext(name)
                if ext == '.md':
                    #location = name_without_ext.split('-')[0]
                    cursor.execute("INSERT INTO 活动内容_简 (name, path) VALUES (?, ?)", (name_without_ext, file_path))
            
            for name in dirs:
                dir_path = os.path.join(root, name)
                md_file_path = os.path.join(dir_path, name + '.md')
                
                if not os.path.isfile(md_file_path):
                    #location = name.split('-')[0]
                    cursor.execute("INSERT INTO 活动内容_简 (name, path) VALUES (?, ?)", (name, dir_path))

    folder_paths = [
        r"D:\学习and学校\obsidian\qiluo\1-学业与未来",
        r"D:\学习and学校\obsidian\qiluo\2-自由学习与探索",
        r"D:\学习and学校\obsidian\qiluo\3-LAE其他",
    ]

    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM 活动内容_简")
    cursor.execute("CREATE TABLE IF NOT EXISTS 活动内容_简 (name TEXT, path TEXT)")
    for folder_path in folder_paths:
        process_folder(folder_path, cursor)


    conn.commit()
    conn.close()












class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 400)
        self.update_activity_sim_button = QPushButton(Dialog)
        self.update_activity_sim_button.setObjectName(u"update_activity_sim_button")
        self.update_activity_sim_button.setGeometry(QRect(20, 50, 75, 24))
        
        
        self.update_activity_sim_label = QLabel(Dialog)
        self.update_activity_sim_label.setObjectName(u"update_activity_sim_label")
        self.update_activity_sim_label.setGeometry(QRect(20, 20, 120, 16))


        
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bb0\u5f55\u57fa\u7840\u72b6\u6001", None))
        self.update_activity_sim_button.setText(QCoreApplication.translate("Dialog", u"yes", None))
        
        self.update_activity_sim_label.setText(QCoreApplication.translate("Dialog", u"更新：活动内容_简", None))
        self.update_activity_sim_button.clicked.connect(self.show_message)
    # retranslateUi
    def show_message(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("已成功刷新表")
        msgBox.setStandardButtons(QMessageBox.Ok)
        QTimer.singleShot(500, msgBox.accept)  # 0.5 seconds
        msgBox.exec()




class db_modification_window(QDialog):
    def __init__(self):
        super().__init__()
 # 使用ui文件，导入定义的界面类
        self.ui = Ui_Dialog()
 # 初始化界面
        self.ui.setupUi(self)   
        self.ui.update_activity_sim_button.clicked.connect(update_activity_sim)
        #self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        
    
    
# 启动窗口
app = QApplication(sys.argv)

main_window=db_modification_window()

# 显示主窗口 
main_window.show()

app.exec()



