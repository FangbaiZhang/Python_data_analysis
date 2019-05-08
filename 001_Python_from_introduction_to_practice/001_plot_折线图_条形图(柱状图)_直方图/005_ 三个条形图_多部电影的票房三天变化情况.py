# -*- coding: utf-8 -*-

# 导入包
import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴和Y轴数据,三天电影票房情况，票房单位万元
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_14 = [2358,399,2358,362]
b_15 = [12357,156,2045,168]
b_16 = [15746,312,4497,319]

# 设置图形的大小
plt.figure(figsize=(10, 6), dpi=128)

# 设置X轴的坐标数据,条形图宽度为0.2,先设置14号的数据，绘制15号，
# X轴坐标向右移动0.2即可，也可以多移动一点，保持一点间隙
bar_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i + 0.02 + bar_width for i in x_14]
x_16 = [i + 0.02 + bar_width for i in x_15]

# 竖直条形图，用的是width设置宽度，x轴参数是一个可迭代对象，一般为列表
# 分别绘制三天的电影票房，绘制三次即可
plt.bar(x_14, b_14, width=bar_width, label='9月14日', color='orange')
plt.bar(x_15, b_15, width=bar_width, label='9月15日',color='grey')
plt.bar(x_16, b_16, width=bar_width, label='9月16日',color='green')

# 将X轴转换为对应的字符串，只对应中间的，字就在正中间
plt.xticks(x_15, a, rotation = 0)

# 设置图片，X轴，Y轴标题
plt.title("三天单日电影票房", fontsize=24)
plt.xlabel("票房(万元)", fontsize=14)
plt.ylabel("电影名称", fontsize=14)

# 设置网格,显示图例
plt.grid(axis='both', color='grey', linestyle='-.', alpha=0.5)
plt.legend(loc='upper right')

# 显示图形
plt.show()