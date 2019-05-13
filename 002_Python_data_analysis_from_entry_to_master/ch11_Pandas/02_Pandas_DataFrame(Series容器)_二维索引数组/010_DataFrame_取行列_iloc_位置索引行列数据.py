# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个二维索引数组
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
print(t3)
print(type(t3))
print('*' * 100)

# 取连续的，只要一个中括号，使用冒号
t6 = t3.loc['a':'c', ['W', 'Z']]
print(t6)
print('*' * 100)

# iloc使用方法和loc一样，只不过使用的是标签的位置
t7 = t3.iloc[0:3, [0, 3]]
print(t7)
print('*' * 100)

# 上面两种方法取出结果一样
# 位置索引适合取首尾或者指定固定位置
