

import re

with open(r'D:\学习and学校\obsidian\qiluo\03-Projects\01-自由探索\02-搞事情\LAE\test.md','r',encoding='utf-8') as file:
    data = file.read()
    pattern = r'【(.*?)】'
    result = re.findall(pattern, data)
    print(result)