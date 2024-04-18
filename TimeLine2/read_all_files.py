'''
功能： 读取给定位置的文件夹里的所有文件内容 记录其名称 和地址 
自动省略.md后缀 且文件夹和md重名时保留后者
并且自动提取 location的值~ 
'''

'''
import os
import sqlite3

def process_folder(folder_path, cursor):
    for root, dirs, files in os.walk(folder_path):
       for name in files:
            file_path = os.path.join(root, name)
            name_without_ext, ext = os.path.splitext(name)
            if ext == '.md':
                location = name_without_ext.split('-')[0]
                cursor.execute("INSERT INTO Files (name, path,location) VALUES (?, ?, ?)", (name_without_ext, file_path,location))
        
       for name in dirs:
            dir_path = os.path.join(root, name)
            md_file_path = os.path.join(dir_path, name + '.md')
            
            # Only process the folder if there's no .md file with the same name inside it
            if not os.path.isfile(md_file_path):
                location = name.split('-')[0]  # Extract the number before the '-'
                cursor.execute("INSERT INTO Files (name, path, location) VALUES (?, ?, ?)", (name, dir_path, location))

# 这里可以修改读取的文件夹路径
folder_paths = [
    r"D:\学习and学校\obsidian\qiluo\1-学业与未来",
    r"D:\学习and学校\obsidian\qiluo\2-自由学习与探索",
    r"D:\学习and学校\obsidian\qiluo\3-LAE其他",
    
]
# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('file_paths.db')

# Create a cursor object
cursor = conn.cursor()

# Create a new table named 'Files' with two columns: 'name' and 'path'
cursor.execute("CREATE TABLE IF NOT EXISTS Files (name TEXT, path TEXT, location TEXT)")

# Clear old data from the table
cursor.execute("DELETE FROM Files")

# Define the folder paths
folder_paths = [
    r"D:\学习and学校\obsidian\qiluo\1-学业与未来",
    r"D:\学习and学校\obsidian\qiluo\2-自由学习与探索",
    r"D:\学习and学校\obsidian\qiluo\3-LAE其他"
]

for folder_path in folder_paths:
    # Process the folder and save the information to the database
    process_folder(folder_path, cursor)

# Commit the changes and close the connection
conn.commit()
conn.close()
'''


import os
import sqlite3
import random

def process_folder(folder_path, cursor):
    for root, dirs, files in os.walk(folder_path):
       for name in files:
            file_path = os.path.join(root, name)
            name_without_ext, ext = os.path.splitext(name)
            if ext == '.md':
                location = name_without_ext.split('-')[0]
                cursor.execute("INSERT INTO tem (name, path, location（基于内容）, 推荐时长（基于内容）, reminder（基于内容）) VALUES (?, ?, ?, ?, ?)", (name_without_ext, file_path, location, '', ''))
        
       for name in dirs:
            dir_path = os.path.join(root, name)
            md_file_path = os.path.join(dir_path, name + '.md')
            
            if not os.path.isfile(md_file_path):
                location = name.split('-')[0]
                cursor.execute("INSERT INTO tem (name, path, location（基于内容）, 推荐时长（基于内容）, reminder（基于内容）) VALUES (?, ?, ?, ?, ?)", (name, dir_path, location, '', ''))

folder_paths = [
    r"D:\学习and学校\obsidian\qiluo\1-学业与未来",
    r"D:\学习and学校\obsidian\qiluo\2-自由学习与探索",
    r"D:\学习and学校\obsidian\qiluo\3-LAE其他",
]

conn = sqlite3.connect('activity - 副本.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS tem (name TEXT, path TEXT, location（基于内容） TEXT, 推荐时长（基于内容） TEXT, reminder（基于内容） TEXT)")
cursor.execute("DELETE FROM tem")

for folder_path in folder_paths:
    process_folder(folder_path, cursor)

rows = cursor.execute("SELECT name FROM 活动内容 WHERE name NOT IN (SELECT name FROM tem)").fetchall()

for row in rows:
    cursor.execute("""
        UPDATE 活动内容
        SET location（基于内容） = ?
        WHERE name = ?
    """, ("not exist:" + str(random.randint(10000, 99999)), row[0]))
cursor.execute("""
    INSERT OR REPLACE INTO 活动内容 (name, path, location（基于内容）, 推荐时长（基于内容）, reminder（基于内容）)
    SELECT name, path, location（基于内容）, 推荐时长（基于内容）, reminder（基于内容） FROM tem
    WHERE name NOT IN (SELECT name FROM 活动内容)
""")

cursor.execute("DROP TABLE IF EXISTS tem")

conn.commit()
conn.close()
 
'''
要么取消主键 要么？？？
'''