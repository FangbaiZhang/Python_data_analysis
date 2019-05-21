# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 构造两个数组
df1 = pd.DataFrame(np.ones((2, 4)), index=['A', 'B'], columns=list('abcd'))
df2 = pd.DataFrame(np.arange(9).reshape(3, 3), index=['A', 'B', 'C'], columns=list('fax'))
print(df1)
print(df2)
print('*' * 100)

# 合并
# 对a列进行操作，df1里面a列的A和B行都有1
# df1的A和B行分别和df2的A行进行了合并操作
# 内连接hao = 'inner'，取的交集
print(df1.merge(df2, on='a', how='inner'))
print('*' * 100)

# 对df1进行修改，此时只有df1的B行和df2的A行进行合并
df1.loc['A', 'a']  = 100
print(df1)
print('*' * 100)
print(df1.merge(df2, on='a', how='inner'))
print('*' * 100)

# 上面默认的是内连接hao = 'inner'，取的交集,outer取的并集
# 外连接，相同的进行合并，没有的数据自动补全为NaN
