# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# 显示中文和显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义画布和绘图对象
fig, ax = plt.subplots(1, 3, figsize=(12, 3))

# 1行3列三个图，可以省略行0，直接写列ax[0, 0]等同于a[0]
ax[0].hist(np.random.rand(10000)) #rand函数生成元素在[0, 1)区间均匀分布的浮点数
ax[0].set_title('rand随机浮点数')

ax[1].hist(np.random.randn(10000)) #randn函数生成标准分布的浮点数，标准差为1
ax[1].set_title('randn标准分布浮点数')

ax[2].hist(np.random.randint(low=0, high=10, size=10000)) #randint函数生成随机整数，指定上限下限个数
ax[2].set_title('randint随机整数')


plt.show()

