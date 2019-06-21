# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制画布和子图对象
fig, ax1 = plt.subplots(figsize=(8, 4))

# 生成数据，半径，面积，体积
r = np.linspace(0, 5, 100)
a = 4 * np.pi * r ** 2
v = (4 * np.pi / 3) * r **3

# 绘制左Y轴图
ax1.plot(r, a, lw=2, ls='--', color='blue')
# 设置标题，XY轴标题
ax1.set_title("Surface Area and Volume of A Sphere", fontsize=16)
ax1.set_xlabel("Radius (m)")
ax1.set_ylabel(r"Surface Area ($m^2$)", fontsize=16, color='blue')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 350)
# 设置Y轴刻度文字为蓝色
for label in ax1.get_yticklabels():
    label.set_color("blue")

# 绘制右Y轴图,共用ax1的X轴
ax2 = ax1.twinx()
# 绘制ax2图
ax2.plot(r, v, lw=2, ls='-.', color='red')
ax2.set_ylabel(r"Volume ($m^3$)", fontsize=16, color='red')
ax2.set_ylim(0, 600)
# 设置Y轴刻度文字为红色
for label in ax2.get_yticklabels():
    label.set_color("red")


# 展示图形
plt.show()
