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

# 删除有Nan的行或者列,hao的默认参数是any，只要有一个就删掉
print(t3.dropna(axis=0))
print('*' * 100)

# 全部为Nan的行或者列才删除
print(t3.dropna(axis=0, how='all'))
print('*' * 100)

# 以上操对t3是没有修改的，t3还是原来的t3

# 如果需要修改t3，可以加入inplace参数，原位置修改
print(t3.dropna(axis=0, how='any', inplace=True))
print('*' * 100)
print(t3)