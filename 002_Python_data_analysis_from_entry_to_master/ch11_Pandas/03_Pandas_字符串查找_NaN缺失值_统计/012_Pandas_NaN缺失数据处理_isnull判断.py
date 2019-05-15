# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 我们的数据缺失通常有两种情况：
# 一种就是空，None等，在pandas是NaN(和np.nan一样)
# 另一种是我们让其为0，有时候就是数字0,有时就不需要处理

# 创建一个数组，并将其中某些值赋值为NaN
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
t3.loc[['a'], ['W', 'Z']] = np.nan
t4 = t3.copy()
print(t4)
print('*' * 100)

# 判断是否有NaN值，使用isnull，notnull
print(pd.isnull(t4))
print('*' * 100)

# 判断某一列
print(pd.notna(t4['W']))