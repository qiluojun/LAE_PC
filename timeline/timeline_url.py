from urllib.parse import unquote

def get_address(url):
    decoded_url = unquote(url)
    # Replace "obsidian://" with "D:\学习and学校\obsidian\qiluo\"
    decoded_url = decoded_url.replace("obsidian://open?vault=qiluo&file=", "D:\\学习and学校\\obsidian\\qiluo\\").replace("/", "\\")
    # Add ".md" to the end of the string
    decoded_url += ".md"
    return decoded_url




