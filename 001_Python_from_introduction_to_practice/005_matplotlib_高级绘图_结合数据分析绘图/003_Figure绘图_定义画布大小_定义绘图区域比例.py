# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成绘图数据
# -2到2的1000个等分数据
x = np.linspace(-2, 2, 1000)
y1 = np.cos(40*x)
y2 = np.exp(-x**2)

# 定义画布对象的大小和颜色
fig = plt.figure(figsize=(10, 5), facecolor="#f1f1f1")

# 在画布上添加一个子图，子图对象占画布比例，离画布左侧距离10%，底部10%，宽度80%，高度80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes((left, bottom, width, height), facecolor="#e1e1e1")

# 子图上面绘制曲线,设置线条颜色和线型
ax.plot(x, y1 * y2, 'r-')
ax.plot(x, y2, 'b--')
ax.plot(x, -y2, 'b--')
ax.scatter(0, 0, s=5000, color='green')
ax.scatter(0, 0, s=1000, color='black')
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 1.5)

plt.show()