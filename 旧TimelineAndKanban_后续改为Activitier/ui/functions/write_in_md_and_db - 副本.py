# 1. 在哪里写 
    # 要么在md 要么在db
    # md 搞到位置   & db 搞到位置（db简单 直接插入新内容即可 ）
# 2. 写啥
    # 新活动  on md & on db
    # 活动记录  on md   & on db

import sqlite3
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from  functions.Class_activityAndRecord import  Activity, ActivityRecord




'''activity = Activity(name="跑步", target_completion_date="2022-12-31", content_location="141+222-sds", 
                    type_location="户外", activity_status={"status": "进行中", "times_performed": 1}, 
                    target_duration=30, progress_description="已完成一半", 
                    handle="这是一段描述\n有多行的\n抓手") 

activity_record = ActivityRecord(activity, start_time="20221105100000", end_time="20221105103000", 
                                 actual_duration=30, actual_content="跑了5公里", evaluation="感觉很好")
'''


def find_path(activity): # 活动 和 活动记录 均可用此 找到对应md~
    # 连接到SQLite数据库
    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT path FROM 活动内容_简 WHERE name=?", (activity.content_location,))

    # 获取查询结果
    result = cursor.fetchone()

    # 关闭数据库连接
    conn.close()
    #print('in find', activity.content_location)
    # 如果查询结果为空，返回None
    if result is None:
        return None
    
    # 否则，返回查询到的路径
    return result[0]
    

def write_activity_in_md(activity):  #在对应path 写入对应活动
    # 读取文件内容
    path=find_path(activity)
    print('in write', path)
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 找到插入位置
    start_index = lines.index("### 下属活动一览\n") + 1
    end_index = lines.index("### 抓手 👈\n")

    # 生成要插入的文本
    text = []
    text.append(f"#### {activity.name} {activity.timestamp} {activity.target_completion_date}\n")
    text.append(f"{activity.activity_status['status']} 已进行：{activity.activity_status['times_performed']}次 ；累计用时{activity.time_accumulated}\n")
    text.append(f"{activity.type_location}\n")
    if activity.target_duration is not None:
        text.append(f"{activity.target_duration}\n")
    if activity.progress_description is not None:
        text.append(f"{activity.progress_description}\n")
    if activity.handle is not None:
        text.append("【抓手】\n")
        text.append(f"{activity.handle}\n")
        text.append("【抓手】\n")

    # 插入文本
    lines = lines[:end_index] + text + lines[end_index:]

    # 写回文件
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def update_activity_in_md(activity):
    # 读取文件内容
    path = find_path(activity)
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()



    # 找到活动开始和结束的位置
    start_index = next((i for i, line in enumerate(lines) if activity.timestamp in line), None)
    if start_index is None:
        print(f"活动 {activity.name} 未找到")
        return
    end_index = next((i for i, line in enumerate(lines[start_index:], start=start_index) if line.startswith("##### 活动实际内容记录")), None)
    if end_index is None:
        end_index = lines.index("### 抓手 👈\n", start_index)


    # 生成新的活动信息
    text = []
    text.append(f"#### {activity.name} {activity.timestamp} {activity.target_completion_date}\n")
    text.append(f"{activity.activity_status['status']} 已进行：{activity.activity_status['times_performed']}次 ；累计用时{activity.time_accumulated}\n")
    text.append(f"{activity.type_location}\n")
    if activity.target_duration is not None:
        text.append(f"{activity.target_duration}\n")
    if activity.progress_description is not None:
        text.append(f"{activity.progress_description}\n")
    if activity.handle is not None:
        text.append("【抓手】\n")
        text.append(f"{activity.handle}\n")
        text.append("【抓手】\n")

    # 替换旧的活动信息
    lines = lines[:start_index] + text + lines[end_index:]

    # 写回文件
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def write_activity_in_db(activity):
    # 连接到SQLite数据库
    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()

    # 准备要插入的数据
    data = (activity.name, activity.target_completion_date, activity.content_location, activity.type_location, 
            activity.activity_status['status'],activity.activity_status['times_performed'],activity.time_accumulated, 
            activity.target_duration, activity.progress_description,activity.timestamp)

    # 执行插入操作
    cursor.execute("INSERT INTO activity (name, target_completion_date, content_location, type_location, activity_status, times_performed,time_accumulated,target_duration, progress_description,timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?)", data)

    # 提交事务
    conn.commit()

    # 关闭数据库连接
    conn.close()
    
