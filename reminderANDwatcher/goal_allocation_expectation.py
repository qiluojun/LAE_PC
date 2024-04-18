import re
import sqlite3


def read_goals_from_file(filepath):
    goals = []  # List to store the goals
    content_locations = {}  # Dictionary to store content_location for each level
    pattern = re.compile(r'\d+(\.\d+)+')  # Pattern to identify node levels
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if "(see:" in line:
                pattern_see=re.compile(r'\d+(\.\d+){2,}')
                before_see, _, after_see = line.partition("(see:")
                after_see = after_see[re.search(pattern_see, after_see).start():] if re.search(pattern_see, after_see) else ""
                line = before_see + after_see
                
                
                
            level_match = pattern.match(line.lstrip())
            if level_match:
                level = level_match.group()
                location = level  # Store the numeric code as location
                
                
                
                # Check for content_location in brackets
                content_location_match = re.search(r'\【\d+-.+?\】', line)
                if content_location_match:
                    content_location = content_location_match.group(0).strip('【】')
                    # Update content_locations for the current level
                    content_locations[level] = content_location
                
         
                
                '''
                # Check if line contains a goal
                if "【goal】" in line or "[goal]" in line:
                    goal_name = line.split("【goal】")[0].split()[-1] + line.split("【goal】")[-1]
                    goal_time = ""
                    if "[" in line and "]" in line:  # Check if line contains time
                        goal_time = line[line.find("[")+1:line.find("]")]
                    elif "【" in line and "】" in line: 
                        goal_time = line[line.find("【")+1:line.find("】")]
                    
                    # Find the closest content_location
                    parts = level.split('.')
                    for i in range(len(parts), 0, -1):
                        search_level = '.'.join(parts[:i])
                        if search_level in content_locations:
                            goal_content_location = content_locations[search_level]
                            break
                    else:
                        goal_content_location = ""
                    '''
                    
                    
                    
                # Check if line contains a goal
                goal_match = re.search(r'(\【goal|(\[goal))', line)
                if goal_match:
                    
                    goal_content = re.search(r'(\【goal(.+?)?\】|\[goal(.+?)?\])', line)
                    if goal_content:
                        goal_tag_full = goal_content.group(0)
                        goal_time = goal_content.group(2) if goal_content.group(2) else goal_content.group(3)
                        goal_name = line.split(goal_tag_full)[0].split()[-1] + line.split(goal_tag_full)[-1]
                    else:
                        goal_name = line
                        goal_time = ""
                    
                    # Find the closest content_location
                    parts = level.split('.')
                    for i in range(len(parts), 0, -1):
                        search_level = '.'.join(parts[:i])
                        if search_level in content_locations:
                            goal_content_location = content_locations[search_level]
                            break
                    else:
                        goal_content_location = ""
                    
                    #print('location,goal_name,goal_time,goal_content_location',location,goal_name,goal_time,goal_content_location)
                    # Add the goal to the list
                    if goal_time:
                        goals.append({"location": location, "name": goal_name.strip(), "time": goal_time.strip(), "content_location": goal_content_location})
                    else:goals.append({"location": location, "name": goal_name.strip(), "time": ' ', "content_location": goal_content_location})
                        
                    
                    
                    
                    
                    
                    
    return goals

def read_expectations_from_file(filepath):
    expectations = []  # List to store the expectations
    content_locations = {}  # Dictionary to store content_location for each level
    pattern = re.compile(r'\d+(\.\d+)+')  # Pattern to identify node levels
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if "(see:" in line:
                pattern_see=re.compile(r'\d+(\.\d+){2,}')
                before_see, _, after_see = line.partition("(see:")
                after_see = after_see[re.search(pattern_see, after_see).start():] if re.search(pattern_see, after_see) else ""
                line = before_see + after_see
                
            
            level_match = pattern.match(line.lstrip())
            if level_match:
                level = level_match.group()
                location = level  # Store the numeric code as location
              
                # Check for content_location in brackets
                content_location_match = re.search(r'\【\d+-.+?\】', line)
                if content_location_match:
                    content_location = content_location_match.group(0).strip('【】')
                    # Update content_locations for the current level
                    content_locations[level] = content_location
                
                expectation_match = re.search(r'(\【expectation|(\[expectation))', line)
                if expectation_match:
                    #print(line)
                    expectation_content = re.search(r'(\【expectation(.+?)?\】|\[expectation(.+?)?\])', line)
                    if expectation_content:
                        expectation_tag_full = expectation_content.group(0)
                        expectation_time = expectation_content.group(2) if expectation_content.group(2) else expectation_content.group(3)
                        expectation_name = line.split(expectation_tag_full)[0].split()[-1] + line.split(expectation_tag_full)[-1]
                    else:
                        expectation_name = line
                        expectation_time = ""
                    
                    # Find the closest content_location
                    parts = level.split('.')
                    for i in range(len(parts), 0, -1):
                        search_level = '.'.join(parts[:i])
                        if search_level in content_locations:
                            expectation_content_location = content_locations[search_level]
                            break
                    else:
                        expectation_content_location = ""
                    
                    #print('location,expectation_name,expectation_time,expectation_content_location',location,expectation_name,expectation_time,expectation_content_location)
                    # Add the expectation to the list
                    if expectation_time:
                        expectations.append({"location": location, "name": expectation_name.strip(), "time": expectation_time.strip(), "content_location": expectation_content_location})
                    else:expectations.append({"location": location, "name": expectation_name.strip(), "time": ' ', "content_location": expectation_content_location})
                        
    return expectations




def write_goals_to_db(goals):
    db_path = "D:\\学习and学校\\搞事情\\LAE\\TimelineAndKanban\\activity.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 确保表存在
    cursor.execute('''CREATE TABLE IF NOT EXISTS goals
                      (location TEXT, name TEXT, time TEXT, content_location TEXT)''')
    
    
    # 清空表中的旧值
    cursor.execute('DELETE FROM goals')
    
    for goal in goals:
        cursor.execute('''INSERT INTO goals (location, name, time, content_location)
                          VALUES (?, ?, ?, ?)''', (goal['location'], goal['name'], goal['time'], goal['content_location']))
    
    conn.commit()
    conn.close()


def write_expectations_to_db(expectations):
    db_path = "D:\\学习and学校\\搞事情\\LAE\\TimelineAndKanban\\activity.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 确保表存在
    cursor.execute('''CREATE TABLE IF NOT EXISTS expectations
                      (location TEXT, name TEXT, time TEXT, content_location TEXT)''')
    
    # 清空表中的旧值
    cursor.execute('DELETE FROM expectations')
    
    for expectation in expectations:
        cursor.execute('''INSERT INTO expectations (location, name, time, content_location)
                          VALUES (?, ?, ?, ?)''', (expectation['location'], expectation['name'], expectation['time'], expectation['content_location']))
    
    conn.commit()
    conn.close()



if __name__ == "__main__":
    # Example usage
    filepath = "C:\\Users\\qiluo\\Desktop\\LAE!!!.txt"  # Update this to the correct path
    goals = read_goals_from_file(filepath)
    write_goals_to_db(goals)
    expectations = read_expectations_from_file(filepath)
    write_expectations_to_db(expectations)





