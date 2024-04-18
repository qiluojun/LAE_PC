'''
基于 db 数据   读取 推荐时长 reminder 
基于 md 文档  读取 抓手
并且可以在对应位置写入
'''

import sqlite3
import os


# D:\\学习and学校\\搞事情\\LAE\\TimeLine2\\file_paths.db

''' 数据来源：

def on_table_view_clicked(self, index):
    self.selected_index = index.row()
'''
# 后文统一用 selected_index作为传递的参数

# 正文： mainwindow.activity=activity_read_write()

class activity_read():
    
    def __init__(self):
        self.md_path=""
        self.pick_up=""
    
    def get_cell_content(self,db_path, table_name, selected_row,selected_column): #可以打印对应行（selected index）任意列的内容
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Select the row based on the selected_index
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1 OFFSET {selected_row}")

        # Fetch the row
        row = cursor.fetchone()

        # Print the content of the third column
        if row:
            cell_content = row[selected_column]  
            
        else:
            print("Row not found.")

        # Close the database connection
        conn.close()
    '''
    db_path = "D:\\学习and学校\\搞事情\\LAE\\TimeLine2\\file_paths.db"
    table_name = "files"  # Replace with the actual table name
    selected_index = 3  # Replace with the desired index

    print_cell_content(db_path, table_name, selected_index)
    '''
    


    def read_pick_up(self):  # 读取 “抓手”
        filename = self.md_path
        
        with open(filename,'r',encoding='utf-8') as f:
            lines = f.readlines()
            pick_up = []
            record = False
            i=0
            for line in lines:
                
                if line.startswith('## 抓手'):
                    record = True
                    i=1
                elif line.startswith('## 实际记录'):
                    record = False
                    i=0
                elif i==1:
                    if "+{" in line:
                        record = False
                    elif "}+" in line:
                        record = True
                    elif record:
                        pick_up.append(line)
        pick_up = ''.join(plapick_upn)
        print(pick_up)

    
        
class activity_write(object):
    def __init__(self, md_path): # 此处塞md的具体地址
        self.md_path=md_path
    def generate_activity_record(self): #用于生成 实际记录板块要写入的字符串参数
        print("还没写好")
    
    '''def md_write_general(self,starting_point,ending_point,writing_content):
            with open(self.md_path, 'r+', encoding='utf-8') as f:
                lines = f.readlines()
                f.seek(0)
                record = False
                for line in lines:
                    if line.startswith(starting_point):
                        record = True
                        f.write(line)
                    elif line.startswith(ending_point):
                        record = False
                        f.write(line)
                    elif not record:
                        f.write(line)
                f.truncate()
                f.write(writing_content)'''
    def md_write_general(self, starting_point, ending_point, writing_content):
        # 在对应位置上 写入对应内容 并且自动换行
        
        with open(self.md_path, 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            f.seek(0)
            record = False
            for line in lines:
                if line.startswith(starting_point):
                    record = True
                    f.write(line)
                elif line.startswith(ending_point):
                    record = False
                    f.write(writing_content)
                    f.write('\n')
                    f.write(line)
                elif not record:
                    f.write(line)
            f.truncate()
            #f.write(writing_content)
test=activity_write("D:/学习and学校/obsidian/qiluo/00-BASE/testtt.md")
test.md_write_general('## 抓手','## 实际记录','asfihaofhi看见我才对！  afhaiodhwi oawiiwi')