# -*- coding: utf-8 -*-

# 导入包
import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 5, 0.1)
y1 = np.cos(2*np.pi*x)
y2 = np.arctan(2*np.pi*x)

# 设置图形的大小,下面的设置线条的宽度和标记的大小都与图形的大小有关，设置合适才是最美观的
plt.figure(figsize=(10, 8), dpi=128)

# 图形分成2行1列，第一个图在1位置，第二个图在2位置
# 绘制第一个图
plt.subplot(2, 1, 1)
line1= plt.plot(x, y1)
plt.ylim(-2, 2)
# 添加注释,传入注释内容，注释的箭头的点坐标，注释文字的坐标位置，
# shrink设置箭头末端和文字起点的间距，箭头自己会根据箭头起点和文字起点自适应大小和倾斜角度
plt.annotate('我是注释', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='red', edgecolor='red', shrink=0.05))

# 绘制第二个图
plt.subplot(2, 1, 2)
line2= plt.plot(x, y2)
plt.ylim(-2, 2)
plt.annotate('我是注释', xy=(2, 1), xytext=(3, 0), arrowprops=dict(facecolor='black', shrink=0.05))


# 设置线条风格，点标记颜色等
plt.setp(
    line1, color='red', linewidth='1', linestyle='-.',
    marker=r'$\clubsuit$', markersize='10', markerfacecolor='blue', markeredgecolor='blue',
)

plt.setp(
    line2, color='red', linewidth='1', linestyle='--',
    marker='>', markersize='5', markerfacecolor='blue', markeredgecolor='blue',
)


plt.show()