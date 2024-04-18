'''
船新版本！
要求 把所有功能集合到这个程序上
包括：
1. 显示 活动 活动内容 活动属性三个表的内容 
2. 可以修改：包括修改格子内容、删行、增行 + read files！！！
3. update_check：  
    0. 检查修改类型
    1. 活动：新增/改动location时 自动填充活动内容、活动属性两表中对应内容
    2. 活动内容、属性 对应格子（不包括location）改动时 自动改动活动对应内容
    3. 活动内容/活动属性：删行时 自动提醒是否有对应相关活动 有时 自动改成 “已删除”
    4. 活动内容/活动属性 改动location时 自动提醒是否有对应相关活动 并且自动改成新的location

'''


# import ……
# activity - 副本.db


'''1 窗口控件！'''





'''2 注： 2 和 3 是连在一起的'''
# 这一部分 比较难 建议先搞其他部分！
read_all_files_button → 
    读取本地文件和文件夹 生成临时表 
    比较对比 临时表和原表不一致的地方
    如有 弹出子窗口 并进行判断：
        1. 缺少的 视为 删除  （并自动引发3.3）
        2. 增加的 视为 新增
        3. 改动的 视为改动 （并自动引发3.4）
    我的预想 大概是 左右两边：
        左边呈现 临时表里多出来的 
        右边呈现 原表里在临时表里找不到的
        最好也是用table view 等 可以单击选中 
        然后选中之后 点击 上述 1 2 3 按钮中某一个 进行处理 没点过的忽略




'''3'''
来自 2 的参数：
# 对应cell： row_index    column_index 选中的原值
# 改动的表类型：table_name=1 活动  2 内容 3 属性 
table_name = 0
row_index,column_index=0


'''3.1  活动：新增/改动location时 自动填充活动内容、活动属性两表中对应内容'''
# 点击了 修改某格子功能 →
#if table_name = 1
    # check if column_name = location
    # get column_name
autoFill_activity_table_on_location:
输入：活动表 要改的 change_column_index 
输入 母表名称  以及要提取数据的get_value_column
location 所在的 location_index  
根据 location_index → matching_value

'''3.2 活动内容、属性 对应格子（不包括location）改动时 自动改动活动对应内容'''
autoUpdate_activity_table_on_MotherTable
# 点击了 修改某格子功能 →
#if table_name = 2/3
根据 table_name = 2/3 得到要改的表名 
得到被修改的母表的cell 所在的  location 和 column_index
根据 column_index 得出 列名 
if  列名 ≠ location~
得到母表中被改的值： value_for_update
得到母表中修改列的列名 column_to_update
在 活动 表中 根据location 找到 要修改的 row_to_update
把 value_to_update 放进  活动 表的  row_to_update + column_to_update 处


'''3.3 活动内容/活动属性：删行时 自动提醒是否有对应相关活动 有时 自动改成 “已删除” '''
update_when_deleted
# 点击了删除某行 →
if table_name = 2/3 
根据 row_index 找到所删行的 location  
寻找 活动表 中  location 有无 对应行  
    如果有：  得到 delete_line_in_child_index
    message box：自动提醒是否有对应相关活动
    把 delete_line_in_child_index行所在的 相应列（给列名 不要用列index） 改为“deleted”

''' 3.4  活动内容/活动属性 改动location时 自动提醒是否有对应相关活动 并且自动改成新的location'''
    ''' 我意识到 这一条貌似不适用于活动内容 因为 location一旦变了 path也会跟着变 
    所以建议不要在db里或程序里改！'''
change_motherTable_location
# 点击了 修改某格子功能 →
if table_name = 2/3 
根据 table_name = 2/3 得到要改的表名 
得到被修改的母表的cell 所在的  new_location old_value 和 column_index
根据 column_index 得出 列名 
列名 = location~ 
message box：自动提醒是否有对应相关活动
在 活动 表中 根据 old_valule 找到 要修改的 row_to_update
把 new_location 放进  活动 表的  row_to_update + location~ 处
