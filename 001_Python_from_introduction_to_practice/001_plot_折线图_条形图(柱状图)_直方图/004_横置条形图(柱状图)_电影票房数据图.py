# -*- coding: utf-8 -*-

# 导入包
import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# X轴和Y轴数据,票房单位亿
a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]
b = [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=128)

# 绘制横置条形图，x轴参数是一个可迭代对象，一般为列表
# 竖直条形图，用的是width设置宽度
plt.barh(a, b, height=0.5, color='red')

# 设置图片，X轴，Y轴标题
plt.title("2018年电影票房纪录", fontsize=24)
plt.xlabel("票房(亿元)", fontsize=14)

# 设置坐标轴刻度，刻度间隔,range不能设置步长
my_x_ticks = np.arange(0, 61, 5)
plt.xticks(my_x_ticks)

# 设置网格
plt.grid(axis='both', color='grey', linestyle='-.', alpha=0.5)

# 显示图形
plt.show()