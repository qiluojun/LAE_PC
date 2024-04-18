import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



# 指定字体为微软雅黑，用于显示中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或其他你喜欢的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号无法显示的问题

# 接下来是你的绘图代码





# 示例项目时间线数据
dates = [
    (datetime(2024, 2, 7), datetime(2024, 2, 11), "完成文献综述"),
    (datetime(2024, 3, 1), datetime(2024, 4, 1), "实验设计与实施")
]

# 绘制时间线
fig, ax = plt.subplots()
ax.set_title('毕设进度时间线')

# 为每个任务添加时间线
for start, end, label in dates:
    ax.plot([start, end], [label, label], marker = '|', markersize = 10, linestyle = '-')

# 设置日期格式
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
