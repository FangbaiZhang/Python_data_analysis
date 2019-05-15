# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 我们的数据缺失通常有两种情况：
# 一种就是空，None等，在pandas是NaN(和np.nan一样)
# 另一种是我们让其为0，有时候就是数字0,有时就不需要处理

# 创建一个数组，并将其中某些值赋值为NaN
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
t3.loc[['a'], ['W', 'Z']] = np.nan
print(t3)
print('*' * 100)

t4 = t3.copy()
t5 = t3.copy()
# NaN填充数据, 使用列的平均值填充
print(t4.fillna(t4.mean()))
# 原数组并没有变化,浅拷贝，指向的还是t3的地址
print(t4)
print('*' * 100)

# 只填充第一列，使用列标签即可
# 需要修改后赋值，才会改变原数组
# 虽然是浅拷贝，但是原地址指向的数字已经发生了变化
t5['W'] = t5['W'].fillna(t5['W'].mean())
print(t5)
print('*' * 100)


# 处理为0的数据：t[t==0] = np.nan
# 当然并不是每次为0的数据都需要处理
# 计算平均值等情况，nan是不参与计算的，但是0会