# -*- coding: utf-8 -*-
# 绘制一系列点的散点图，设置样式

import matplotlib.pyplot as plt

# 指定x,y轴数据
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# 绘制散点图
plt.scatter(x_values, y_values, s=100)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 显示刻度，设置刻度大小和颜色
plt.tick_params(axis='both', which='both', colors='black', labelsize=14)

# 输出图片
plt.show()

