import datetime

class Question:
    def __init__(self, variable=None, ques_stem=None, choice_num=0,ques_id=None,choice=None,answer_content=None,ans_time=None,continuity=None,choice_id=None):
        self.variable = variable
        self.ques_stem = ques_stem
        self.choice_num = choice_num
        self.ques_id = ques_id
        self.choice_id=choice_id
        self.choice=choice
        self.answer_content= answer_content
        self.ans_time =ans_time
        self.continuity=continuity
    
    def generate_time(self):
        self.ans_time=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
