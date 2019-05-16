# -*- coding: cp936 -*-
# 绘制一系列点的散点图，自动计算数据，并设置点的颜色和边缘色
# 详细见P292

import matplotlib.pyplot as plt

# 自动生成数据
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 画图，设置点的大小，颜色和边缘色
# 使用RGB颜色，先绘图，然后右键图片显示着色板Show color picker
# 选择想要的颜色，有对应的RGB编号，注意编号前面的#要加上
plt.scatter(x_values, y_values, c='#B3A9FF', edgecolor='gold', s=30)
# 使用RGB设置图标颜色,给定颜色c三个0-1的值，分别表示红绿蓝，值为1,0,0就是红色
# plt.scatter(x_values, y_values, c=(1, 0, 0), edgecolor='red', s=30)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='both', colors='blue', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 50, 0, 2500])

plt.show()

