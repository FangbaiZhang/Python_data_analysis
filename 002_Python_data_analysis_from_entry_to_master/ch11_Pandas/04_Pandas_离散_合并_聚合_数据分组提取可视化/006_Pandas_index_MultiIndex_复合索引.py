# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个DataFrame
df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list('abc'), columns=list('abcd'))
print(df)
print('*' * 100)

# 设置复合索引，a和d作为前两列，是行的复合索引
df1 = df.set_index(['a', 'd'])
print(df1)
print('*' * 100)
print(df1.info())
print('*' * 100)
print(df1.index)
print('*' * 100)
# 输出结果中的levels就是复合索引中的a和d,a的索引具体值是[0, 4, 8],d的具体值是[3, 7, 11]
# levels中的a列表是外层的索引，d是内层的索引
# labels是每个值所在行对应的索引位置
# names就是索引的名称

