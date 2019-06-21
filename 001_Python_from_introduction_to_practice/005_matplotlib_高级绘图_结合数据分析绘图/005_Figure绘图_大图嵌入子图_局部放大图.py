# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义一个画布
fig = plt.figure(figsize=(8, 6))

# 定义一个函数
def f(x):
    return 1/(1 + x**2) + 0.1/(1 + ((3 - x)/0.1)**2)

# 定义一个绘图方法
def plot_and_format_axes(ax, x, f, fontsize):
    ax.plot(x, f(x), lw=3, color='blue')
    ax.xaxis.set_major_locator(mpl.ticker.MaxNLocator(5)) # X轴显示5个刻度
    ax.yaxis.set_major_locator(mpl.ticker.MaxNLocator(4)) # Y轴显示5个刻度
    ax.set_xlabel(r"$x$", fontsize=fontsize)
    ax.set_ylabel(r"$f(x)$", fontsize=fontsize)

# 主图,添加主图在画布的位置（占画布的比例），离左侧10%，底部15%，宽80%,高80%，背景色
ax_max = fig.add_axes([0.1, 0.15, 0.8, 0.8], facecolor="#f5f5f5")
x = np.linspace(-4, 14, 1000)
plot_and_format_axes(ax_max, x, f, 18)

# 局部图，添加局部图绘图的位置
# 局部图X轴取值范围
x0, x1 = 2.5, 3.5
ax_min = fig.add_axes([0.5, 0.5, 0.38, 0.4], facecolor=None)
x = np.linspace(x0, x1, 1000)
plot_and_format_axes(ax_min, x, f, 14)


# 展示图形
plt.show()