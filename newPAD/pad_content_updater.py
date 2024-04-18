def extract_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        pattern = r'(\d+【.*?】)'
        result = re.findall(pattern, text)
        return result

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def run_program():
    address_file = 'D:\\学习and学校\\obsidian\\qiluo\\00-MOC\\sidelines_address.md'
    resemble_file = 'D:\\学习and学校\\obsidian\\qiluo\\00-MOC\\resemble.md'
    resemble_content = ''
    with open(address_file, 'r', encoding='utf-8') as f:
        file_list = f.readlines()
        i=1
        for file in file_list:
            file = file.strip()
            content = extract_text(file)
            if content:
                resemble_content += '{}{}  {}{}  {}{}\n'.format(i, content[0], i, content[1], i, content[2])
            i=i+1
    write_to_file(resemble_file, resemble_content)

run_program()
