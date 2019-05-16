# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

# 创建一个二维索引数组
t3 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('abc'), columns=list('WXYZ'))
print(t3)
print(type(t3))
print('*' * 100)

# 取连续多行loc['a':'c']，冒号和一个中括号
# 取不连续多行，逗号和两个中括号
t5 = t3.loc[['a', 'c']]
print(t5)
print(type(t5))
print('*' * 100)

# 取连续的，只要一个中括号，使用冒号
t6 = t3.loc['a':'c', ['W', 'Z']]
print(t6)
print('*' * 100)

# 取不连续的，两个中括号，使用逗号
t7 = t3.loc[['a','c'], ['W', 'Z']]
print(t7)
print('*' * 100)

# 注意，只获取行，列的冒号不用写
# 但是，只获取列，行的冒号需要写
t8 = t3.loc[:, 'Y':'Z']
print(t8)
print('*' * 100)