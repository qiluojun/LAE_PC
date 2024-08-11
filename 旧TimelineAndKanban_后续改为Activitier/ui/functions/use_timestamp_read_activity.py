from PySide6.QtSql import *
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QThread,Signal,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

import sqlite3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pynput import keyboard
import pyperclip




from functions.Class_activityAndRecord import Activity, ActivityRecord
from functions.circle_choose import MyListener
from functions.write_in_md_and_db import write_activity_in_db,write_activity_in_md,find_path






# 需要接受外界（主窗口）传入的参数： current_activity_timestamp
# 获取对应活动的数据 从db和md中搞到手~
def get_activity(current_activity_timestamp):
    # 连接到SQLite数据库
    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT * FROM activity WHERE timestamp=?", (current_activity_timestamp,))

    # 获取查询结果
    result = cursor.fetchone()

    # 关闭数据库连接
    conn.close()

    # 如果查询结果为空，返回None
    if result is None:
        return None

    # 否则，创建一个新的Activity对象并返回
    current_activity = Activity(
        name=result[0],
        target_completion_date=result[1],
        content_location=result[2],
        type_location=result[3],
        activity_status={'status': result[4], 'times_performed': result[5]},
        time_accumulated=result[6],
        target_duration=result[7],
        progress_description=result[8],
        timestamp=result[9]
    )


    # 找到对应的md文件
    path = find_path(current_activity)

    # 读取文件内容
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 找到活动开始的位置
    activity_start_index = next((i for i, line in enumerate(lines) if current_activity_timestamp in line), None)

    # 如果没有找到活动，返回None
    if activity_start_index is None:
        print("No activity found with the given timestamp.")
        return None

    # 找到"【抓手】\n"的位置
    start_index = next((i for i, line in enumerate(lines[activity_start_index:]) if line.strip() == "【抓手】"), None)

    # 如果没有找到"【抓手】\n"，那么抓手就不存在
    if start_index is None:
        #print("No 【抓手】 found in the activity.")
        current_activity.handle = None
    else:
        # 找到下一个"【抓手】\n"
        end_index = next((i for i, line in enumerate(lines[start_index+activity_start_index+1:]) if line.strip() == "【抓手】"), None)

        # 如果没有找到下一个"【抓手】\n"，那么抓手就是最后一部分
        if end_index is None:
            #print("No end 【抓手】 found in the activity.")
            current_activity.handle = None
        else:
            end_index += start_index + activity_start_index + 1  # Add start_index and activity_start_index to get the correct index in the original list

            # 读取抓手的值
            current_activity.handle = ''.join(lines[start_index+activity_start_index+1:end_index]).strip()

    return current_activity




 
if __name__ == "__main__":
    current_activity_timestamp = '20231109090927'
    current_activity = get_activity (current_activity_timestamp)
    if current_activity is not None:
        print(current_activity.name)
        print(current_activity.handle)
    else:
        print("No activity found with the given timestamp.")

