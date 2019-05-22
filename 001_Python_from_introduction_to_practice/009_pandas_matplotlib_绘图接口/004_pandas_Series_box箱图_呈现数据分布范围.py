# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 用来正常显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# rand函数生成元素在[0, 1)区间均匀分布的浮点数数组，传入参数为shape
df = pd.Series(np.random.rand(10), name='A')
print(df)

# 绘制箱图
df.plot.box()

plt.show()

# 箱线图的绘制方法是：先找出一组数据的最大值、最小值、中位数和两个四分位数；
# 然后， 连接两个四分位数画出箱子；再将最大值和最小值与箱子相连接，中位数在箱子中间。

# 中位数（又称中值，英语：Median），统计学中的专有名词，
# 代表一个样本、种群或概率分布中的一个数值，其可将数值集合划分为相等的上下两部分。
# 对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。
# 如果观察值有偶数个，通常取最中间的两个数值的平均数作为中位数

# 四分位数（Quartile）应用于统计学中的箱线图绘制，是统计学中分位数的一种，
# 即把所有数值由小到大排列并分成四等份，处于三个分割点位置的数值就是四分位数