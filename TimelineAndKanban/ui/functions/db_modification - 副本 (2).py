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
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                    lae_index = None
                    for i, line in enumerate(lines):
                        if line.strip() == "# LAE 用":
                            lae_index = i
                            break
                    if lae_index is not None and lae_index + 1 < len(lines) and lines[lae_index + 1].strip().startswith("【id】"):
                        id = lines[lae_index + 1].strip()[4:]
                        cursor.execute("INSERT INTO temp_table (id, name, path) VALUES (?, ?, ?)", (id, name_without_ext, file_path))
                    else:
                        cursor.execute("INSERT INTO temp_table (name, path) VALUES (?, ?)", (name_without_ext, file_path))
            
            for name in dirs:
                dir_path = os.path.join(root, name)
                md_file_path = os.path.join(dir_path, name + '.md')
                
                if not os.path.isfile(md_file_path):
                    cursor.execute("INSERT INTO temp_table (name, path) VALUES (?, ?)", (name, dir_path))

    folder_paths = [
        r"D:\学习and学校\obsidian\qiluo\1-学业与未来",
        r"D:\学习and学校\obsidian\qiluo\2-自由学习与探索",
        r"D:\学习and学校\obsidian\qiluo\3-LAE其他",
    ]

    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 活动内容_简 (id TEXT, name TEXT, path TEXT)")
    cursor.execute("CREATE TEMPORARY TABLE temp_table (id TEXT, name TEXT, path TEXT)")
    for folder_path in folder_paths:
        process_folder(folder_path, cursor)

    # 删除原表中不存在于临时表中的行
    cursor.execute("DELETE FROM 活动内容_简 WHERE id NOT IN (SELECT id FROM temp_table) OR id IS NULL")
    # 插入临时表中新的行到原表
    cursor.execute("INSERT INTO 活动内容_简 (id, name, path) SELECT id, name, path FROM temp_table WHERE id NOT IN (SELECT id FROM 活动内容_简) OR id IS NULL")
    # 更新原表中存在于临时表中的行的name和path
    cursor.execute("""
        UPDATE 活动内容_简
        SET name = (SELECT name FROM temp_table WHERE 活动内容_简.id = temp_table.id),
            path = (SELECT path FROM temp_table WHERE 活动内容_简.id = temp_table.id)
        WHERE EXISTS (SELECT 1 FROM temp_table WHERE 活动内容_简.id = temp_table.id AND (活动内容_简.name != temp_table.name OR 活动内容_简.path != temp_table.path))
    """)
    cursor.execute("DROP TABLE temp_table")

    conn.commit()
    conn.close()





'''修改 location 的时候 顺便修改其他的表中的对应内容'''
def update_other_table(id, new_name):
    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()
    
    
    # 获取旧的name
    cursor.execute("SELECT name FROM 活动内容_简 WHERE id = ?", (id,))
    old_name = cursor.fetchone()
    
    # 更新活动内容_简表中的name
    cursor.execute("UPDATE 活动内容_简 SET name = ? WHERE id = ?", (new_name, id))
    
    
    
    
    if old_name:
        old_name = old_name[0]
        print("old_name",old_name)
        # 更新activity表中的content_location
        cursor.execute("UPDATE activity SET content_location = ? WHERE content_location = ?", (new_name, old_name))
        # 更新activity_record表中的content_location
        cursor.execute("UPDATE activity_record SET content_location = ? WHERE content_location = ?", (new_name, old_name))
    
    conn.commit()
    conn.close()












'''ui'''

class UpdateOtherTableDialog(QDialog):
    def __init__(self, parent=None):
        super(UpdateOtherTableDialog, self).__init__(parent)
        self.setWindowTitle("Update Other Table")
        self.setGeometry(100, 100, 300, 200)
        
        self.id_label = QLabel("ID:", self)
        self.id_label.setGeometry(10, 20, 60, 30)
        self.id_input = QLineEdit(self)
        self.id_input.setGeometry(70, 20, 200, 30)
        
        self.name_label = QLabel("New Name:", self)
        self.name_label.setGeometry(10, 60, 60, 30)
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(70, 60, 200, 30)
        
        self.update_button = QPushButton("Update", self)
        self.update_button.setGeometry(100, 100, 100, 30)
        self.update_button.clicked.connect(self.update_table)

    def update_table(self):
        id = self.id_input.text()
        new_name = self.name_input.text()
        update_other_table(id, new_name)
        QMessageBox.information(self, "Success", "Table updated successfully.")
        self.close()




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

        self.update_other_table_button = QPushButton("Update Other Table", Dialog)
        self.update_other_table_button.setGeometry(QRect(20, 80, 200, 30))
        
        
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
        self.ui.update_other_table_button.clicked.connect(self.show_update_other_table_dialog)
        #self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) 
    def show_update_other_table_dialog(self):
        self.dialog = UpdateOtherTableDialog(self)
        self.dialog.show()













    
    
# 启动窗口
app = QApplication(sys.argv)

main_window=db_modification_window()

# 显示主窗口 
main_window.show()

app.exec()



