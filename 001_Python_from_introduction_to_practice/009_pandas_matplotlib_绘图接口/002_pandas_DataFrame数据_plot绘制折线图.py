# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 创建一个Series数组，生成1000个随机标准正态分布的浮点数，索引是时间序列
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

# 创建一个DataFrame数据结构,生成1000行4列的标准正态分布的浮点数，索引是时间序列
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()

# index自动作为X坐标，列作为Y轴，有几列就是几条曲线，columns作为图例
df.plot()

plt.show()