# -*- coding: cp936 -*-
# 详细见P313
# 分析CSV文件，CSV文件第一行类似于EXCEL表格，第一行是表头数据，第二行开始就是对应的具体数据
# 提取表头数据，和最高气温数据用于绘制最高气温图

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 分析读取2014年7月份的天气数据
with open('sitka_weather_07-2014.csv', encoding='utf-8') as f:
    
    # 读取整个文件的内容，使用csv模块中的reader,读取结果是一个列表，每一行是一个列表
    reader = csv.reader(f)

    # 读取文件的第一行内容，next函数每次读取一行,读取指针暂停
    header_row = next(reader)
    print(header_row)
    # 读取第二行的内容，具体的天气数据
    # second_row = next(reader)
    # print(second_row)
    # print()

    # 打印文件头中每列的名称及其位置，enumerate用来给列表中每个元素添加一个索引
    # 添加索引后是由索引和元素组成一个元组，然后所有的元组组成一个新的列表
    # 提取出每个列表元组中的索引和对应的值
    for index, column_header in enumerate(header_row, start=1):
        print(index, column_header)
    print()
    
    # 上面输出显示获取文件中的最高气温，上面输出显示，第1列为日期，第2列为最高气温
    dates, highs = [], []
    # 从第2行开始遍历每一行，因为第一行前面已经采用next读取了
    # 将每一行第一个数据和第二个数据，日期和最高气温提取添加到列表
    for row in reader:
        # 提取日期
        current_date = datetime.strptime(row[0], "%Y/%m/%d") # 注意单月天气的日期之间是用的/
        dates.append(current_date)
        # 提取最高气温
        high = int(row[1])
        highs.append(high)

# 下面开始可视化最高气温
# 根据最高气温数据绘制图形,设置图形大小及分辨率
fig = plt.figure(dpi=128, figsize=(7, 5))
plt.plot(dates, highs, c='red')

# 设置图形标题，X和Y轴标题
plt.title("Daily high temperature, July 2014")
plt.xlabel("Date", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
# 将x轴的文字斜着显示
fig.autofmt_xdate()
# 设置刻度，which参数用于显示主副刻度，该处折线点太少没有主副区别
# 设置刻度在内部，颜色黑色等参数
plt.tick_params(axis='both', which='both', width=2,
        colors='black', direction='in', labelsize=8)
# 横坐标是日期，单独设置y坐标轴的取值范围
plt.ylim([0, 100])

plt.show()



