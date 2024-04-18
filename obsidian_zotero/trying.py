import sqlite3
import re
import datetime
import time
import os

def extract_zotero_key(line):
    # 使用正则表达式匹配并提取 Zotero Key
    match = re.search(r'zotero://select/items/1_([A-Za-z0-9]+)', line)
    if match:
        return match.group(1)  # 返回匹配的第一个括号内的内容，即 Zotero Key
    return None


def update_md_file_with_path(md_file_path, db_path):
    with open(md_file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        key = None
        for line in lines:
            extracted_key = extract_zotero_key(line)
            if extracted_key:
                key = extracted_key
                break
        
        # If a key was found, find the path using the updated find_path function
        if key:
            path = find_path(key, db_path)  # Ensure this uses the updated function that accepts Zotero Key
            has_path = False
            in_front_matter = False
            for i, line in enumerate(lines):
                if line.strip() == '---':
                    if not in_front_matter:
                        in_front_matter = True
                    else:
                        if not has_path:
                            lines.insert(i, f'paper_path: {path}\n')
                        break
                elif line.startswith('paper_path:'):
                    lines[i] = f'paper_path: {path}\n'
                    has_path = True
                    break
                    
        # Write the changes back to the file
        file.seek(0)
        file.writelines(lines)
        file.truncate()



def find_collection_path(collectionID, cursor, path=[]):
    """
    Recursively finds the collection path for a given collectionID.
    
    :param collectionID: The current collectionID for which to find the parent collection.
    :param cursor: The SQLite cursor object for database operations.
    :param path: The current path of collection names.
    :return: A list representing the collection path of the item.
    """
    if collectionID is None:
        return path
    
    cursor.execute("SELECT collectionName, parentCollectionID FROM collections WHERE collectionID=?", (collectionID,))
    result = cursor.fetchone()
    if result:
        collectionName, parentCollectionID = result
        return find_collection_path(parentCollectionID, cursor, [collectionName] + path)
    else:
        return path

def find_path(key, db_path):
    """
    Find the collection path for a given key in the Zotero database.
    
    :param key: The key of the item for which to find the collection path.
    :param db_path: Path to the Zotero SQLite database file.
    :return: A string representing the collection path of the item.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Find the itemID for the given key
    cursor.execute("SELECT itemID FROM items WHERE key=?", (key,))
    itemID_result = cursor.fetchone()
    if itemID_result:
        itemID = itemID_result[0]
        # Find the collectionID for the found itemID
        cursor.execute("SELECT collectionID FROM collectionItems WHERE itemID=?", (itemID,))
        collectionID_result = cursor.fetchone()
        if collectionID_result:
            collectionID = collectionID_result[0]
            # Find the collection path
            path_list = find_collection_path(collectionID, cursor)
            path = " / ".join(path_list)
        else:
            path = "Item not found in any collection"
    else:
        path = "Key not found"
    
    conn.close()
    return path

# Example usage
#key = '9AYJZ8ET'  # Replace 'YourKeyHere' with the actual key
#print(find_path(key))




def extract_key_and_update_path(md_file_path, db_path):
    """
    Extracts the Zotero item key from a Markdown file and updates the file with the collection path.
    
    :param md_file_path: Path to the Markdown file.
    :param db_path: Path to the Zotero SQLite database file.
    """
    # Pattern to find the Zotero key
    key_pattern = re.compile(r'\[Local library\]\(zotero://select/items/1_([A-Z0-9]+)\)')
    # Read the Markdown file
    with open(md_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Extract the key
    key = None
    for line in lines:
        match = key_pattern.search(line)
        if match:
            key = match.group(1)
            break
    
    if key is not None:
        # Find the path using the key
        path = find_path(key, db_path)  # Assume find_path is already defined and modified to accept a key
        
        # Update the Markdown file
        in_header = False
        header_found = False
        path_updated = False
        for i, line in enumerate(lines):
            if line.strip() == '---':
                if not in_header:
                    in_header = True
                elif in_header and not header_found:
                    header_found = True
                    in_header = False
                    if not path_updated:
                        # Insert paper_path before the closing ---
                        lines.insert(i, f'paper_path: {path}\n')
                        path_updated = True
            elif in_header and line.startswith('paper_path:'):
                lines[i] = f'paper_path: {path}\n'
                path_updated = True
        
        # Write the updated content back to the file
        with open(md_file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
    else:
        print("Zotero item key not found in the Markdown file.")

def update_recent_md_files_in_folder(folder_path, db_path, days=3):
    now = time.time()
    three_days_ago = now - (days * 86400)  # 86400 seconds in a day
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                ctime = os.path.getctime(file_path)
                
                if ctime > three_days_ago:
                    update_md_file_with_path(file_path, db_path)

# 调用这个函数，确保传入正确的数据库路径和 MD 文件夹路径
folder_path = r"D:\学习and学校\obsidian\qiluo\03-Projects\02-Reading\mdnotes"
db_path = r"C:\Users\qiluo\Zotero\zotero.sqlite"
update_recent_md_files_in_folder(folder_path, db_path)
