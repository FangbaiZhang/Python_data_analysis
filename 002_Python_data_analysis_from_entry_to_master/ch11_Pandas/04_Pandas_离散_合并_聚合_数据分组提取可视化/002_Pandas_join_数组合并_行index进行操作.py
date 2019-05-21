# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 构造两个数组
df1 = pd.DataFrame(np.ones((2, 4)), index=['A', 'B'], columns=list('abcd'))
df2 = pd.DataFrame(np.zeros((3, 3)), index=['A', 'B', 'C'], columns=list('xyz'))
print(df1)
print(df2)
print('*' * 100)

# join合并数组
# 列会自动拼接在后面，行数多的加少的，没有的值就是NaN
# 行数少的加行数多的，多出的行直接删除了‘

print(df1.join(df2))
print('*' * 100)

print(df2.join(df1))
print('*' * 100)