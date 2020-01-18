# -*- coding: utf-8 -*-

# 导入包
import matplotlib.pyplot as plt

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴和Y轴数据,三天电影票房情况，票房单位万元
movie = ["流浪地球","中国机长","哪吒之魔童降世","少年的你"]
y_1 = [23585,4566,36898,2620]
y_2 = [21235,5598,39852,2835]
y_3 = [22986,6895,41250,2985]

# 设置图形的大小
plt.figure(figsize=(10, 6), dpi=128)

# 设置X轴的坐标数据,条形图宽度为0.2,先设置14号的数据，绘制15号，
# X轴坐标向右移动0.02即可，也可以多移动一点，保持一点间隙
bar_width = 0.2
x_1 = list(range(len(movie)))
x_2 = [i + 0.02 + bar_width for i in x_1]
x_3 = [i + 0.02 + bar_width for i in x_2]

# 竖直条形图，用的是width设置宽度，x轴参数是一个可迭代对象，一般为列表
# 分别绘制三天的电影票房，绘制三次即可
plt.bar(x_1, y_1, width=bar_width, label='10月1日', color='red')
plt.bar(x_2, y_2, width=bar_width, label='10月2日',color='orange')
plt.bar(x_3, y_3, width=bar_width, label='10月3日',color='green')

# 将X轴转换为对应的字符串，只对应中间的，字就在正中间
plt.xticks(x_2, movie, rotation = 0)

# 设置图片，X轴，Y轴标题
plt.title("2019国庆电影票房", fontsize=24)
plt.xlabel("单日票房(万元)", fontsize=14)
plt.ylabel("电影名称", fontsize=14)

# 设置网格,显示图例
plt.grid(axis='both', color='grey', linestyle='-.', alpha=0.5)
plt.legend(loc='upper right')

# 显示图形
plt.show()