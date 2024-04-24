import sqlite3
from class_question_answer import Question

def get_question_from_db():
    # 连接到 SQLite 数据库
    conn = sqlite3.connect('D:\\学习and学校\\搞事情\\LAE\\GraduateProject\\data.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT variable, ques_stem, choice_num, ques_id, choice_id, continuity FROM ques_basic")

    # 获取所有行
    rows = cursor.fetchall()

    # 创建问题集合
    question_set = []
    for row in rows:
        # 创建 Question 对象并添加到集合中
        question = Question(variable=row[0], ques_stem=row[1], choice_num=row[2], ques_id=row[3], choice_id=row[4], continuity=row[5])
        # 如果 choice_id 不是 0 或空，则从 ques_choices 表中获取选项
        if question.choice_id and question.choice_id != 0:
            question.choice = get_choice_from_db(question.choice_id)
            
        question_set.append(question)

    # 关闭连接
    conn.close()
    
    return question_set

def get_choice_from_db(choice_id):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect('D:\\学习and学校\\搞事情\\LAE\\GraduateProject\\data.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT choice_name, choice_index FROM ques_choices WHERE choice_id = ?", (choice_id,))

    # 获取所有行
    rows = cursor.fetchall()

    # 创建字典存储选项名称和编号
    choice_dict = {row[1]: row[0] for row in rows}

    # 关闭连接
    conn.close()

    return choice_dict


def write_answer_in_db(question_set):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect('D:\\学习and学校\\搞事情\\LAE\\GraduateProject\\data.db')
    cursor = conn.cursor()

    for question in question_set:
        # 插入数据到 user_answer 表
        cursor.execute("""
            INSERT INTO user_answer (variable, ques_stem, answer_content, ans_time, ques_id)
            VALUES (?, ?, ?, ?, ?)
        """, (question.variable, question.ques_stem, question.answer_content, question.ans_time, question.ques_id))

    # 提交事务
    conn.commit()

    # 关闭连接
    conn.close()