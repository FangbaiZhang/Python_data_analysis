# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 用来正常显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# rand函数生成元素在[0, 1)区间均匀分布的浮点数数组，传入参数为shape
df = pd.DataFrame(np.random.rand(5, 4), index=list('ABCDE'), columns=['系列1', '系列2', '系列3', '系列4'])
print(df)

# kind可以传入图表类型
# bar直方图，自动分组，行作为一组
# 列作为同一个系列

df.plot(kind='bar')

plt.show()
