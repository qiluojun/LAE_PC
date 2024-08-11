from datetime import datetime


# 假设常模规则非常简单：只有时间段和预期活动类型
model = [
    {
        'time': [('00:00', '08:20'), ('12:50', '13:30'), ('23:00', '23:59')],
        'target_activity': ['any'],
        'rule_id': '01',
        'description': '不允许使用电脑的时间'
    },
    # 这里可以添加更多的规则
    
    {
        'time': [('08:20', '11:00'), ('13:30', '16:30'), ('18:30', '21:59')],
        'target_activity': ['知乎','bilibili'],
        'rule_id': '02',
        'description': '知乎、B站时段中异常使用'
    },
    # 这里可以添加更多的规则
    
]



def check_status(status, model=model):
    
    current_time = status['current_time']
    activity = status['activity']
    rules_violated = []  # 初始化违反规则的列表

    for rule in model:
        rule_time_intervals = rule['time']
        target_activity = rule['target_activity']

        # 检查当前时间是否在规则的时间段内
        in_time_interval = False
        for interval in rule_time_intervals:
            start_time, end_time = interval
            if start_time <= current_time <= end_time:
                in_time_interval = True
                break

        # 如果当前时间在规则的时间段内，则检查活动是否符合规则要求
        if in_time_interval:
            # 修改此处逻辑，使用任意(target)作为子字符串检查是否存在于activity中
            if any(target.lower() in activity.lower() for target in target_activity):
                rules_violated.append(rule['rule_id'])
            
            #if activity in target_activity:
                #rules_violated.append(rule['rule_id'])
    
    return rules_violated
