from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, 
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget, QDoubleSpinBox,QMessageBox)


from writeID import insert_id

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
    
    
    
    # 先找到需要更新的行：临时表与活动内容_简表中同id但name或path不同的行
    cursor.execute("""
        SELECT 活动内容_简.id, temp_table.name AS new_name, 活动内容_简.name AS old_name
        FROM temp_table
        JOIN 活动内容_简 ON temp_table.id = 活动内容_简.id
        WHERE temp_table.name != 活动内容_简.name OR temp_table.path != 活动内容_简.path
    """)
    rows_to_update = cursor.fetchall()

    # 对于每个这样的行，先更新其他表，再更新活动内容_简表中的name
    for id, new_name, old_name in rows_to_update:
        if old_name:
            # 更新activity表中的content_location
            cursor.execute("UPDATE activity SET content_location = ? WHERE content_location = ?", (new_name, old_name))
            # 更新activity_record表中的content_location
            cursor.execute("UPDATE activity_record SET content_location = ? WHERE content_location = ?", (new_name, old_name))
            # 更新活动内容_简表中的name
            cursor.execute("UPDATE 活动内容_简 SET name = ? WHERE id = ?", (new_name, id))

    # 最后，更新活动内容_简表中的path，以匹配临时表中的新path
    cursor.execute("""
        UPDATE 活动内容_简
        SET path = (SELECT path FROM temp_table WHERE 活动内容_简.id = temp_table.id)
        WHERE EXISTS (
            SELECT 1 
            FROM temp_table 
            WHERE 活动内容_简.id = temp_table.id 
            AND 活动内容_简.path != temp_table.path
        )
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

class InsertIdDialog(QDialog):
    def __init__(self, parent=None):
        super(InsertIdDialog, self).__init__(parent)
        self.setWindowTitle("InsertId")
        self.setGeometry(100, 100, 300, 200)
        

        
        self.name_label = QLabel("MD Name:", self)
        self.name_label.setGeometry(10, 60, 60, 30)
        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(70, 60, 200, 30)
        
        self.insert_button = QPushButton("Update", self)
        self.insert_button.setGeometry(100, 100, 100, 30)
        self.insert_button.clicked.connect(self.InsertId)

    def InsertId(self):
        md_name = self.name_input.text()
        
        
        conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
        cursor = conn.cursor()
        # 获取旧的name
        cursor.execute("SELECT path FROM 活动内容_简 WHERE name = ?", (md_name,))
        path = cursor.fetchone()
        path=path[0]
        conn.commit()
        conn.close()
        
        insert_id(path)
        QMessageBox.information(self, "Success", "id inserted successfully.")
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

        self.insert_id_button = QPushButton("insert id", Dialog)
        self.insert_id_button.setGeometry(QRect(20, 80, 200, 30))
        
        
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
        self.ui.insert_id_button.clicked.connect(self.show_InsertIdDialog_dialog)
        #self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint) 
    def show_InsertIdDialog_dialog(self):
        self.dialog = InsertIdDialog(self)
        self.dialog.show()













    
    
# 启动窗口
app = QApplication(sys.argv)

main_window=db_modification_window()

# 显示主窗口 
main_window.show()

app.exec()



