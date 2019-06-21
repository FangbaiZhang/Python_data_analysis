# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成数据
# 生成30个-5到2等分元素
x = np.linspace(-5, 2, 30)
y1 = x**3 + 5*x**2 + 10
# y2是y1的导数
y2 = 3*x**2 + 10*x
# y3是y2的导数
y3 = 6*x + 10

# 对象绘图,返回一个画布，一个绘图对象，figsize是指的每个子图的大小
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# 上面只绘制了一个子图，子图上绘制出三条曲线
ax.plot(x, y1, lw=2, color='blue', label=r"y(x)")
ax.plot(x, y2, lw=2, color='red', label=r"y'(x)")
ax.plot(x, y3, lw=2, color='green', label=r"y''(x)")


# 绘制y=0的辅助线，不管x是多少，对应y的取值都是0
ax.plot(x, np.zeros_like(x), lw=1, color='black')
# 绘制两个点
x1 = -3.33
ax.scatter([x1], [x1**3 + 5*x1**2 + 10], s=100, color='blue')
ax.scatter([0], [10], s=100, color='blue')
# 以上面两个点绘制两条垂线
ax.plot([0, 0], [0, 10], lw=1, ls='--', color='grey')
ax.plot([-3.33, -3.33], [0, x1**3 + 5*x1**2 + 10], lw=1, ls='--', color='grey')


# 修改美化图形
# 注意：subplots对象设置时候前面加了set_，之前绘图直接是ylim，xlabel等等
# 设置坐标轴范围
ax.set_ylim(-22, 45)
ax.set_xlim(-5, 2)
# 设置刻度，直接传入列表，列表中是每个刻度的具体值
ax.set_xticks([-4, -2, 0, 2])
ax.set_yticks([-10, 0, 10, 20, 30])

ax.set_xlabel("$x$", fontsize=28)
ax.set_ylabel("$y$", fontsize=28)

# loc是注释的位置，ncol是注释一行显示的个数
ax.legend(loc='upper center', ncol=1, fontsize=18, frameon=False)


# 展示所有图形
plt.show()
# 保存图形
fig.savefig("002_subplots_绘制子图_绘制辅助线.pdf")