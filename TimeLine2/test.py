import sqlite3

# Connect to the database
conn = sqlite3.connect('activity - 副本.db')
cursor = conn.cursor()
row_index=3

'''

# Execute the SQL query to select the value from table2
cursor.execute(f"SELECT reminder（基于内容） FROM {table2} WHERE {column1} = ?", (matching_value,))
result = cursor.fetchone()


把上面的语句放进来 #测试没问题的话# 就可以抽象成一个高度抽象的函数：
给定 某个表A  从表B中 读取某行某列值 塞入表A的某行某列中！！  好耶！！！


'''


# 得到 某行/某列的名称
    #行
cursor.execute(f"SELECT name FROM pragma_table_info('{table_name}') WHERE cid = ?", (row_index,))
row_name = cursor.fetchone()[0]
    # 列：
cursor.execute(f"PRAGMA table_info('{table_name}')")
columns = cursor.fetchall()
column_name = columns[column_index][1]


# 删行
# Delete the row identified by row_index
cursor.execute("DELETE FROM table_name WHERE rowid = ?", (row_index,))

# 插入新行
    # Get the rowid of the row below rowA
cursor.execute("SELECT rowid FROM table_name WHERE condition")
row_below_rowA = cursor.fetchone()[0]
cursor.execute("INSERT INTO table_name (column1, column2) VALUES (?, ?)", (value1, value2, row_below_rowA))



# 得到数值
    #从 表B 的 行 row_index 中 提取 列 = matching_value 的 一行
cursor.execute(f"SELECT 某行 FROM {表B} WHERE {某列} = ?", (matching_value,))
get_result = cursor.fetchone()[0]

# 改数值
# 把数据 insert_value 放进 表A 的 某一行中 

cursor.execute("UPDATE 表A SET 被更新的列 = ? WHERE rowid = ?", (insert_value, 某一行))







# Get the matching value from table1's column A
cursor.execute("SELECT location（基于内容） FROM 活动 WHERE rowid = ?", (row_index,))
matching_value = cursor.fetchone()[0]

# Execute the SQL query to select the value from table2
cursor.execute("SELECT reminder（基于内容） FROM 活动内容 WHERE location（基于内容） = ?", (matching_value,))
result = cursor.fetchone()[0]



# Execute the SQL query to update table1
cursor.execute("UPDATE 活动 SET reminder（基于内容） = ? WHERE rowid = ?", (value_from_table2, row_index))

# Commit the changes
conn.commit()

# Close the connection
conn.close()



