import datetime

class Activity:
    def __init__(self, name, target_completion_date=None, content_location=None, type_location=None, 
                 activity_status=None, times_performed=0,time_accumulated=None, target_duration=None, progress_description=None, 
                 handle=None,timestamp=None):
        self.name = name
        self.target_completion_date = target_completion_date
        self.content_location = content_location
        self.type_location = type_location
        self.activity_status = activity_status if activity_status else {"status": "待开始", "times_performed": times_performed}
        self.time_accumulated = time_accumulated
        self.target_duration = target_duration
        self.progress_description = progress_description
        self.handle = handle
        self.timestamp = timestamp  #等到点击确定的时候 再调用函数去生成

    def generate_timestamp(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

class ActivityRecord:
    def __init__(self, activity, start_time=None, end_time=None, actual_duration=None, 
                 actual_content=None, evaluation=None):
        self.name = activity.name
        self.timestamp = activity.timestamp
        self.time_period = None
        self.record_timestamp= None
        self.content_location = activity.content_location
        self.type_location = activity.type_location
        # 注意 这个是 例如 进行中 第五次记录 注意计数是否有误
        self.activity_status = {"status": "进行中", "times_performed": activity.activity_status["times_performed"] + 1}
        self.target_completion_date = activity.target_completion_date
        self.target_duration = activity.target_duration
        self.actual_duration = {"start_time": start_time, "end_time": end_time, "duration": actual_duration}
        self.actual_content = actual_content
        self.evaluation = evaluation

    def generate_timestamp(self):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