def update_activity_in_db(activity):
    # 连接到SQLite数据库
    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()
    print("activity.activity_status['status']")
    print(activity.activity_status['status'])
    # 准备要更新的数据
    data = (activity.target_completion_date, activity.content_location, activity.type_location, 
            activity.activity_status['status'],activity.activity_status['times_performed'],activity.time_accumulated, 
            activity.target_duration, activity.progress_description,activity.timestamp, activity.timestamp)

    # 执行更新操作
    cursor.execute("UPDATE activity SET target_completion_date = ?, content_location = ?, type_location = ?, activity_status = ?, times_performed = ?, time_accumulated = ?, target_duration = ?, progress_description = ?, timestamp = ? WHERE timestamp = ?", data)

    # 提交事务
    conn.commit()

    # 关闭数据库连接
    conn.close()


def write_activity_record_in_md(activity_record):
    # 生成要写入的文本
    path=find_path(activity_record)
    text = []
    text.append(f"第{activity_record.activity_status['times_performed']}次记录\n")
    text.append(f"{activity_record.record_timestamp[:8]}-{activity_record.actual_duration['start_time'][8:]}-{activity_record.actual_duration['end_time'][8:]}-{activity_record.actual_duration['duration']}\n")
    if activity_record.evaluation is not None:
        text.append(f"{activity_record.evaluation}\n")
    if activity_record.actual_content is not None:
        text.append(f"{activity_record.actual_content}\n")

    # 读取文件内容
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 找到插入位置
    start_index = next((i for i, line in enumerate(lines) if activity_record.timestamp in line), None)
    end_index = next((i for i, line in enumerate(lines[start_index:], start=start_index) if line.startswith("#### ")), None)
    if end_index is None:
        end_index = lines.index("### 抓手 👈\n", start_index)

    # 找到活动记录开始的位置
    record_start_index = next((i for i, line in enumerate(lines[start_index:end_index], start=start_index) if line.startswith("##### 活动实际内容记录")), None)
    if record_start_index is None:
        print("not found")
        lines.insert(end_index, "##### 活动实际内容记录\n")
        record_start_index = end_index
        end_index += 1





    # 插入文本
    lines = lines[:record_start_index+1] + text + ["\n"] + lines[end_index:]
    print(lines[record_start_index:end_index])
    # 写回文件
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def write_activity_record_in_db(activity_record):
    # 连接到SQLite数据库
    conn = sqlite3.connect(r'D:\学习and学校\搞事情\LAE\TimelineAndKanban\activity.db')
    cursor = conn.cursor()
# 准备要插入的数据
    data = (activity_record.name, activity_record.target_completion_date, 
        f"{activity_record.activity_status['status']} 第{activity_record.activity_status['times_performed']}次", 
        activity_record.target_duration, activity_record.content_location, 
        activity_record.type_location, activity_record.evaluation, activity_record.timestamp,activity_record.time_period,activity_record.record_timestamp,
        activity_record.actual_duration['start_time'], activity_record.actual_duration['end_time'],activity_record.actual_duration['duration'])
    # 执行插入操作
    cursor.execute("INSERT INTO activity_record (name,target_completion_date,activity_status,target_duration,content_location,type_location,evaluation,timestamp,time_period,record_timestamp,start_time,end_time,actual_duration) VALUES (?, ?, ?, ?, ?,  ?, ?,?,?,?,?,?,?)", data)

    # 提交事务
    conn.commit()

    # 关闭数据库连接
    conn.close()
    

    
    
