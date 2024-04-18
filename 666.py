# 定义一个列表，用于存储用户输入的数字记录
records = []

# 用一个循环来实现程序的交互
while True:
# 打印提示信息，让用户选择操作
    print("请选择操作：")
    print("1. 输入数字")
    print("2. 查看历史输入记录")
    print("3. 修改历史输入记录")
    print("4. 退出程序")
    choice = input()

# 根据用户的选择来执行不同的操作
    if choice == "1":
# 输入数字，将其加入到记录列表中
        num = input("请输入一个数字：")
        records.append(num)
    elif choice == "2":
# 查看历史输入记录
        print("历史输入记录：")
        for record in records:
            print(record)
    elif choice == "3":
# 修改历史输入记录
        index = int(input("请选择要修改的记录的序号："))
        if index >= 1 and index <= len(records):
            new_num = input("请输入新的数字：")
            records[index-1] = new_num
        else:
            print("序号无效，请重新选择")
    elif choice == "4":
# 退出程序
        break
    else:
# 如果用户输入了无效的选择，就提示用户重新输入
        print("无效的选择，请重新输入")

