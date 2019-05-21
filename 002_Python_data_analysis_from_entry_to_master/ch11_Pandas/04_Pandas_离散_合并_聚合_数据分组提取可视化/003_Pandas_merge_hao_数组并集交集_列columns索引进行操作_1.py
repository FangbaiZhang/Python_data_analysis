# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 构造两个数组
df1 = pd.DataFrame(np.ones((2, 4)), index=['A', 'B'], columns=list('abcd'))
df2 = pd.DataFrame(np.arange(9).reshape(3, 3), index=['A', 'B', 'C'], columns=list('fax'))
print(df1)
print(df2)
print('*' * 100)

# 上面默认的是内连接hao = 'inner'，取的交集,outer取的并集
# 外连接，相同的进行合并，没有的数据自动补全为NaN
# df1的B行与df2的A行合并，df1的A行补全,df2的BC行补全，最终得到4行
print(df1.merge(df2, on='a', how='outer'))
print('*' * 100)

# left以左连接为基准补全，行数即df1的两行，即以df1为基准补全
# df1的A和B行分别和df2的A行进行合并
print(df1.merge(df2, on='a', how='left'))
print('*' * 100)

# right以右连接为基准补全，行数即df2的三行，即以df2为基准补全
# df2的A行先分别和df1的A和B行进行合并，然后df2的B和C行继续合并，df1没有则自动以NaN补全
print(df1.merge(df2, on='a', how='right'))
print('*' * 100)