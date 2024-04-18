import sqlite3
from pywinauto import Desktop
import schedule
import time
''' 更新思路 能否做到 检测到新窗口打开 或 旧窗口关闭 然后 触发事件？ 实现：
    #1. 即时窗口名称显示
    #2. 过往窗口历史 （可以根据desktop的名称 来归纳以往的信息）

目前的功能 每10s 读取一次当前窗口列表  这个是根本 似乎没法有更简单的办法了
基于此 可以摸索 找到 新窗口 旧窗口 进行标记哈哈哈 
sqlite NB 比原生的字典好用多了呜呜'''

# Connect to the SQLite database
conn = sqlite3.connect('output.db')
cursor = conn.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS output (app_name TEXT)")

# Function to check for new windows and record them in the database
def check_for_new_windows():
    # Get the current window names
    windows = Desktop(backend="uia").windows()
    current_names = set(w.window_text() for w in windows if w.window_text().strip())

    # Retrieve the existing window names from the database
    cursor.execute("SELECT app_name FROM output")
    existing_names = set(row[0] for row in cursor.fetchall())

    # Find the new window names
    new_names = current_names - existing_names

    # Insert the new window names into the database
    for name in new_names:
        cursor.execute("INSERT INTO output (app_name) VALUES (?)", (name,))

    # Commit the changes
    conn.commit()

# Schedule the check_for_new_windows function to run every 10 seconds
schedule.every(10).seconds.do(check_for_new_windows)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)

# Close the connection (this will never be reached in this infinite loop)
conn.close()