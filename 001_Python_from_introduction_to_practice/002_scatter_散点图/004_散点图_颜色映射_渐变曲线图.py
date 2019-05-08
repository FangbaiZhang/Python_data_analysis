# -*- coding: cp936 -*-
# 绘制一系列点的散点图，自动计算数据
# 使用颜色映射绘制渐变曲线图
# 相对于003，数据加密即可变成线条

import matplotlib.pyplot as plt

# 绘制多个点

x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]

# 颜色映射，将c设置成x或者y的值，然后设置cmap映射，直接进matplotlib官网选择颜色代码的名称
# Colormap reference网址：https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.jet,
        edgecolor='none', s=50)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='both', colors='black', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1050, 0, 1100000])

plt.show()


