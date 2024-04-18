import sqlite3
from datetime import datetime, timedelta
import re
from fractions import Fraction
# 连接数据库 (请替换为您的实际数据库文件路径)
db_path = 'D:\\学习and学校\搞事情\\LAE\\TimelineAndKanban\\activity.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 定义处理数据的函数
def update_real_goal():
    start_date = datetime.strptime("2024-03-22", "%Y-%m-%d")
    
    # 从 real_goal 表中获取数据
    cursor.execute("SELECT name, location, DDL, len_total, lenth_day_min, day_duration_max FROM real_goal")
    goals = cursor.fetchall()

    for goal in goals:
        name, location, ddl_str, current_len_total, current_lenth_day_min, current_day_duration_max = goal
        ddl = datetime.strptime(str(ddl_str), "%m.%d.%Y")
        
        # 筛选匹配的 activity_record 记录
        location_prefix = location.split('-')[0]  # 提取location的数字代码
        query = """
        SELECT record_timestamp, actual_duration FROM activity_record 
        WHERE content_location LIKE '{}%-%'
        AND record_timestamp >= '{}' AND record_timestamp <= '{}'
        """.format(location_prefix, start_date.strftime("%Y%m%d"), (ddl + timedelta(days=1)).strftime("%Y%m%d"))
        cursor.execute(query)
        activities = cursor.fetchall()
        print(ddl.strftime("%Y%m%d"))
        
        
        
        '''# 筛选匹配的 activity_record 记录
        query = """
        SELECT record_timestamp, actual_duration FROM activity_record 
        WHERE content_location LIKE '{}%'
        AND record_timestamp >= '{}' AND record_timestamp <= '{}'
        """.format(location.split('-')[0], start_date.strftime("%Y%m%d"), ddl.strftime("%Y%m%d"))
        cursor.execute(query)
        activities = cursor.fetchall()'''

        # 计算总时长、日均时长和活动频率
        total_duration_seconds = 0
        activity_days = set()
        for record_timestamp, actual_duration in activities:
            # 记录活动的日期
            activity_date = datetime.strptime(record_timestamp[:8], "%Y%m%d").date()
            activity_days.add(activity_date)
            
            # 累加时长
            hours, minutes, seconds = map(int, actual_duration.split(':'))
            total_duration_seconds += timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

        total_days = (ddl - start_date).days + 1
        len_total = round(total_duration_seconds // 60)  # 转换为小时
        lenth_day_min = len_total / total_days  # 日均时长
        if len(activity_days) > 0:
            day_duration_max = Fraction(len(activity_days), total_days)  # 活动频率
            
        else:
            day_duration_max = 0  # 如果没有活动天数，频率设置为0
        # 更新 real_goal 表
        updates = []
        for current_value, new_value, column_name in [
            (current_len_total, int(len_total), "len_total"),
            (current_lenth_day_min, int(lenth_day_min), "lenth_day_min"),
            (current_day_duration_max, day_duration_max, "day_duration_max")
        ]:
            current_value_str = str(current_value)
            
            if current_value is not None and new_value > 0:
                # 检查当前值是否已经包含【】
                if "【" in current_value_str and "】" in current_value_str:
                    # 使用正则表达式找到【】内的内容并替换
                    updated_value = re.sub(r"【.*?】", f"【{new_value}】", current_value)
                else:
                    # 按原来的方式附加新的值
                    updated_value = f"{current_value}【{new_value}】"
                updates.append(f"{column_name} = '{updated_value}'")

        if updates:
            update_query = f"UPDATE real_goal SET {', '.join(updates)} WHERE name = '{name}'"
            cursor.execute(update_query)
        
        # 打印匹配的行以检查匹配是否正确
        for activity in activities:
            print("name,activity",name,activity)
        

    conn.commit()

# 注意：在实际执行前，请确保已正确设置数据库路径，并检查SQL语句与您的数据库结构匹配
update_real_goal()

# 关闭数据库连接
conn.close()
