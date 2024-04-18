'''
在原来timelineV3.3.2 的基础上 选中 点击对应按钮 显示（测试时使用 print）
'''



# 这里！！！！！！！！！！！！！——基于 timelineV3.3.2
cursor = main_window.ui.plan_text.textCursor()
selected_text = cursor.selectedText()
selected_text = selected_text.replace("\u2029", "\n")
with open(r"D:\学习and学校\obsidian\qiluo\00-BASE\for_text.md", "a", encoding="utf-8") as file:
    file.write(selected_text)

# Rest of the code...
