# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 创建一个Series数组，生成1000个随机标准正态分布的浮点数，索引是时间序列
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(ts)
print('*' * 100)

# 求累加值
ts = ts.cumsum()
print(ts)
print('*' * 100)

# 我们可以使用 plt.plot(x=, y=)，把x,y的数据作为参数存进去，
# 但是ts本来就是一个数据，所以我们可以直接plot
# 上面的Series数组第一列index就是X坐标，第二列就是对应的值
ts.plot()

# 同样可以使用plt传入各种图形设置
# 默认为选取最优化的设置

plt.show()