basics_state_record_seperate.py
    运行即一个独立窗口 往集合版db里记入基本状态~

db_modification.py
    db file的伴随程序 
    目前功能：
    1. 按照目前obsidian文件情况 刷新 活动内容-简 





Class_activityAndRecord.py 
    定义了活动 和 活动记录 的类 包括基本属性 和 时间戳的生成 
        两个类是组合关系~
    未来可能考虑加入其他属性生成、修改方法

from_md_to_copy_and_window_to_copy.py
    到时候整合一下 
    write_here.py
        点击确认后 自动把一段文字 复制到粘贴板上 我手动粘贴一下即可  并且还会弹出一个持续任意时长后会自动消失的信息窗口 以确认 按钮点击成功了
    circle_choose_print.py
        鼠标选中的内容 按下ctrl+c 自动print出来~

write_in_md_and_db.py
在md和db记录活动等 


new_activity_ui.py
    即 添加新活动（悬浮置顶显示） 
    还差最后一个按钮 立即开始活动 没有写功能 等主窗口搞定~

mainwindow_ui.py
    主窗口 ui
    最好把和不需要 每xx进行一次时间检查的 功能 都放这里 省得挤主进程

TimeLineWorkingOn.py
    主进程
    打算所有和时间相关的东东 都放在这里好了 乐
V2：增加后台托盘功能~