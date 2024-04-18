from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtGui import *
import sys
import sqlite3

class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QWidget(MainWindow)
        self.layout = QHBoxLayout(self.centralwidget)
        self.left_layout=QVBoxLayout()
        self.right_layout=QVBoxLayout()
        
        self.change_input_layout=QHBoxLayout()
        self.new_delete_layout=QHBoxLayout()
        
        self.table_view_activity_content = QTableView()
        self.table_view_activity_type = QTableView()

        self.button_change_value = QPushButton("change_value")
        self.input_bar = QLineEdit(self.centralwidget)
        self.button_new_row = QPushButton("new_row")
        self.button_delete_row = QPushButton("delete_row")
        self.table_view_activity = QTableView()
        
        self.left_layout.addWidget(self.table_view_activity_content)
        self.left_layout.addWidget(self.table_view_activity_type)
        
    
        
        self.change_input_layout.addWidget(self.button_change_value)
        self.change_input_layout.addWidget(self.input_bar)
        self.new_delete_layout.addWidget(self.button_new_row)
        self.new_delete_layout.addWidget(self.button_delete_row)
        self.right_layout.addLayout(self.change_input_layout)
        self.right_layout.addLayout(self.new_delete_layout)
        self.right_layout.addWidget(self.table_view_activity)
        
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(self.right_layout)
        

        
        
        
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("search activity")
        MainWindow.resize(700, 600)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 读取数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('D:\\学习and学校\\搞事情\\LAE\\TimeLine2\\activity - 副本 - 副本.db')
        self.db.open()

        self.model_activity = QSqlTableModel(db=self.db)
        self.model_activity.setTable('活动')
        self.model_activity.select()
        self.model_activity_content = QSqlTableModel(db=self.db)
        self.model_activity_content.setTable('活动内容')
        self.model_activity_content.select()
        self.model_activity_type = QSqlTableModel(db=self.db)
        self.model_activity_type.setTable('活动类型')
        self.model_activity_type.select()
        # 连接table view  和 数据库
        # self.table_view.setColumnHidden(2,True)  用来隐藏某一列
        self.table_view_activity.setModel(self.model_activity)
        self.table_view_activity_content.setModel(self.model_activity_content)
        self.table_view_activity_type.setModel(self.model_activity_type)
        
        ''' 给各按钮上功能咯！ '''
        
        # 首先 给表 安基本功能
        self.table_view_activity.clicked.connect(self.on_table_view_activity_clicked)
        self.table_view_activity_content.clicked.connect(self.on_table_view_activity_content_clicked)
        self.table_view_activity_type.clicked.connect(self.on_table_view_activity_type_clicked)
        
        #self.model_activity.dataChanged.connect(self.test)
        
        # 给 按钮 按功能
        self.button_change_value.clicked.connect(self.on_click_button_change_value)
        self.button_delete_row.clicked.connect(self.update_when_deleted)
        #self.button_new_row.clicked.connect(self.insert_new_row)





        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
        

    '''获得所点击格子的所有信息！好耶！'''    
    def on_table_view_activity_clicked(self,index): 
        self.table_clicked= '活动'
        # Get the value in the clicked cell
        self.click_value = self.model_activity.data(index)

        # Get the row index and column index of the clicked cell
        self.click_row_index = index.row() 
        self.click_column_index = index.column() 

        # Get the name of the row and column
        self.click_row_name = self.model_activity.headerData(self.click_row_index, Qt.Vertical)
        self.click_column_name = self.model_activity.headerData(self.click_column_index, Qt.Horizontal)
        print(self.click_column_index)
    def on_table_view_activity_content_clicked(self,index): #获得所点击格子的所有信息！好耶！
        self.table_clicked= '活动内容'
        # Get the value in the clicked cell
        self.click_value = self.model_activity_content.data(index)

        # Get the row index and column index of the clicked cell
        self.click_row_index = index.row()
        self.click_column_index = index.column()

        # Get the name of the row and column
        self.click_row_name = self.model_activity_content.headerData(self.click_row_index, Qt.Vertical)
        self.click_column_name = self.model_activity_content.headerData(self.click_column_index, Qt.Horizontal)
    def on_table_view_activity_type_clicked(self,index): #获得所点击格子的所有信息！好耶！
        self.table_clicked= '活动类型'
        # Get the value in the clicked cell
        self.click_value = self.model_activity_type.data(index)

        # Get the row index and column index of the clicked cell
        self.click_row_index = index.row()
        self.click_column_index = index.column()

        # Get the name of the row and column
        self.click_row_name = self.model_activity_type.headerData(self.click_row_index, Qt.Vertical)
        self.click_column_name = self.model_activity_type.headerData(self.click_column_index, Qt.Horizontal)

    '''function 3.1-4'''
    def refresh(self):# Update the model to reflect the changes
        self.model_activity.select()
        self.model_activity_content.select()
        self.model_activity_type.select()
    
    
    
    def write_value_to_cell(self):
        conn = sqlite3.connect('activity - 副本 - 副本.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {self.table_clicked} SET {self.click_column_name} = ? WHERE rowid = ?", (self.value_input, self.click_row_index+1))
        print("write 函数执行了这一步")
        conn.commit()
        conn.close()
        self.refresh()
        print("write is done")
    def delete_row(self):
        conn = sqlite3.connect('activity - 副本 - 副本.db')
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {self.table_clicked} WHERE rowid = ?", (self.click_row_index +1,))
        conn.commit()
        conn.close()
        self.refresh()
    def autoFill_activity_table_on_location(self): # 3.1   
        conn = sqlite3.connect('activity - 副本 - 副本.db')
        cursor = conn.cursor()
        
        
        if self.click_column_name == 'location（基于内容）':
            motherTable = '活动内容'
            column_to_get1='reminder（基于内容）'
            column_to_get2='推荐时长（基于内容）'
        elif self.click_column_name == 'location（基于类型）':
            print("tyoe")
            motherTable = '活动类型'
            column_to_get1='reminder（基于类型）'
            column_to_get2='推荐时长（基于类型）'            

        
        # 得到数值
        cursor.execute(f"SELECT {column_to_get1} FROM {motherTable} WHERE {self.click_column_name } = ?", (self.value_input,))
        if cursor.fetchone():
            reminder = cursor.fetchone()[0]
        cursor.execute(f"SELECT {column_to_get2} FROM {motherTable} WHERE {self.click_column_name } = ?", (self.value_input,))
        if cursor.fetchone():
            time = cursor.fetchone()[0]
        # 写入对应位置
        cursor.execute(f"UPDATE 活动 SET {column_to_get1} = ? WHERE rowid = ?", (reminder, self.click_row_index +1))
        cursor.execute(f"UPDATE 活动 SET {column_to_get2} = ? WHERE rowid = ?", (time, self.click_row_index +1))
        
        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()
        self.refresh()

    def autoUpdate_activity_table_on_MotherTable(self):     # 3.2 
        conn = sqlite3.connect('activity - 副本 - 副本.db')
        cursor = conn.cursor()
        
        if self.table_clicked == '活动内容':
            location_name= 'location（基于内容）'
            column_to_get1='reminder（基于内容）'
            column_to_get2='推荐时长（基于内容）'
        if  self.table_clicked == '活动类型':
            
            location_name= 'location（基于类型）' 
            column_to_get1='reminder（基于类型）'
            column_to_get2='推荐时长（基于类型）'
        cursor.execute(f"SELECT {location_name} FROM {self.table_clicked} WHERE rowid = ?", (self.click_row_index +1,))
        find=cursor.fetchone()
        if find is not None:
            location = find[0]
            
            # 得到数值
            cursor.execute(f"SELECT {column_to_get1} FROM {self.table_clicked} WHERE {location_name} = ?", (location,))
            reminder = cursor.fetchone()[0]
            cursor.execute(f"SELECT {column_to_get2} FROM {self.table_clicked} WHERE {location_name} = ?", (location,))
            time = cursor.fetchone()[0]
            # 写入对应位置
            cursor.execute(f"UPDATE 活动 SET {column_to_get1} = ? WHERE {location_name} = ?", (reminder, location))
            cursor.execute(f"UPDATE 活动 SET {column_to_get2} = ? WHERE {location_name} = ?", (time, location))
            
            # Commit the changes
            conn.commit()
        # Close the connection
        conn.close()
        self.refresh()        
        
    def update_when_deleted(self):  #3.3
        #先检查 再删！
        conn = sqlite3.connect('activity - 副本 - 副本.db')
        cursor = conn.cursor()
        if self.table_clicked in ('活动内容' , '活动类型'):
            if self.table_clicked == '活动内容':
                location_name='location（基于内容）'
            else: location_name='location（基于类型）'
            
            cursor.execute(f"SELECT {location_name} FROM {self.table_clicked} WHERE rowid = ?", (self.click_row_index+1,))
            location = cursor.fetchone()[0]
            cursor.execute(f"SELECT {location_name} FROM 活动 WHERE {location_name} = ?", (location,))
            if cursor.fetchone(): find = location
            else:  find  = None
            
        
        if not (find is None):
            QMessageBox.warning(self.centralwidget,"注意", "活动表有被修改到")
            cursor.execute(f"UPDATE 活动 SET {location_name} = 'deleted' WHERE {location_name} = ?", (find,))

        # Commit the changes
        conn.commit()
        # Close the connection
        conn.close()
        self.delete_row()
        self.refresh()   
            
    def change_motherTable_location(self):  #3.4    
        conn = sqlite3.connect('activity - 副本 - 副本.db.db')
        cursor = conn.cursor()
        print(self.table_clicked,self.click_column_name)
        cursor.execute(f"SELECT {self.click_column_name} FROM 活动 WHERE {self.click_column_name} = ?",(self.click_value,))
        find = cursor.fetchone()
        if find:
            QMessageBox.warning(self.centralwidget,"注意", "活动表有被修改到")
            cursor.execute(f"UPDATE 活动 SET {self.click_column_name} = ? WHERE {self.click_column_name} = ?", (self.value_input,self.click_value))
        else: print("mother函数执行了 然后find是空")
        conn.commit()
        # Close the connection
        conn.close()
        self.refresh()   

        
        
    '''button的功能和函数逻辑分支'''
    def on_click_button_change_value(self):
        self.value_input = self.input_bar.text()
        self.write_value_to_cell()
        
        '''if self.table_clicked in ('活动内容' , '活动类型'):
            if self.click_column_name in ('location（基于内容）' , 'location（基于类型）'):
                print("3.4")
                self.change_motherTable_location()
            else: 
                print("3.2")
                self.autoUpdate_activity_table_on_MotherTable()
        else:
            if  self.click_column_name in ('location（基于内容）' , 'location（基于类型）'):
                self.autoFill_activity_table_on_location()'''
    
    def on_click_button_delete_row(self):
        if self.table_clicked in ('活动内容' , '活动类型'):
            print('func_3_3()')
    
    '''我目前的想法是 根据 test的零散语句 把func3.1 2 3 4 写出来 然后这里import？'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def retranslateUi(self, MainWindow):
        _translate = QApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "read_files"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())






'''
class childFunctions(object):
    def __init__(self):
        self.table_clicked 
        self.click_value

        self.click_row_index 
        self.click_column_index 

       
        self.click_row_name 
        self.click_column_name 
        
        location（基于内容）  location_content
        location（基于类型）  location_type
        reminder（基于内容）  reminder_content
        reminder（基于类型）  reminder_type
        推荐时长（基于内容）  time_content
        推荐时长（基于类型）  time_type
   '''     
    