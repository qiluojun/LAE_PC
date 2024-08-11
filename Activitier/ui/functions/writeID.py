import os
import datetime

def insert_id(file_path):
    # 获取文件创建时间
    timestamp = os.path.getctime(file_path)
    # 将时间戳转换为datetime对象
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    # 格式化时间
    id = dt_object.strftime("%Y%m%d%H%M%S")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lae_index = None
    for i, line in enumerate(lines):
        if line.strip() == "# LAE 用":
            lae_index = i
            break

    if lae_index is None:
        raise ValueError(f"'# LAE 用' not found in {file_path}")

    # Check if the next line after "# LAE 用" starts with "【id】"
    if lae_index + 1 < len(lines) and lines[lae_index + 1].strip().startswith("【id】"):
        #print("pass")
        return  # Skip this file if it already has an id

    lines.insert(lae_index + 1, f"【id】{id}\n")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# 使用示例
#insert_id(r"D:\学习and学校\obsidian\qiluo\1-学业与未来\14-ada\141+222-sds.md")

def insert_id_to_files_in_folders(folders):
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    try:
                        #print(f"Processing file: {full_path}")
                        insert_id(full_path)
                    except Exception as e:
                        print(f"Error processing file {full_path}: {e}")
# 使用示例
folders = [r"D:\学习and学校\obsidian\qiluo\1-学业与未来", r"D:\学习and学校\obsidian\qiluo\2-自由学习与探索",r"D:\学习and学校\obsidian\qiluo\3-LAE其他"]
insert_id_to_files_in_folders(folders)
