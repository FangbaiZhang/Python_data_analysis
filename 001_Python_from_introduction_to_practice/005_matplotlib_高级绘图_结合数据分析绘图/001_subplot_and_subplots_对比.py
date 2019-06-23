# -*- coding: utf-8 -*-

# subplot与subplots对比：
# subplot多图模式，使用三个坐标值定义一个子图对象
# subplots更高级的绘图模式，返回数组对象，直接使用两个坐标定义子图对象

# subplot绘图参考：003_折线图_一张图中绘制三个独立的图.py
# subplots绘图参考：001_subplots_绘制子图_ax对象绘制多个图



# subplots绘图展示,绘制3行3列的多个子图：

import matplotlib.pyplot as plt

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

nrows, ncols = 3, 3
fig, ax = plt.subplots(nrows, ncols)

for m in range(nrows):
    for n in range(ncols):
        # 隐藏XY轴刻度
        ax[m, n].set_xticks([])
        ax[m, n].set_yticks([])
        # 添加文字
        ax[m, n].text(0.25, 0.5, "axes[%d, %d]" % (m, n), fontsize=15, color='red')

ax[1, 1].text(0.5, 0.2, 'subplots演示', fontsize=15, color='blue', horizontalalignment='center')

# plt直接设置，是默认在最后一个子绘图对象上面设置
plt.text(0, 0, 'figure画布注释', ha='left', rotation=-15, wrap=True)

plt.show()


